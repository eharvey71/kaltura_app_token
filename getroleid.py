from settings import partner_id, admin_secret, userId, role_name
import requests
import json
import pandas as pd
from pandas import json_normalize

from KalturaClient import *
from KalturaClient.Plugins.Core import *

# Get a ks
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

if role_name != "":

    # Perhaps, the Kaltura KMC Admin has created a role to further limit access.
    # Get the list of existing roles created in the KMC in order to retrieve the proper ID
    # Update filters and service endpoint based on your needs
    filter1 = '&filter[descriptionLike]=' + role_name
    filter2 = '&filter[objectType]=KalturaUserRoleFilter'
    service_url = 'https://www.kaltura.com/api_v3/service/userrole/action/list'

    data = 'ks=' +  ks + '&format=1' + filter1 + filter2
    response = requests.post(service_url, headers=headers, data=data)

    roledict = json.loads(response.text)
    role_df = json_normalize(roledict['objects'])
    print(role_df)

    role_info = role_df.filter(['id','permissionNames'])
    print(role_info)

else:
    print("No role name provided.  Please update settings.py with a role name.")