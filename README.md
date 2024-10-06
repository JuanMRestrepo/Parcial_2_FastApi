# Parcial_2_FastApi

This project is the second partial of fastapi

## Project Description

The objective of this project is to demonstrate the knowledge to date from the creation of the fastapi, the migration of the database, the AAA and Http class tests and the clean code.

## Technologies Used

- Python
- FastAPI
- Postgres
- Alembic
- Sqlalchemy
- Pytest
- Httpx
- Tox
- Pylint
- Autopep8

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/JuanMRestrepo/Parcial_2_FastApi.git
   cd Parcial_2_FastApi/auth_service
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Start the server:
   ```
   uvicorn app.main:app --reload
   ```

5. Test Status:
   ```
   tox
   ```

The API will be available at `http://localhost:8084`.

## API Endpoints

- POST `/api/pagos:/`: Create a payment
- GET `/api/pagos`: Get all payments
- POST `/api/arrendatarios`: Create a tenant
- GET `/api/arrendatarios`: Get all tenants

For detailed API documentation, visit `http://localhost:8084/docs` after starting the server.

## Project Structure

- `app/`: Main application package
  - `config/`: Configuration files
   - `config.py`
  - `models/`: Defines data models for database tables
   - `pago_model.py`
   - `arrendatario_model.py`
  - `repositories/`: Implements data access logic
   - `pago_repository.py`
   - `arrendatario_repository.py`
  - `routes/`: Defines the API endpoints
   - `pago_routes.py`
   - `arrendatario_routes.py`
  - `schemas/`: Defines the input and output schemas for the API
   - `pago_schema.py`
   - `arrendatario_schema.py`
  - `services/`: Contains the business logic
   - `pago_service.py`
   - `arrendatario_service.py` 
  - `main-py`: Application entry point

- `test/`: Contains the unit tests.
  - `test_pago_service.py`
  - `test_arrendatario_service.py`

## Contribution
Please make corrections in this section

Thank you for your interest in this project!!!
