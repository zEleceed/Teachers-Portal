# Teacher's Classroom Management Portal

## Overview
This web application, built with Python and Django, serves as a platform for teachers to efficiently manage classrooms and student information. It supports basic registration and deletion functionalities, classroom folder management, student management within those folders, and allows teachers to note and record noteworthy events happening during class, organized by month.

## Features

### User Registration and Authentication
- Secure registration and login system for teachers.
- Password recovery and user management options.

### Classroom Management
- Ability to create, update, and delete classroom folders.
- Classrooms are associated with specific teachers.

### Student Management
- Add, update, move, and delete student records within classroom folders.
- Manage student information effectively.

### Daily Comments
- Teachers can add comments for each class, organized by month.
- Option to edit or delete past comments.

## User Stories

### Classroom Management
- **As a teacher, I want to create, update, and delete classroom folders so that I can manage my classes effectively.**

  **Acceptance Criteria:**
  - Can create a new classroom folder with a unique name.
  - Can update the name/details of an existing classroom.
  - Can delete a classroom folder.

### Student Management
- **As a teacher, I want to add, move, and delete students from classroom folders so that I can keep my class lists up to date.**

  **Acceptance Criteria:**
  - Can add a student with necessary details to a classroom.
  - Can move a student from one classroom to another.
  - Can delete a student from a classroom.

### Daily Comments
- **As a teacher, I want to note down and save noteworthy events for each day, organized by month, so that I can track classroom activities and progress over time.**

  **Acceptance Criteria:**
  - Can add a comment for a specific day under a classroom.
  - Can view comments organized by month.
  - Can edit or delete past comments.

