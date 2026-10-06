# Expense Management System

This expense management system consists of a Streamlit frontend application and a FastAPI backend server.


## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```

2. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```

3. **Create the database:**
   Make sure MySQL is running, then run:
   ```commandline
    mysql -u root -p < schema.sql
   ```
   This creates the `expense_manager` database, the `expenses` table, and one sample row used by the tests.

4. **Configure the database:**
   ```commandline
   cp .env.example .env

5. **Run the FastAPI server:**:   
   ```commandline
    cd backend && uvicorn server.server:app --reload
   ```
6. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```