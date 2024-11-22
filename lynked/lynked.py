import random
import traceback
import json
from log import getLogger
import requests

logger = getLogger('lynked', 'logs/lynked')
headers = {
    'Authorization': 'Bearer 897|t9Bwa7Tb8c0Q47K4VHJKeeLKcSnjovk7JKoz630l',
    'Content-type': 'application/json',
    'Accept': 'application/json'}

def specific_string(length):
    sample_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  # define the specific string
    # define the condition for random string
    return ''.join((random.choice(sample_string)) for x in range(length))


class Lynked:
    # @Authentication.token_required
    def create(self):
        ref = specific_string(15)
        data = self
        logger.info("Request : %s" % data)
        try:

            createresponse = requests.post('https://lynkeddemo.cyber.lk/api/v1/external/slt-crm/customer/create', data=json.dumps(data),
                                           headers=headers)

            resmsg = json.loads(createresponse.text)
            if createresponse.status_code == 200:
                logger.info("Response : %s" % ref + " - " + str(resmsg))
                return resmsg
            else:
                logger.info("Response : %s" % ref + " - " + str(resmsg))
                return resmsg

            return resmsg
        except Exception as e:
            resmsg= {"status": "error","errors": e}
            logger.info("Exception : %s" % ref + " - " + str(resmsg))
            return resmsg


