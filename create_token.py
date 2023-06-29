from settings import partner_id, admin_secret, userId
import requests
import json
import pandas as pd
from pandas import json_normalize

from KalturaClient import *
from KalturaClient.Plugins.Core import *
import hashlib

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

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

# Kaltura KMC Admin has created a role to further limit access.
# Get the list of existing roles created in the KMC in order to retrieve the proper ID
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

# Update filters and service endpoint based on your needs
filter1 = '&filter[descriptionLike]=Learning'
filter2 = '&filter[objectType]=KalturaUserRoleFilter'
service_url = 'https://www.kaltura.com/api_v3/service/userrole/action/list'

data = 'ks=' +  ks + '&format=1' + filter1 + filter2
response = requests.post(service_url, headers=headers, data=data)

roledict = json.loads(response.text)
role_df = json_normalize(roledict['objects'])
#print(role_df)

role_info = role_df.filter(['id','permissionNames'])
#print(role_info)

# create the app token
appToken = KalturaAppToken()
appToken.hashType = KalturaAppTokenHashType.SHA256
appToken.sessionPrivileges = "setrole:28239382,privacycontext:learningclues"
appToken.expiry = 1703980800 #App Token to expire at 12AM, December 31st, 2023
result = client.appToken.add(appToken);
id=result.id;
token=result.token;
print(token)