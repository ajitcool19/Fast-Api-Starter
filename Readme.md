## Fast-Api starter

This is a starter project for Fast-Api. It includes the following features:

### Features
1: Middleware Support -> DB Session, JWT Authentication, Request Logging

2: SqlAlchemy ORM

3: Pydantic Models

4: Docker Support

5: Sentry for Reporting

### How to run
1: Clone the repository
2: Suggestion to create a virtual environment by running 
2a:`python3 -m venv venv`
2b: Activate the virtual environment by running `source venv/bin/activate`
3: Install the requirements by running `pip install -r startup/requirements.txt`
4: Run the server by running `python3 startup/start_server.py dev` or `python3 startup/start_server.py prod`
