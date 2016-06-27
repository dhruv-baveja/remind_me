import logging
import json
import arrow
from dateutil.tz.tz import tzutc

from rest_framework.parsers import JSONParser


logger = logging.getLogger(__name__)


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


def convert_date_time_to_iso_format(date):
    """
    :param date: any valid datetime string
    :return: ISO8601 formatted datetime string
    """
    arrow_dt = arrow.get(date)
    if isinstance(arrow_dt.tzinfo, tzutc):
        return arrow_dt.format('YYYY-MM-DDTHH:mm:ss.SSS') + 'Z'
    return arrow_dt.format('YYYY-MM-DDTHH:mm:ss.SSSZZ')
