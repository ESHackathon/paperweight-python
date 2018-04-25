# Paperweight Python
## Broaden your horizons

Learn more about a scientific field. Paperweight allows you to simply paste in an RIS file of publications (exportable from Scopus), and find keywords and topic modelling analysis to help you discover more about the field.

## About the app

The app is in two parts, a Rails 5.2 interface with postgres database for the main app, and a Flask app with Python 3 and rake-ntlk for natural language processing

## 1. Rails App (Interface)

Available at https://github.com/ESHackathon/paperweight.git

```
bundle install
yarn install
rails db:create db:migrate
rails s
```

## 2. Flask App (Data Science)

Find the repo here...
https://github.com/ESHackathon/paperweight-python.git

Parsing the keywords and data science stuff is done in Python, run the flask app (from https://github.com/ESHackathon/paperweight-python.git) and place the local address in the `flask.rb` file

`FLASK_APP_ADDRESS="http://127.0.0.1:5000/"`

Fire up the flask app with...

```
export FLASK_APP=server.py
python server.py
```
# Paperweight Python Keyword Extractor

Uses rake-nltk to extract keywords from a RIS file. RIS files are posted to the root path via a json api, and return the processed keywords.

## Run

```
export FLASK_APP=server.py
flask run
```
