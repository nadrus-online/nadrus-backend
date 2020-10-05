## Nadrus Oneline

This repository contains code for the nadrus.online platform.

### Running Locally

From the project's main directory, you can run using `gunicorn` or using `flask` directly:

```bash
# run two workers using the gunicorn webserver
gunicorn -w 2 "app:create_app('production')"
```

or

```bash
# simple run using the flask server
env FLASK_APP="app:create_app('dev')" python -m flask run
```
