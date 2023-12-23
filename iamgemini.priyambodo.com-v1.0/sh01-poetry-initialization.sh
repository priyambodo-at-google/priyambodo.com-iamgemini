#/bin/bash
pip install --upgrade pip
pip install --upgrade poetry

#Initialize the Poetry environment 
poetry new myapp #(optional)
poetry init

#Activate the environment in your directory
poetry config virtualenvs.in-project true
poetry install
poetry shell

#Add your Python Dependency Package
poetry add streamlit
poetry add google-cloud-aiplatform
poetry add google-cloud-logging

#Operational that you might need (optional)
poetry remove streamlit #removing package
poetry env info
poetry show --tree
poetry show --latest
poetry exit
poetry list env
deactivate #deactivate the environment