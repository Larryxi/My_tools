#!/usr/bin/env python

#####################
#Name: HTTP Scan
#Author: Larry
#Time: 2015-12-12
#####################

import logging

import requests

class HTTPScan(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.url = "http://%s:%s" % (ip,port)
        self.portscan_logger = logging.getLogger("portscan")

    def run(self):
        try:
            r = requests.get(self.url,timeout=0.5)
            if r.headers != {} and r.status_code == 200:
                self.portscan_logger.info("Port %s HTTP service" % (self.port))
        except Exception as e:
            self.portscan_logger.debug(str(e))
