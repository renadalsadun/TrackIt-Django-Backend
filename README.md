

# Track IT - Backend
## Description
Track IT is a full stack web application, built using React, Django REST Framework, and PostgreSQL. It is designed to help users create trackers, manage them, log applications, and attach related documents.

This project was individually developed during the last week of Software Engineering Bootcamp By General Assembly.



## Tech Stack
**Backend:**
Python, JavaScript, PostgreSQL

**Frontend:**
React, React Router, React Toastify, Bulma CSS, Axios, Uploadcare, JWT


### Front End Repo Link

[Frontend Repo Link](https://git.generalassemb.ly/renad/TrackIt-React-Frontend)

## ER Diagram

![erd](<Screenshot 2025-05-08 at 2.07.40 AM.png>)

## Routing Table
### 1. SERVER
| Route Name           | URL                                   | HTTP Verb | Description                     |
| :------------------- | :------------------------------------ | :-------- | :------------------------------ |
| signup               | `api/signup/`                         | POST      | Signup new user                 |
| obtain_token_pair    | `api/token/ `                         | POST      | Get token pair                  |
| tracker-list         | `api/trackers/`                       | GET       | List all Trackers               |
| tracker-create       | `api/trackers/new`                    | POST      | Create a new Tracker            |
| tracker-detail       | `api/tracker/<int:pk>/`               | GET       | List all Tracker Detail         |
| tracker-update       | `api/tracker/<int:pk>/update/`        | PATCH     | Edit a Tracker                  |
| tracker-delete       | `api/tracker/<int:pk>/delete/`        | DELETE    | Delete a Tracker                |
| application-list     | `api/applications/`                   | POST      | Create a new Application        |
| application-create   | `api/applications/new/`               | POST      | Create a new Application        |
| application-detail   | `api/applications/<int:pk>/`          | GET       | List all Application details    |
| application-update   | `api/applications/<int:pk>/update/`   | PATCH     | Edit Application                |
| application-delete   | `api/applications/<int:pk>/delete`    | DELETE    | Delete Application              |
| application-documents| `api/applications/<int:pk>/documents/`| GET       | List all Application’s Documents|
| document-new         | `api/documents/`                      | POST      | Create a new Document           |
document-list  |	`api/documents/`|	GET	|List all Documents|
document-create|	`api/documents/new/`|	POST|	Create a new Document|
document-detail|	`api/documents/<int:pk>/`|	GET|	Get Document Detail|
document-update|	`api/documents/<int:pk>/update/`|	PATCH|	Update a Document|
document-delete|	`api/documents/<int:pk>/delete/`|	DELETE|	Delete a Document|






### 2. CLIENT

| Route Name            | URL                                                  | HTTP Verb | Description                         |
| :-------------------- | :--------------------------------------------------- | :-------- | :---------------------------------- |
| signup                | `/signup`                                            | POST      | Signup new user                     |
| login                 | `/login`                                             | POST      | Login user                          |
| home                  | `/home`                                              | GET       | Display user's dashboard/home       |
| trackers              | `/`                                                  | GET       | List all Trackers (Main Page)       |
| tracker_detail        | `/trackers/:id`                                      | GET       | View Tracker Detail                 |
| tracker_add           | `/trackers/add`                                      | POST      | Create a new Tracker                |
| tracker_edit          | `/trackers/:id/edit`                                 | PATCH     | Edit a Tracker                      |
| application_add       | `/trackers/:trackerId/applications/add`              | POST      | Create a new Application            |
| application_edit      | `/trackers/:trackerId/applications/:applicationId/edit` | PATCH  | Edit an Application                 |
| document_add          | `/documents/add`                                     | POST      | Create a new Document               |
| document_list         | `/documents`                                         | GET       | List all Documents                  |
| not_found             | `/not-found` or `*`                                  | -         | Page Not Found                      |






## Installation Instructions
1. Clone Repositories:


`https://git.generalassemb.ly/renad/TrackIt-React-Frontend.git`
`https://git.generalassemb.ly/renad/TrackIt-Django-Backend.git`

2. Set up the Backend 


`cd backend-folder`



`pipenv shell`



`python manage.py runserver`



3. Set up Frontend 


`cd frontend-folder`



`npm install`



`npm run dev`





## IceBox Features
- Allow users to create custom fields for their trackers, giving them full control over the structure of their data.
- Add a new user type (Organizations) with special features like posting application openings, announcements, and managing applicants. 
- Enable notifications and/or calendar reminders for upcoming application deadlines 
- Add filters and search functionality to easily browse applications and trackers.