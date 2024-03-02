# QuizBowl

QuizBowl is a web-based application that allows users to participate in a quiz game. The application is built using Flask, a Python web framework, and uses SQLite for data storage.

## Features

- User registration and login system
- Dashboard for participating in the quiz
- Question options for selecting difficulty and category
- Real-time question fetching and answering

## Installation

1. Clone the repository:
```sh
git clone https://github.com/yourusername/quizbowl.git
cd quizbowl
```

2. Install the required Python packages:
```sh
pip install -r requirements.txt
```

3. Run the application:
```sh
python run.py
```

The application will be accessible at http://localhost:5000.

## Project Structure

The project has the following structure:

- `app/`: Contains the main application code.
  - `__init__.py`: Initializes the Flask application and its extensions.
  - `routes.py`: Defines the routes for the application.
- `models/`: Contains the SQLAlchemy models.
- `api/`: Contains the routes for the API.
- `site/`: Contains the routes for the site.
- `admin/`: Contains the routes for the admin interface.
- `static/`: Contains the static files (CSS, JavaScript, images).
- `templates/`: Contains the HTML templates.
- `instance/`: Contains instance-specific configuration files.
- `migrations/`: Contains the Alembic migration scripts.
- `run.py`: The entry point for running the application.
- `requirements.txt`: Lists the Python dependencies for the project.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the terms of the MIT license. See the LICENSE file for details.
