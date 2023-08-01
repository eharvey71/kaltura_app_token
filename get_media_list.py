# from KalturaClient import *
# from KalturaClient.Plugins.Core import *
# from settings import partner_id, admin_secret, userId, ks

# config = KalturaConfiguration(partner_id)
# config.serviceUrl = "https://www.kaltura.com/"
# client = KalturaClient(config)
# if ks == "":
#     ks = client.session.start(
#                 admin_secret,
#                 userId,
#                 KalturaSessionType.ADMIN,
#                 partner_id)
# client.setKs(ks)

# filter = KalturaMediaEntryFilter()
# filter.orderBy = KalturaMediaEntryOrderBy.CREATED_AT_ASC
# filter.freeText = "learning"
# pager = KalturaFilterPager()

#result = client.media.list(filter, pager)

import json, requests
from pprint import pprint
from settings import partner_id, ks

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = 'ks=' +  ks + '&format=1'
response = requests.post('https://www.kaltura.com/api_v3/service/media/action/list', headers=headers, data=data)
resp_dict = json.loads(response.text)
pprint(resp_dict)

