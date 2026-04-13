# Django Blog API

## Overview
A REST API for a blog built with Django and Django REST Framework.
Supports authentication, permissions, and Dockerized setup.

## Features
- CRUD for posts
- User authentication
- Permissions
- Docker support

## Tech Stack
- Django
- Django REST Framework
- Docker
- SQLite

## Run with Docker

```bash
docker-compose up --build

The app will be available at:
http://localhost:8000

## 5. Environment variables

Create a `.env` file:

SECRET_KEY=your_secret_key
DEBUG=True

## API Endpoints

- /api/v1/ - list/create posts
- /api/v1/<id>/ - retrieve/update/delete post