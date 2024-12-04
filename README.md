# Lost and Found Management System

## Introduction

The **Lost and Found Management System** is a microservices-based application designed to help individuals report and manage lost and found items efficiently. By leveraging a scalable architecture, this system aims to connect users who have lost items with those who have found them, facilitating easy communication and resolution.

## Project Overview

This project is developed as part of our software engineering course, focusing on the principles of distributed systems and microservices architecture. Our team is committed to applying theoretical concepts to create a practical solution for a common real-world problem.

### Objectives

- **Scalability**: The system is designed to handle a large number of users and items efficiently.
- **Reliability**: By implementing fault tolerance and robust communication methods, we aim to ensure consistent service availability.
- **Asynchronous Processing**: Utilizing tools like RabbitMQ and Celery, the system can manage tasks without blocking user interactions.
- **Team Collaboration**: This project enhances our teamwork and collaboration skills as we work together to build a comprehensive solution.

## Microservices

The application consists of three main microservices:

1. **User Service**: Manages user accounts, authentication, and user profiles.
2. **Item Service**: Handles the management of lost and found items, including reporting, searching, and updating item statuses.
3. **Notification Service**: Sends notifications to users regarding items that match their search criteria or updates on reported items.

## Technologies Used

- **Django REST Framework**: For building the APIs.
- **PostgreSQL and MySQL**: For persistent data storage.
- **RabbitMQ**: For inter-service communication.
- **Celery**: For handling asynchronous tasks.
