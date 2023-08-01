from settings import partner_id, admin_secret, userId, role_id, \
    privacy_context, token_expiry, apptoken_user, widget_session, enable_entitlement, uri_restrict
import json

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

session_privs = ''

# create the app token
appToken = KalturaAppToken()

# Set the role ID provided in settings.py, if applicable
if role_id != '':
    session_privs = session_privs + 'setrole:' + str(role_id)

# Set the privacy context, if applicable
if privacy_context != '':
    session_privs = session_privs + ',privacycontext:' + privacy_context

# Set the widget session, if applicable
if widget_session != '':
    session_privs = session_privs + ',widget:1'

# Set the entitlement check, if applicable
if enable_entitlement != '':
    session_privs = session_privs + ',enableentitlement'

# Set the URI restriction, if applicable
if uri_restrict != '':
    session_privs = session_privs + ',urirestrict:' + uri_restrict

# Set an optional user to apply during app token creation
if apptoken_user != '':
    appToken.sessionUserId = apptoken_user

appToken.hashType = KalturaAppTokenHashType.SHA256
appToken.sessionPrivileges = session_privs
appToken.expiry = token_expiry

result = client.appToken.add(appToken)

# write the app token info to a JSON file for later retrieval
print('Writing app token info to JSON file...')
json_result = json.dumps(str(result.__dict__))
with open('token_' + result.id + '.json', 'w') as outfile:
    json.dump(json_result, outfile)

# print the KS used to create the app token
print('Kaltura Admin Session Used: ' + ks)
print('App Token Session privileges applied: ' + result.sessionPrivileges)

# print the app token, app token ID
print('App Token: ' + result.token)
print('App Token ID: ' + result.id)