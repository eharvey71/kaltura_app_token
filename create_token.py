from settings import partner_id, admin_secret, userId, role_id, privacy_context, token_expiry
import requests
import json
import pandas as pd
from pandas import json_normalize

from KalturaClient import *
from KalturaClient.Plugins.Core import *

# Administrator generates a session in order to create the app token
config = KalturaConfiguration(partner_id)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)
ks = client.session.start(
            admin_secret,
            userId,
            KalturaSessionType.ADMIN,
            partner_id)
client.setKs(ks)

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

session_privs = ""

# Set the role ID provided in settings.py, if applicable
if role_id != "":
    session_privs = session_privs + "setrole:" + str(role_id)

# Set the privacy context, if applicable
if privacy_context != "":
    session_privs = session_privs + ",privacycontext:" + privacy_context

# create the app token
appToken = KalturaAppToken()
appToken.hashType = KalturaAppTokenHashType.SHA256
appToken.sessionPrivileges = session_privs
appToken.expiry = token_expiry
result = client.appToken.add(appToken);
id=result.id;
token=result.token;
print(token)
