# Django+FenixEdu Authentication Demo

## Getting Started

1) Make sure you've registered an External Application in your Fenix instance. Collect the Client ID and Client Secret.

2) Update FenixAuthDemo/settings.py and set the FENIXEDU_CLIENT_ID, FENIXEDU_CLIENT_SECRET and FENIXEDU_REDIRECT_URI to match the values obtained in the previous step. 

3) Install dependencies and perform the initial migration: 
```bash
pip3 install -r requirements.txt
python3 manage.py migrate
```

4) Run the server in development mode: 
```bash
python3 manage.py runserver 0.0.0.0:8000
```

5) Visit localhost:8000 in your browser.
