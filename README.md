# Integrated Symbiotics

### Installation

Clone the repo

    git clone https://github.com/JKring/integrated-symbiotics.git

Go into the directory, install requirements and start the server

    cd integrated-symbiotics
    pip install -r requirements.txt
    foreman start

If gunicorn can't connect:
		sudo lsof -i :5000
		kill -9 PID

Navigate to [localhost:5000](http://localhost:5000) in your browser.

### Deploy to Heroku

Make some changes. Add and commit them:

    git add .
    git commit -m "i made some changes"

Push them to heroku

    git push heroku master
