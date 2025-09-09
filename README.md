# My CV Backend

A backend service for managing CVs, user authentication, and related data. This project is built with Python and designed to support a CV application.

## Table of Contents
- Features
- Project Structure
- Setup & Installation
- Usage
- Database Setup
- API Endpoints
- Testing
- License

## Features
- User authentication and management
- CV creation, update, and retrieval
- Actuator endpoints for health checks
- Modular code structure for easy maintenance

## Project Structure
```
my_cv_backend/
├── app/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   └── migrations/
├── tests/
├── docs/
├── venv/
├── config.py
├── dbInit.sql TODO update the folder structure since db file moved
├── docker-compose.yaml
├── requirements.txt
├── run.py
├── wsgi.py
└── README.md
```

## Setup & Installation

### Database Setup
This project uses PostgreSQL. You can use Podman to run a local PostgreSQL container:

```bash
podman run -d --name my-pg-cv-db -e POSTGRES_USER=mycv -e POSTGRES_PASSWORD=mycv -e POSTGRES_DB=mycv -v C:/Development/DevCamp/my_cv_backend:/docker-entrypoint-initdb.d:Z -p 6543:5432 postgres:17
```
or
```powershell
.\app\migrations\init-db.ps1
```
or 
```bash
podman-compose up -d
```

Start the container:
```bash
podman start my-pg-cv-db
```

View logs:
```bash
podman logs -f my-pg-cv-db
```

Access the container shell:
```bash
podman exec -it my-pg-cv-db bash
```

Enter PostgreSQL prompt:
```bash
psql -U mycv -d mycv
```

List tables:
```psql
\dt
```

Exit PostgreSQL:
```psql
\q
```

Exit container shell:
```bash
exit
```

List tables directly from host:
```bash
podman exec -it my-pg-cv-db psql -U mycv -d mycv -c "\dt"
```

If localhost doesnt work when connecting to the host name. In pgAdmin 4 use the ip from wsl under inet
```bash
ip addr show eth0
```

### python backend server
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd my_cv_backend
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\Activate
   ```
3. **Install from and generate requirements.txt run this command in the root directory**
   ```bash
   pip install -r requirements.txt
   ```

   ```bash
   pip freeze > requirements.txt
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Dummy data can be seed by running**
   ```bash
   python -m app/migrations/seed.py
   ```
6. **Run the application:**
   ```bash
   python run.py [port]
   ```
   Replace `[port]` with your desired port number (e.g., `python run.py 4000`). If no port is provided, the default is 5000.

## Usage
- The backend exposes RESTful endpoints for user and CV management.
- Use tools like Postman or curl to interact with the API.
- The application can be run locally or deployed using Docker Compose.

## API Endpoints
- `/auth` - User authentication routes
- `/cv` - CV management routes
- `/actuator` - Health check and monitoring routes

Refer to the code in `app/routes/` for detailed endpoint documentation.

docs availble at `{URL}/apidocs`  TODO should I hard code the port

## Testing
- Tests are located in the `tests/` directory.
- To run tests:
  ```bash
  pytest tests/
  ```

## License
This project is licensed under the MIT License.

# Questions
which is better between relative and absolute imports
TODO add rate limiting
why does my path show app but link to the __init__.py file in my app