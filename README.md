<p align="center">
  <img src=".github/assets/01-landing-page.jpg" alt="Landing Page" width="80%">
</p>

## Key Features

* [cite_start]**Secure Admin Authentication**: Dedicated login for administrators with password hashing to protect credentials[cite: 9, 38].
* [cite_start]**Full Room Management (CRUD)**: Admins can add, view, update, and delete room details, including number, type, price, and availability[cite: 5, 33, 52].
* [cite_start]**Public Room Listings**: General users can view all available rooms without needing to log in, ensuring usability and accessibility[cite: 12, 34].
* [cite_start]**Responsive Frontend**: A clean and user-friendly interface built with Bootstrap[cite: 86].
* [cite_start]**Input Validation**: Server-side and client-side validation to ensure data integrity and prevent injection attacks[cite: 37].

<details>
<summary><b>Click to see more screenshots</b></summary>
<br>
<table>
  <tr>
    <td><img src=".github/assets/02-admin-login.jpeg" alt="Admin Login"></td>
    <td><img src=".github/assets/03-all-rooms-view.jpeg" alt="All Rooms"></td>
  </tr>
  <tr>
    <td align="center"><em>Admin Login Page</em></td>
    <td align="center"><em>All Rooms View</em></td>
  </tr>
  <tr>
    <td><img src=".github/assets/04-add-new-room.jpeg" alt="Add New Room"></td>
    <td><img src=".github/assets/05-edit-room.jpeg" alt="Edit Room"></td>
  </tr>
  <tr>
    <td align="center"><em>Add New Room Form</em></td>
    <td align="center"><em>Edit Room Form</em></td>
  </tr>
</table>
</details>

## System Architecture & CI/CD Pipeline

[cite_start]The application is built on a modular MVC (Model-View-Controller) architecture using the Flask framework[cite: 35, 56]. [cite_start]It is hosted on an **AWS EC2 instance** within a custom VPC in the `eu-west-1` (Ireland) region[cite: 7, 39, 97].

[cite_start]The project features a complete CI/CD pipeline automated with **GitHub Actions**[cite: 8, 89]. [cite_start]On every push to the `main` branch, the pipeline automatically triggers, connects to the EC2 server via SSH, and deploys the latest version of the application[cite: 8, 117, 120]. [cite_start]This ensures continuous delivery and high reliability[cite: 46, 98].

<p align="center">
  <img src=".github/assets/architecture-cicd-pipeline.jpg" alt="CI/CD Pipeline Diagram" width="60%">
  <br>
  <em>CI/CD Pipeline Workflow.</em>
</p>

## Technology Stack

| Category | Technology | Description |
|---|---|---|
| **Backend** | `Flask` | [cite_start]A lightweight Python web framework for building the application logic and API[cite: 82]. |
| **Database** | `SQLite3` | [cite_start]A simple, file-based relational database for data persistence[cite: 36, 84]. |
| **Frontend** | `HTML`, `CSS`, `Bootstrap` | [cite_start]Used for creating a clean, responsive, and user-friendly interface[cite: 86]. |
| **Cloud Hosting**| `AWS EC2` | [cite_start]The virtual server where the application is deployed and hosted[cite: 7, 90]. |
| **CI/CD** | `Git`, `GitHub Actions` | [cite_start]For version control and automating the build, test, and deployment pipeline[cite: 87, 89]. |
| **Code Analysis**| `pylint`, `SonarQube Cloud` | [cite_start]Static analysis tools to ensure code quality, maintainability, and security[cite: 10, 92, 93]. |


## Static Code Analysis

[cite_start]As part of DevSecOps best practices, the codebase was continuously analyzed using `pylint` and `SonarQube Cloud`[cite: 10, 165, 166]. [cite_start]This helped identify and fix potential bugs, security vulnerabilities, and code smells early in the development cycle[cite: 164, 236].

<p align="center">
  <img src=".github/assets/analysis-pylint-output.png" alt="Pylint Scan Output" width="70%">
  <br>
  [cite_start]<em>Example `pylint` output, which scored the code 8.43/10[cite: 183].</em>
</p>
