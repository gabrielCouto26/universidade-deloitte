# Deloitte University Challenge

A modern university management system backend built with Django Rest Framework. This RESTful API provides endpoints for managing students, teachers, coordinators, disciplines, and grades with role-based access control and token authentication.

## Overview

This project implements a backend solution for university administration. The system supports multiple user roles (Students, Teachers, and Coordinators) with permission-based access control. It features a modular architecture that separates concerns into distinct modules for authentication, student management, teacher management, discipline management, and grade tracking.

## Architecture

The application follows a modular architecture pattern with the following components:

- **Authentication Module**: Token-based user authentication and session management with role-based permissions
- **User Management**: User model with support for Students, Teachers, and Coordinators
- **Student Management**: Create, view, and manage student records with grade tracking
- **Teacher Management**: Create, view, and manage teacher records with discipline and grade management
- **Discipline Management**: Manage courses/subjects with detailed information and student enrollment
- **Grade Management**: Track and manage student grades with full CRUD operations
- **Permission System**: Flexible permission model that adapts to authenticated user roles
- **RESTful API**: Comprehensive API endpoints following REST principles

## Technology Stack

- **Framework**: Django 4.2.x
- **API Framework**: Django Rest Framework
- **Database**: MySQL (relational database)
- **Authentication**: Token Authentication (DRF Token Authentication)
- **CORS**: django-cors-headers for cross-origin resource sharing
- **Python**: Python 3.x

## Getting Started

### Prerequisites

- Python 3.x (3.8 or higher recommended)
- MySQL database server
- pip package manager
- Virtual environment tool (venv or virtualenv)

### Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On Linux/Mac
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

3. Install required packages:
```bash
pip install Django
pip install djangorestframework
pip install django-cors-headers
pip install mysqlclient
```

### Database Setup

1. Create a MySQL database for the project
2. Update database settings in `universidade_deloitte/settings.py` with your database credentials
3. Run migrations:
```bash
python manage.py migrate
```

### Development

Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## System Flow

1. **Authentication**: Users authenticate through token-based authentication, receiving an access token upon successful login
2. **Permission Loading**: Upon successful authentication, user permissions are retrieved and used to determine API endpoint access
3. **Role-Based Access**: API endpoints enforce permissions based on user roles (Students, Teachers, Coordinators)
4. **CRUD Operations**: Each module (Students, Teachers, Disciplines, Grades) provides full CRUD operations through RESTful endpoints
5. **Data Management**: All data operations are performed through API calls, with proper serialization and validation

## API Endpoints

- **Authentication**: `/api-token-auth/` - Token authentication endpoint
- **User Info**: `/api/user-info` - Get authenticated user information
- **Students**: `/api/students/` - List and create students
- **Students Detail**: `/api/students/<id>` - Retrieve, update, or delete a student
- **Student Grades**: `/api/students/grades` - Get grades for authenticated student
- **Teachers**: `/api/teachers/` - List and create teachers
- **Teachers Detail**: `/api/teachers/<id>` - Retrieve, update, or delete a teacher
- **Teacher Grades**: `/api/teachers/grades` - Get grades managed by authenticated teacher
- **Teacher Disciplines**: `/api/teachers/disciplines` - Get disciplines taught by authenticated teacher
- **Disciplines**: `/api/disciplines/` - List and create disciplines
- **Disciplines Detail**: `/api/disciplines/<id>` - Retrieve, update, or delete a discipline
- **Discipline Students**: `/api/disciplines/<id>/students` - Get students enrolled in a discipline
- **Grades**: `/api/grades/` - List and create grades
- **Grades Detail**: `/api/grades/<id>` - Retrieve, update, or delete a grade

## Frontend Repository

This backend is designed to work with the frontend application:
https://github.com/gabrielCouto26/universidade-deloitte-frontend

Make sure to configure CORS settings in `settings.py` to allow requests from your frontend application.
