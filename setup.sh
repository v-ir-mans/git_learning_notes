#!/bin/bash

# Navigate to the backend folder
cd backend || { echo "Backend folder not found"; exit 1; }

# Create the virtual environment
python3 -m venv pyserverenv

# Activate the virtual environment
source pyserverenv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the server.py script
python server.py

# Optionally deactivate the virtual environment after running
deactivate
