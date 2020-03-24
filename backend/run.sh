#! /usr/bin/env bash

source venv/bin/activate

export FLASK_APP="app"
export FLASK_ENV="development"

flask run --port 5000
