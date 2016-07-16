# -*- coding:utf-8 -*-
import requests
from loggingd import *
'''
    This function do a request to the URL with the required parameters.
    Both "POST" and "GET"  method supported, "POST" is default
    The response will be return with json format
'''


def getresponse(url, requesparameters, method="POST"):
    try:
        if method == "POST":
            r = requests.post(url, data=requesparameters)
            logger.info("Do POST request to %s with parameter(s) %s" % (url, requesparameters))
        if method == "GET":
            r = requests.get(url, params=requesparameters)
            logger.info("Do GET request to %s with parameter(s) %s" % (url, requesparameters))
        if r.status_code == 200:
            return r.json()
        else:
            logger.error("Status_code is %s, URL: %s, Parameters: %s" % (r.status_code, url, requesparameters))
            return None
    except Exception, e:
        logger.error("Error caught: %s, URL: %s" % (e, url))

