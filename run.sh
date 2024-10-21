#!/bin/bash

cd backend || { echo "Backend folder not found"; exit 1; }

# Activate the virtual environment
source pyserverenv/bin/activate

# Run the server.py script
python server.py

# Optionally deactivate the virtual environment after running
deactivate
