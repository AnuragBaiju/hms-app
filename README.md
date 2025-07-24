# Hotel Management System (HMS-Flask)

[![Python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.2.2-000000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF.svg?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![AWS](https://img.shields.io/badge/Deployed_on-AWS_EC2-FF9900.svg?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/ec2/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A cloud-native Hotel Management System (HMS) built with Flask and SQLite3, demonstrating a complete DevSecOps lifecycle. This project, developed for the MSc. in Cloud Computing at the National College of Ireland, features a secure CRUD application with a fully automated CI/CD pipeline for deployment to AWS EC2.


<br>

<p align="center">
  <img src=".github/assets/01-landing-page.jpg" alt="Landing Page" width="90%">
</p>

## ✨ Key Features

* **Secure Admin Dashboard**: Full CRUD (Create, Read, Update, Delete) functionality for managing hotel rooms, protected by a secure admin login with hashed passwords.
* **Public Room Catalog**: A public-facing view where users can browse room listings without requiring authentication.
* **Automated CI/CD Pipeline**: Every push to the `main` branch triggers a GitHub Actions workflow that automatically deploys the application to an AWS EC2 instance.
* **Static Code Analysis**: Integrated with `pylint` and SonarQube Cloud to proactively identify and fix code quality issues and security vulnerabilities.
* **Secure Cloud Architecture**: Deployed within a custom VPC on AWS with securely configured security groups and SSH key management for access control.

## 🏗️ System Architecture & CI/CD

The application follows a modular MVC (Model-View-Controller) structure to ensure maintainability and scalability. The core CI/CD pipeline automates the entire deployment process, from code commit to live application.

1.  A developer pushes code to the private GitHub repository.
2.  A GitHub Actions workflow is automatically triggered.
3.  The workflow establishes a secure SSH connection to the AWS EC2 instance using credentials stored in GitHub Secrets.
4.  On the server, the script pulls the latest code, sets up the environment, installs dependencies, and restarts the Flask application.

<p align="center">
  <img src=".github/assets/architecture-cicd-pipeline.jpg" alt="CI/CD Pipeline Diagram" width="70%">
</p>

## 🛠️ Technology Stack

| Category      | Technologies & Tools                                 |
| :------------ | :--------------------------------------------------- |
| **Backend** | `Flask`, `Python 3.11`                     |
| **Database** | `SQLite3`                                        |
| **Frontend** | `HTML`, `CSS`, `Bootstrap`                      |
| **Cloud** | `AWS EC2`, `VPC`, `Security Groups`          |
| **CI/CD** | `Git`, `GitHub`, `GitHub Actions`       |
| **DevSecOps** | `SonarQube Cloud`, `pylint`           |


## 📂 Project Structure

The project is organized with a clean and understandable structure:
