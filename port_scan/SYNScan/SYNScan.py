#!/usr/bin/env python

#######################
#Name: SYN Scan
#Author: Larry
#Time: 2015-12-12
#######################

import logging

from scapy.all import *

class SYNScan(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = int(port)
        scapy_logger = logging.getLogger("scapy.runtime")
        scapy_logger.setLevel(logging.WARNING)
        self.portscan_logger = logging.getLogger("portscan")

    def run(self):
        ans = sr1(IP(dst=self.ip)/TCP(dport=self.port),timeout=1,verbose=0)
        if ans == None:
            pass
        elif int(ans[TCP].flags) == 18:
            self.portscan_logger.info("Port %s on TCP is open" % (self.port))
