# Django Multi-User Blog

## Project Overview

The Django Multi-User Blog is a web-based blogging platform designed to facilitate content creation, management, and discovery. It features user authentication, content visibility controls, media management, and an intuitive interface. The project is built using Django and follows best practices for security and performance.

## Features

### User Authentication and Profile Management

- User registration, login, logout, and password reset via email.
- Profile management with support for uploading and updating profile pictures.
- CAPTCHA integration to prevent automated spam registrations.

### Blog Post Management

- Users can create, edit, and delete blog posts.
- Visibility control allows posts to be set as either public or private.
- Image uploads for posts, with automatic resizing to optimize storage.

### Search and Navigation

- Search functionality to filter posts by author.
- Paginated display of posts (five posts per page).
- Filtered views to display public posts from different users.

### User Interface

- A structured homepage displaying posts authored by the logged-in user.
- Dedicated post detail pages for individual blog entries.
- An about page outlining the platform’s purpose and functionality.

### Security and Access Control

- Authentication is required for content creation and profile management.
- Users can only edit or delete their own posts.
- Private posts are only accessible to the post author.

### Media Management

- Profile and post images are stored in an organized directory structure.
- Automatic image resizing ensures optimized storage.

### Deployment Readiness

- Static and media files are properly configured for production.
- SMTP email settings are integrated for password recovery.


## Technologies Used

- **Backend:** Django, SQLite
- **Frontend:** Bootstrap, HTML, CSS
- **Libraries:** Pillow (image processing), django-crispy-forms (form styling), django-simple-captcha (spam protection)

