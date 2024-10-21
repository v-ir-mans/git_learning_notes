cd backend || (echo Backend folder not found & exit /B)

:: Activate the virtual environment
call pyserverenv\Scripts\activate.bat

:: Run the server.py script
python server.py

:: Optionally deactivate the virtual environment after running
deactivate