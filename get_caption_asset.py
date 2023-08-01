############################################### Kaltura Libs not working with this endpoint
#from KalturaClient import *
#from KalturaClient.Plugins.Core import *
############################################### Kaltura Libs not working with this endpoint

import json, requests

from settings import partner_id, ks

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

caption_asset_id = ''
data = 'ks=' +  ks + '&format=1&id=' + caption_asset_id
response = requests.post('https://www.kaltura.com/api_v3/service/caption_captionasset/action/getUrl', headers=headers, data=data)
resp_dict = json.loads(response.text)
print(resp_dict)

############################################### Kaltura Libs not working with this endpoint
#config = KalturaConfiguration(partner_id)
#config.serviceUrl = "https://www.kaltura.com/"
#client = KalturaClient(config)
#client.setKs(ks)
#storage_id = 0
#result = client.caption.captionAsset.getUrl(caption_asset_id, storage_id)
#x = result.getObjects()
#y = x[0].toParams().toJson()
#print(y)
############################################### Kaltura Libs not working with this endpoint


