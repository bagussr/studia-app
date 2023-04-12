#! /bin/sh
yarn --cwd ./client-studia dev & cd app 
poetry run python ./app/main.py