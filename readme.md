# AFC Requirement

### User

- Sign in
- Sign up
- Reset password
- Get profile
- Update profile

### Teacher<User>

- Get current teacher courses
- Create course
- Update course
- Delete course
- Adding attendance
- Upload attendance photo to get students face
- Update attendance

### Student<User>

- Get alvaible courses
- Get enrolled courses
- Enroll a course

### API Endpoint for User

| URL                        | Method | Description                 |
| -------------------------- | ------ | --------------------------- |
| /api/user/register/teacher | POST   | Sign up as teacher          |
| /api/user/register/student | POST   | Sign up as student          |
| /api/user/reset/password   | POST   | Reset user password         |
| /api/user/profile          | GET    | Get current user profile    |
| /api/user/profile          | PUT    | Update current user profile |

### API Endpoint for Student

| URL                             | Method | Description                     |
| ------------------------------- | ------ | ------------------------------- |
| /api/student/course             | GET    | Get alvaiable course to enroll  |
| /api/student/enroll             | GET    | Get all current student courses |
| /api/student/enroll/<course_id> | POST   | Student enroll a course         |

### API Endpoint for Teacher

| URL                                                       | Method | Description                                |
| --------------------------------------------------------- | ------ | ------------------------------------------ |
| /api/course                                               | POST   | Create a course                            |
| /api/course/<course_id>                                   | GET    | Get detail course                          |
| /api/course/me                                            | GET    | Get all current teacher courses            |
| /api/course/<course_id>/add/attendance                    | POST   | Create course attendance                   |
| /api/course/<course_id>/add/attendance                    | GET    | Get all courses attendance                 |
| /api/course/<course_id>/add/attendance/<attendance_id>    | GET    | Get detail course attendance               |
| /api/course/<course_id>/fc/attendance/<attendance_id>     | POST   | Upload a photo to recognize students faces |
| /api/course/<course_id>/update/attendance/<attendance_id> | PUT    | Update attendance                          |