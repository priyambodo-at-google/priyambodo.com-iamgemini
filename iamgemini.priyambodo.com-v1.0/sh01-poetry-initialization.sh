#/bin/bash
pip install --upgrade pip
pip install --upgrade poetry

#poetry new poetry-demo
poetry init

poetry config virtualenvs.in-project true
poetry install

poetry shell

poetry add streamlit
poetry add google-cloud-aiplatform
poetry add google-cloud-logging
#poetry remove streamlit

#poetry env info
#poetry show --tree
#poetry show --latest
#poetry exit
#poetry list env
#deactivate