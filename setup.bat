@echo off

:: Navigate to the backend folder
cd backend || (echo Backend folder not found & exit /B)

:: Create the virtual environment
python -m venv pyserverenv

:: Activate the virtual environment
call pyserverenv\Scripts\activate.bat

:: Install requirements
pip install -r requirements.txt

:: Run the server.py script
python server.py

:: Optionally deactivate the virtual environment after running
deactivate
