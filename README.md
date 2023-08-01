# kaltura_app_token

## References
Visit my blog for more details on this and similar tools: [edutechdev.com](https://edutechdev.com/)

[Kaltura API - Application Tokens](https://developer.kaltura.com/api-docs/VPaaS-API-Getting-Started/application-tokens.html)

[Kaltura API - Authentication and Security](https://developer.kaltura.com/api-docs/VPaaS-API-Getting-Started/Kaltura_API_Authentication_and_Security.html)

[How to Add Entitlements to Categories](https://knowledge.kaltura.com/help/how-to-add-entitlements-to-categories---kmc)

### Notes:
- It is important to review the differences between ADMIN and USER kaltura sessions when generating a "ks". USER sessions revolve around just being able to access media content in Kaltura that is owned by a specific user and is extremely restrictive for using in an API session. So, when using the app token, ADMIN session types may still be necessary to use if attempting to read or manipulate entries created by other users. That's one of the reasons this script exists -- to explore what options are available for adding security (of sorts) to a kaltura app token session. Higher Education and K12 need these options in order to fall into compliance for a variety of different standards.

- This repository only covers creation of an app token by a Kaltura adminstrator. I'll add more about usage of an app token to generate an app-token KS soon but until then, you'll want to refer to the documentation in my references above.

### Steps for generating a Kaltura app token


Clone this Repo to your development machine with Python 3.10+ installed:
```
git clone git@github.com:eharvey71/kaltura_app_token.git
```

Create a settings.py in the same path as create_token.py and add the following:
```python
# Kaltura Partner ID (PID). This is the Kaltura customer ID, tied to their Kaltura environment.
#partner_id=123456
partner_id=

# ================================================= App Token Creation
# Kaltura Admin Secret - Do not share your admin secret with anyone or commit to a GitHub repo.
# This is only needed to create an app token, where an admin session is required.
admin_secret=''

# Optional - The user ID of the KMC Admin who will create the app token.
userId = ''

# Optional - If a role is being applied to the app token creation. You can run 'python getroleid.py' to get the integer needed for app token creation.
role_id = ''

# Optional - Set Widget Session. privilege to the KS to tell the server that this KS was generated for player use only, 
# which will tell the server to make a distinction between a regular USER session and a “PLAYER” session.
# Set to 1 to enable. Can be blank unless you're applying a widget session to the app token creation.
widget_session = ''

# Optional - Forces entitlement checks.
# Note: there is a setting on account level (configured in the admin console) that determines the default entitlement enforcement
# Set to 1 to enable. Can be blank unless you're applying an entitlement check to the app token creation.
enable_entitlement = ''

# Optional - Restrict API calls to a specific API endpoint. 
# Example: /api_v3/service/media/*
# Allows access to only the caption asset enpoint. 
# Can be blank unless you're applying a URI restriction to the app token creation.
uri_restrict = ''

# Optional - Can be blank unless you're applying a privacy context to the app token creation
# Comma separated list of privacy contexts created by a KMC admin
privacy_context = ''

# Optional - Unix timestamp for the app token to expire
token_expiry = '1703980800' #App Token to expire at 12AM, December 31st, 2023

# Optional - Specific user to add to creation of app token. 
# From Kaltura's docs: This can be useful when wanting to grant particular users with API access and 
# ensure they can not mask their ID as someone else while carrying API actions.
apptoken_user = ''
# =================================================

# ================================================= Get role id from a role name
# Optional - use only if you are running getroleid.py. Can be blank unless you're applying a custom role to the app token creation
# The following can be a partial name if searching for multiple roles
role_name = ''
# =================================================

# ================================================= Configuration for using an App Token
# Existing App Token ID - Use this section for the following tools:
# - gen_apptoken_session.py
appTokenID = ''
atks_expiry = 86400
appToken=''
atks_userId = ''
atks_session_type = 0 # 0 = USER, 2 = ADMIN
atks_session_privs = '' # Comma separated list of privileges
# =================================================

# =================================================
# Storing a ks string here. All scripts will check here first and override with this value.
# If this is blank -- Depending on the tool, the script will look for a $KALTURA_SESSION environment variable or generate a new session.
ks=''
# =================================================
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

[ ] - More reuse through a common, separate function definitions file