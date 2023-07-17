# kaltura_app_token

## References
Visit my blog for more details on this and similar tools: [edtechdev.com](https://edtechdev.com/)

[Kaltura API - Application Tokens](https://developer.kaltura.com/api-docs/VPaaS-API-Getting-Started/application-tokens.html)
[Kaltura API - Authentication and Security](https://developer.kaltura.com/api-docs/VPaaS-API-Getting-Started/Kaltura_API_Authentication_and_Security.html)
[How to Add Entitlements to Categories](https://knowledge.kaltura.com/help/how-to-add-entitlements-to-categories---kmc)

## Notes:
- It is important to review the differences between ADMIN and USER kaltura sessions when generating a "ks". USER sessions revolve around just being able to access media content in Kaltura that is owned by a specific user and is extremely restrictive for using in an API session. So, when using the app token, ADMIN session types may still be necessary to use if attempting to read or manipulate entries created by other users. That's one of the reasons this script exists -- to explore what options are available for adding security (of sorts) to a kaltura app token session. Higher Education and K12 need these options in order to fall into compliance for a variety of different standards.
- This repository only covers creation of an app token by a Kaltura adminstrator. I'll add more about usage of an app token to generate an app-token KS soon but until then, you'll want to refer to the documentation in my references above.

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

# Optional - Specific user to add to creation of app token. From Kaltura's docs: This can be useful when wanting to grant particular users with API access and ensure they can not mask their ID as someone else while carrying API actions.
apptoken_user = ""
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

### To Do
[ ] - Add a script or include CLI / Curl command for listing current app tokens
[ ] - App Token usage examples