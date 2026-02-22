#!/bin/bash
python -v

#Clone the repo

git clone https://github.com/vipigk/fask-portfolio-main.git
cd Flask-portfolio-main

#Create & activate virtual environment

python -m venv venv
source venv/bin/activate

#Install dependencies
pip install -r requirements.txt

#Run the Flask app
gunicorn -w 4 -b 0.0.0.0:8000 app:app