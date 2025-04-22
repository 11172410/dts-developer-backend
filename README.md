# DTS Developer Challenge - Task Manager API

This is the task manager API for the coding challenge for the MOJ Junior Software Developer. The backend for the task manager application is written in the Python language, using the Django REST Framework to create a RESTful API.

## Planning

A simple entity relation diagram was created for the Task model, created with lucidchart.

![ERD diagram of Task model](static/task-api-erd.png)

For simplicity, no User model is being used and the Task model will allow CRUD functionality of tasks to be global. In a real world situation, the User model would be incorporated as a foreign key for an 'owner' field, and authentication for the app would be created.

Each task has the option of a title, an optional description (indicated by blank = True), a status which can toggle between incomplete and complete, a due date and a due time.