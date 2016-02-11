import logging
import json

from rest_framework.parsers import JSONParser


logger = logging.getLogger(__name__)

"""
This utility is used for fetching data from request
"""
def get_data_from_request(request):

    content = {}

    # POST request from mobile client
    try:
        # fetch data from request object
        logger.debug("Trying to fetch data from request using JSONParser method")
        content = JSONParser().parse(request)

    except:

        # DRF panel
        try:
            # fetch data from _content parameter in drf request object
            logger.debug("Trying to fetch data from request from request.POST['_content']")
            content = json.loads(request.POST["_content"])

        except:
            # POST request through web-site ajax request
            logger.debug("Trying to fetch from request.POST")
            content = request.POST

    logger.debug("content in get_data_from_request: %s" %content)
    return content