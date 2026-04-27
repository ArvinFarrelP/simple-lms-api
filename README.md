# 🎓 Simple LMS API

REST API untuk sistem Learning Management System (LMS) menggunakan Django Ninja, JWT Authentication, dan Role-Based Access Control (RBAC).

---

## 🚀 Features

- 🔐 JWT Authentication (Access + Refresh Token)
- 👥 Role-Based Access Control (Admin, Instructor, Student)
- 📚 Course Management (CRUD)
- 📝 Enrollment System
- 📈 Progress Tracking
- 📄 Pagination Support
- 📊 Swagger API Documentation

---

## 🧠 Roles

| Role       | Permissions                     |
| ---------- | ------------------------------- |
| Admin      | Full access (CRUD semua course) |
| Instructor | Create & manage own courses     |
| Student    | Enroll & track progress         |

---

## 🔑 Authentication Flow

1. Login → mendapatkan `access_token` & `refresh_token`
2. Gunakan `access_token` untuk akses endpoint protected
3. Jika expired → gunakan `refresh_token`

---

## 📡 API Endpoints

### Authentication

- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/refresh`
- `GET /api/auth/me`
- `PUT /api/auth/me`

### Courses

- `GET /api/courses`
- `GET /api/courses/{id}`
- `POST /api/courses` (Instructor)
- `PATCH /api/courses/{id}` (Owner/Admin)
- `DELETE /api/courses/{id}` (Admin)

### Enrollments

- `POST /api/enrollments`
- `GET /api/enrollments/my-courses`
- `POST /api/enrollments/{id}/progress`

---

## 📄 Pagination Example
