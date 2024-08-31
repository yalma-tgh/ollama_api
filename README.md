
# Django API with Ollama Integration

This is a Django-based API that integrates with Ollama, a language model service. The main feature of this API is a chat endpoint at `localhost/api/chat` which allows you to send requests and receive responses from the language model.

## Project Structure

```
.
├── asgi.py              # ASGI configuration for the Django project
├── __init__.py          # Initialization file for the Django project
├── manage.py            # Django management script
├── ollama_app           # Main application folder
│   ├── admin.py         # Admin site configuration
│   ├── apps.py          # Application configuration
│   ├── __init__.py      # Initialization file for the app
│   ├── migrations       # Database migrations folder
│   │   └── __init__.py  # Initialization file for migrations
│   ├── models.py        # Database models
│   ├── tests.py         # Unit tests for the application
│   ├── urls.py          # Application-specific URL routing
│   └── views.py         # Views handling API requests
├── requirements.txt     # Dependencies for the project
├── settings.py          # Main configuration file for the project
├── urls.py              # URL routing for the entire project
└── wsgi.py              # WSGI configuration for deployment
```

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Pip (Python package manager)

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**:

   - On Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - On MacOS/Linux:

     ```bash
     source env/bin/activate
     ```

4. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Start the development server**:

   ```bash
   python manage.py runserver
   ```

   The server will start at `http://127.0.0.1:8000/`.

## Using the API

### Chat Endpoint

- **URL**: `http://localhost:8000/api/chat`
- **Method**: `POST`
- **Description**: This endpoint allows you to send chat requests to the Ollama service.

#### Request Format

Send a JSON request with the necessary input, for example:

```json
{
  "message": "Hello, how are you?"
}
```

#### Response Format

The response will be in JSON format, containing the reply from the Ollama service:

```json
{
  "response": "I'm good, thank you! How can I assist you today?"
}
```

## Project Configuration

- **`settings.py`**: Configure your database, installed apps, middleware, and other Django settings here.
- **Environment Variables**: Make sure to set up any required environment variables, such as secret keys or API keys for connecting to Ollama.
