# Movie Rater Project

The Movie Rater project is a Django-based backend application that provides a robust API for managing a list of movies, allowing users to rate these movies. This backend connects seamlessly with a React frontend to create an interactive and user-friendly movie rating platform.

## Features

- **Movies Database:** Store and manage a list of movies, including their details such as title, description, and release year.

- **User Ratings:** Users can rate movies on a scale of 1 to 5, helping to create a community-based movie rating system.

- **CRUD Operations:** Perform CRUD (Create, Read, Update, Delete) operations on movies. Add, retrieve, update, and delete movie entries with ease.

- **API Endpoints:** Exposes a set of RESTful API endpoints for interaction with the movie database.

## Technology Stack

- **Django:** The project is built using the Django web framework, which provides a robust and secure environment for web development.

- **React:** The frontend is developed in React, offering a dynamic and user-friendly interface for users to browse and rate movies.

## Installation

Before running the Movie Rater project, you need to install the required dependencies and set up the database. Follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/movie_rater.git
   cd movie_rater
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create the database schema:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for accessing the Django admin:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

7. Navigate to the Django admin interface at `http://localhost:8000/admin/` and log in with your superuser credentials to add movies to the database.

8. You can access the API at `http://localhost:8000/api/movies/`.

9. To connect the backend to the React frontend, follow the setup instructions in the `frontend` directory of this project.

## API Endpoints

- **List Movies:** `/api/movies/` (GET)
- **Create Movie:** `/api/movies/` (POST)
- **Retrieve Movie Details:** `/api/movies/{movie_id}/` (GET)
- **Update Movie Details:** `/api/movies/{movie_id}/` (PUT)
- **Delete Movie:** `/api/movies/{movie_id}/` (DELETE)
- **List Ratings for a Movie:** `/api/movies/{movie_id}/ratings/` (GET)
- **Rate a Movie:** `/api/movies/{movie_id}/rate/` (POST)

## Usage

The Movie Rater project is designed to be used in conjunction with a React frontend that consumes the provided API endpoints. Users can browse, rate, and manage movies via the React interface.
