# kaltura_app_token

Clone the Repo:
`git clone <this repo>`

Create a settings.py with the following:
```
partner_id=<your partner id>
admin_secret="<your admin secret>"
userId = "<KMC Admin username>"
```

Create a Python virtual environment (Assumes Linux / MacOS):
`python3 -m venv kaltura_env`
`source ./kaltura_env/bin/activate`

Install Dependencies / Modules:
`pip install -r requirements.txt`