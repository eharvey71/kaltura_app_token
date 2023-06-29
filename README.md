# kaltura_app_token

## References
[Kaltura API - Application Tokens](https://developer.kaltura.com/api-docs/VPaaS-API-Getting-Started/application-tokens.html)

[How to Add Entitlements to Categories](https://knowledge.kaltura.com/help/how-to-add-entitlements-to-categories---kmc)

### Steps for generating a Kaltura app token


Clone this Repo to your development machine with Python 3.10+ installed:
```
git clone git@github.com:eharvey71/kaltura_app_token.git
```

Create a settings.py in the same path as create_token.py and add the following:
```python
# Kaltura PID and Admin Secret
partner_id=
admin_secret=""

# Optional - The user ID of the KMC Admin who will create the app token
userId = ""

# Can be blank unless you're applying a custom role to the app token creation
# The following can be a partial name if searching for multiple roles
role_name = ""

# Optional - If a role is being applied to the app token creation. You can run 'python getroleid.py' to get the integer needed for app token creation.
role_id =

# Can be blank unless you're applying a privacy context to the app token creation
# Comma separated list of privacy contexts created by a KMC admin
privacy_context = "lceducation,lcarcheology"

# Unix timestamp for the app token to expire
token_expiry = 1703980800 #App Token to expire at 12AM, December 31st, 2023
```

Create a Python virtual environment (Assumes Linux / MacOS):
```
python3 -m venv kaltura_env
source ./kaltura_env/bin/activate
```

Install Dependencies / Modules:
```
pip install -r requirements.txt
```

Create the app token:
```
python create_token.py
```