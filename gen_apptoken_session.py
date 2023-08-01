from KalturaClient import *
from KalturaClient.Plugins.Core import *
import hashlib

from settings import partner_id, atks_expiry, appTokenID, appToken, atks_session_type, atks_session_privs, atks_userId

config = KalturaConfiguration(partner_id)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)

# Create an unpriviliged KS for use in generating a new app token session
expiry = 86400
widgetId = "_"+str(partner_id)
widget_result = client.session.startWidgetSession(widgetId, expiry)
client.setKs(widget_result.ks)

print("widget KS: " + widget_result.ks)

hashString = hashlib.sha256(widget_result.ks.encode('ascii') + appToken.encode('ascii')).hexdigest()

# Overriding default session expiration of 1 day with 1 month:
#atks_expiry = 43800

result = client.appToken.startSession(appTokenID, hashString, '', atks_session_type, atks_expiry, atks_session_privs)
ksession = result.ks
print("\nhashed token: " + hashString + "\n\nKaltura (App Token) Session: " + ksession)