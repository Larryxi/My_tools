#!/usr/bin/env python

########################
#Name: UDP Scan
#Author: Larry
#Time: 2015-12-12
########################

import logging
import time

from scapy.all import *

class UDPScan(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = int(port)
        scapy_logger = logging.getLogger("scapy.runtime")
        scapy_logger.setLevel(logging.WARNING)
        self.portscan_logger = logging.getLogger("portscan")

    def run(self):
        ans = sr1(IP(dst=self.ip)/UDP(dport=self.port),timeout=5,verbose=0)
        time.sleep(1)
        if ans == None:
            self.portscan_logger.info("port %s on UDP is open" % (self.port))
