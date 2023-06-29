# kaltura_app_token

## References:
[Kaltura API - Application Tokens](https://developer.kaltura.com/api-docs/VPaaS-API-Getting-Started/application-tokens.html)

[How to Add Entitlements to Categories](https://knowledge.kaltura.com/help/how-to-add-entitlements-to-categories---kmc)

### Update the following in the script:


Clone this Repo to your development machine with Python 3.10+ installed:
```
git clone git@github.com:eharvey71/kaltura_app_token.git
```

Create a settings.py in the same path as create_token.py
```python
partner_id=<your partner id>
admin_secret="<your admin secret>"
userId = "<KMC Admin username>"
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