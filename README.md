# Hotel Management System (HMS-Flask)

[![Python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.2.2-000000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF.svg?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![AWS](https://img.shields.io/badge/Deployed_on-AWS_EC2-FF9900.svg?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/ec2/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

[cite_start]A cloud-native Hotel Management System (HMS) built with Flask and SQLite3, demonstrating a complete DevSecOps lifecycle[cite: 4]. [cite_start]This project, developed for the MSc. in Cloud Computing at the National College of Ireland [cite: 2][cite_start], features a secure CRUD application with a fully automated CI/CD pipeline for deployment to AWS EC2[cite: 6, 28].

[cite_start]**Live Demo URL:** **[http://108.129.170.142:5000/](http://108.129.170.142:5000/)** [cite: 13, 141]

<br>

<p align="center">
  <img src=".github/assets/3.jpg" alt="Landing Page" width="90%">
</p>

## ✨ Key Features

* [cite_start]**Secure Admin Dashboard**: Full CRUD (Create, Read, Update, Delete) functionality for managing hotel rooms, protected by a secure admin login with hashed passwords[cite: 5, 33, 38].
* [cite_start]**Public Room Catalog**: A public-facing view where users can browse room listings without requiring authentication[cite: 12, 34].
* [cite_start]**Automated CI/CD Pipeline**: Every push to the `main` branch triggers a GitHub Actions workflow that automatically deploys the application to an AWS EC2 instance[cite: 8, 89, 117].
* [cite_start]**Static Code Analysis**: Integrated with `pylint` and SonarQube Cloud to proactively identify and fix code quality issues and security vulnerabilities[cite: 10, 165, 166].
* [cite_start]**Secure Cloud Architecture**: Deployed within a custom VPC on AWS with securely configured security groups and SSH key management for access control[cite: 7, 30, 40].

## 🏗️ System Architecture & CI/CD

[cite_start]The application follows a modular MVC (Model-View-Controller) structure to ensure maintainability and scalability[cite: 35, 56]. [cite_start]The core CI/CD pipeline automates the entire deployment process, from code commit to live application[cite: 96, 99].

1.  [cite_start]A developer pushes code to the private GitHub repository[cite: 115].
2.  [cite_start]A GitHub Actions workflow is automatically triggered[cite: 117].
3.  [cite_start]The workflow establishes a secure SSH connection to the AWS EC2 instance using credentials stored in GitHub Secrets[cite: 120, 129].
4.  [cite_start]On the server, the script pulls the latest code, sets up the environment, installs dependencies, and restarts the Flask application[cite: 122, 136].

<p align="center">
  <img src=".github/assets/cicd.jpg" alt="CI/CD Pipeline Diagram" width="70%">
</p>

## 🛠️ Technology Stack

| Category      | Technologies & Tools                                 |
| :------------ | :--------------------------------------------------- |
| **Backend** | [cite_start]`Flask`, `Python 3.11` [cite: 82, 42]                    |
| **Database** | [cite_start]`SQLite3` [cite: 84]                                       |
| **Frontend** | [cite_start]`HTML`, `CSS`, `Bootstrap` [cite: 86]                     |
| **Cloud** | [cite_start]`AWS EC2`, `VPC`, `Security Groups` [cite: 90, 40]         |
| **CI/CD** | [cite_start]`Git`, `GitHub`, `GitHub Actions` [cite: 87, 89]      |
| **DevSecOps** | [cite_start]`SonarQube Cloud`, `pylint` [cite: 92, 93]          |


## 📂 Project Structure

The project is organized with a clean and understandable structure:
