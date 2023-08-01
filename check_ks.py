from KalturaClient import *
from KalturaClient.Plugins.Core import *
from settings import partner_id, admin_secret, userId, ks
from pprint import pprint
import datetime

config = KalturaConfiguration(partner_id)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)
admks = client.session.start(
            admin_secret,
            userId,
            KalturaSessionType.ADMIN,
            partner_id)
client.setKs(admks)

result = client.session.get(ks)
pprint(result.__dict__)

unix_expire = result.__dict__.get('expiry')
print("ks will expire: " + datetime.datetime.fromtimestamp(int(unix_expire))
      .strftime('%Y-%m-%d %H:%M:%S'))