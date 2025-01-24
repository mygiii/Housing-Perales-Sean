# Getting Started
1. Clone the Repository

git clone <repository_url>
cd Housing-Perales-Sean

2. Configure the Environment

    Rename .env.example to .env:

mv .env.example .env

## here, i sugest you just put the same password as i did in your postgres database honestly
Update a few files : 
.env : update your_password
    DATABASE_USER=postgres
    DATABASE_PASSWORD=dinodu93
    DATABASE_NAME=housing
    DATABASE_HOST=db
    DATABASE_PORT=5432
Docker-compose.yml :
    in the two environments, there is a sections where put in a password, in DATABASE_PASSWORD & in POSTGRES__PASSWORD
alembic.ini:
    
    sqlalchemy.url = postgresql+asyncpg://postgres:dinodu93@localhost/housing ----- here after "postgres:" put in your password
database.py :
    
    DATABASE_URL = "postgresql+asyncpg://postgres:dinodu93@db:5432/housing" ---- here as well

3. Build and Run the Application

Run the following command to build and start the application using Docker Compose:

docker-compose up --build

This command will:

    Build the Docker containers for the application and the database.
    Apply database migrations using Alembic.
    Start the FastAPI server at http://localhost:8000.

Usage
Endpoints

    Add a new house (POST)
    Add a new house entry to the database.

    Request:

curl -X POST http://localhost:8000/houses \
-H "Content-Type: application/json" \
-d '{
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41,
    "total_rooms": 880,
    "total_bedrooms": 129,
    "population": 322,
    "households": 126,
    "median_income": 8.3252,
    "median_house_value": 452600,
    "ocean_proximity": "NEAR BAY"
}'

Response:

{
    "id": 1,
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41,
    "total_rooms": 880,
    "total_bedrooms": 129,
    "population": 322,
    "households": 126,
    "median_income": 8.3252,
    "median_house_value": 452600,
    "ocean_proximity": "NEAR BAY"
}

Retrieve all houses (GET)
Fetch all house entries from the database.

Request:

curl -X GET http://localhost:8000/houses

Response:

[
    {
        "id": 1,
        "longitude": -122.23,
        "latitude": 37.88,
        "housing_median_age": 41,
        "total_rooms": 880,
        "total_bedrooms": 129,
        "population": 322,
        "households": 126,
        "median_income": 8.3252,
        "median_house_value": 452600,
        "ocean_proximity": "NEAR BAY"
    }
]


Troubleshooting -- 
1. Password Authentication Failed

If you encounter a password authentication error:

    Stop the containers:

docker-compose down

Access the database container:

docker exec -it housing-perales-sean_db_1 bash
su - postgres

Update the PostgreSQL password:

ALTER USER postgres PASSWORD 'your_password';

Exit the container and restart the application.

