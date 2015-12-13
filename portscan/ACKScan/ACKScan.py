#!/usr/bin/python

#########################
#Name: ACK Scan
#Author: Larry
#Time: 2015-12-12
#########################

import logging

from scapy.all import *

class ACKScan(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = int(port)
        scapy_logger = logging.getLogger("scapy.runtime")
        scapy_logger.setLevel(logging.ERROR)
        self.portscan_logger = logging.getLogger("portscan")

    def run(self):
        ACK_response = sr1(IP(dst=self.ip)/TCP(dport=self.port,flags='A'),timeout=1,verbose=0)
        SYN_response = sr1(IP(dst=self.ip)/TCP(dport=self.port,flags='S'),timeout=1,verbose=0)
        if (ACK_response == None) and (SYN_response == None):
            self.portscan_logger.debug("Port %s is either unstatefully filtered or host is down" % (self.port))
        elif ((ACK_response == None) or (SYN_response == None)) and not((ACK_response ==None) and (SYN_response == None)):
            self.portscan_logger.debug("Port %s is filtered by Stateful firewall" % (self.port))
        elif int(SYN_response[TCP].flags) == 18:
            self.portscan_logger.info("Port %s is unfiltered and open" % (self.port))
        elif int(SYN_response[TCP].flags) == 20:
            self.portscan_logger.debug("Port %s is unfiltered and closed" % (self.port))
        else:
            self.portscan_logger.debug("Unable to determine if the port %s is filtered" % (self.port))
