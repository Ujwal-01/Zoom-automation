#!/bin/bash

echo "Starting Zoom Automation"

# Check if Python exists
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Install Python first."
    exit 1
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  echo "Creating Python virtual environment"
  python3 -m venv venv
fi

# Activate venv
echo "Activating virtual environment"
. venv/bin/activate

# Install dependencies
if [ -f requirements.txt ]; then
  echo "Installing required packages"
  pip install --upgrade pip
  pip install -r requirements.txt
else
  echo "requirements.txt not found. Skipping dependency install."
fi

# Run Python script
echo "Running automation script"
python3 src/automation.py

echo "Automation Finished!"

