"""Hotel Management System using Flask and SQLite3."""

import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

# Flask app setup
app = Flask(__name__)
app.secret_key = 'mysecretkey'
DATABASE = 'database.db'


def init_db():
    """Initialize or migrate database with required tables."""
    with sqlite3.connect(DATABASE, timeout=10) as conn:
        cursor = conn.cursor()

        # Create rooms table
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                room_number TEXT NOT NULL,
                room_type TEXT NOT NULL,
                price_per_night REAL NOT NULL,
                availability TEXT NOT NULL,
                description TEXT
            )
            '''
        )

        # Create admin table
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS admin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
            '''
        )

        # Insert default admin if not exists
        existing_admin = cursor.execute(
            "SELECT * FROM admin WHERE username = ?", ("admin",)
        ).fetchone()

        if not existing_admin:
            hashed_pw = generate_password_hash("admin123", method='pbkdf2:sha256')
            cursor.execute("INSERT INTO admin (username, password) VALUES (?, ?)", ("admin", hashed_pw))

        conn.commit()


@app.route('/')
def home():
    """Landing home page."""
    return render_template('home.html')


@app.route('/rooms')
def list_rooms():
    """Display all hotel rooms."""
    with sqlite3.connect(DATABASE, timeout=10) as conn:
        rooms = conn.execute("SELECT * FROM rooms").fetchall()
    return render_template('rooms.html', rooms=rooms)


@app.route('/add', methods=['GET', 'POST'])
def add_room():
    """Add a new room (admin only)."""
    if 'admin_logged_in' not in session:
        flash("You must be logged in as admin to add a room.", "danger")
        return redirect(url_for('login'))

    if request.method == 'POST':
        room_number = request.form.get('room_number')
        room_type = request.form.get('room_type')
        price_per_night = float(request.form.get('price_per_night'))
        availability = request.form.get('availability')
        description = request.form.get('description')

        with sqlite3.connect(DATABASE, timeout=10) as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                INSERT INTO rooms (room_number, room_type, price_per_night, availability, description)
                VALUES (?, ?, ?, ?, ?)
                ''',
                (room_number, room_type, price_per_night, availability, description)
            )
            conn.commit()

        flash('Room added successfully!', 'success')
        return redirect(url_for('list_rooms'))

    return render_template('add_room.html')


@app.route('/edit/<int:room_id>', methods=['GET', 'POST'])
def edit_room(room_id):
    """Edit an existing room (admin only)."""
    if 'admin_logged_in' not in session:
        flash("You must be logged in as admin to edit a room.", "danger")
        return redirect(url_for('login'))

    with sqlite3.connect(DATABASE, timeout=10) as conn:
        cursor = conn.cursor()

        if request.method == 'POST':
            room_number = request.form.get('room_number')
            room_type = request.form.get('room_type')
            price_per_night = float(request.form.get('price_per_night'))
            availability = request.form.get('availability')
            description = request.form.get('description')

            cursor.execute(
                '''
                UPDATE rooms
                SET room_number = ?, room_type = ?, price_per_night = ?, availability = ?, description = ?
                WHERE id = ?
                ''',
                (room_number, room_type, price_per_night, availability, description, room_id)
            )
            conn.commit()
            flash('Room updated successfully!', 'success')
            return redirect(url_for('list_rooms'))

        room = cursor.execute("SELECT * FROM rooms WHERE id = ?", (room_id,)).fetchone()

    return render_template('edit_room.html', room=room)


@app.route('/delete/<int:room_id>', methods=['POST'])
def delete_room(room_id):
    """Delete a room (admin only)."""
    if 'admin_logged_in' not in session:
        flash("You must be logged in as admin to delete a room.", "danger")
        return redirect(url_for('login'))

    with sqlite3.connect(DATABASE, timeout=10) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM rooms WHERE id = ?", (room_id,))
        conn.commit()

    flash('Room deleted.', 'info')
    return redirect(url_for('list_rooms'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login route."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with sqlite3.connect(DATABASE, timeout=10) as conn:
            cursor = conn.cursor()
            admin = cursor.execute("SELECT * FROM admin WHERE username = ?", (username,)).fetchone()

            if admin and check_password_hash(admin[2], password):
                session['admin_logged_in'] = True
                session['admin_user'] = username
                flash("Logged in successfully!", "success")
                return redirect(url_for('list_rooms'))

        flash("Invalid username or password", "danger")

    return render_template('login.html')


@app.route('/logout')
def logout():
    """Admin logout route."""
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for('home'))


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
