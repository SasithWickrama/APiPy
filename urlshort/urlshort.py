import traceback
import json
from log import getLogger
import requests

logger = getLogger('urlshort', 'logs/urlshort')
logger.info("hiii")
headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json'}


class Shorturl:
    # @Authentication.token_required
    def short_url(self):
        data = self
        logger.info("Request : %s" % data)
        try:

            createresponse = requests.post('https://cs.slt.lk/feedback-url/create-short-url', data=json.dumps(data),
                                           headers=headers)

            logger.info("Response Code: %s" % createresponse.status_code)
            resmsg = createresponse.json()
            responsedata = {"data": resmsg['data']}
            logger.info("Response : %s" % resmsg)

            return resmsg
        except Exception as e:
            print("Exception : %s" % traceback.format_exc())
            logger.info("Exception : %s" % traceback.format_exc())
