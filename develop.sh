#! /bin/sh
yarn --cwd ./client-studia dev & cd app 
poetry install
poetry run python ./app/main.py