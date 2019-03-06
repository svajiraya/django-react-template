# Boilerplate project

**Credits**: [@stevenphaedonos](https://github.com/stevenphaedonos) 

## Running the application

### For development
1. Install [Docker](https://store.docker.com/search?type=edition&offering=community) and [docker-compose](https://docs.docker.com/compose/install/#install-compose)
2. Create a backend config file: `backend/.env`
    ```
    SECRET_KEY = 'important_secret'

    NAME = 'app'
    USERNAME = 'root'
    PASSWORD = 'root'
    HOST = 'db'

    ALLOWED_HOSTS = "localhost"
    CORS_WHITELIST = "localhost:3000"
    ```
3. Create a frontend config file: `frontend/.env.development`
    ```
    REACT_APP_BACKEND_URL = "http://localhost:8000/"
    ```
4. From your terminal, run `docker-compose build` followed by `docker-compose up` in the project's root directory
5. If this is the first time running, you must perform the following:
    - Attach to the backend container with:
      `docker-compose exec backend bash`
    - Perform database migrations:
      1) `python manage.py makemigrations`
      2) `python manage.py migrate`
