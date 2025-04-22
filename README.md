# DTS Developer Challenge - Task Manager API

This is the task manager API for the coding challenge for the MOJ Junior Software Developer. 

## Planning

A simple entity relation diagram was created for the Task model, created with lucidchart.

![ERD diagram of Task model](static/task-api-erd.png)

For simplicity, no User model is being used and the Task model will allow CRUD functionality of tasks to be global. In a real world situation, the User model would be incorporated as a foreign key for an 'owner' field, and authentication for the app would be created.
