#!/usr/bin/env python
#coding=utf-8

import optparse
import sys
import logging

from scapy.all import *

class Sniff(object):
    def __init__(self, port):
        logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
        self.port = port

    def run(self):
        try:
            sniff(prn=self.udp_monitor_callback, filter='udp', store=0)
        except KeyboardInterrupt as e:
            print '[+] Bye !'
            sys.exit(0)

    def udp_monitor_callback(self, pkt):
        if pkt.getlayer(Raw):
            raw_load = pkt.getlayer(Raw).load
            if pkt[UDP].dport == self.port and raw_load[:4] == '\x00\x03\x00\x01':
                print '[+] The server %s is available' % (pkt[IP].src)
                sys.exit(0)

if __name__ == '__main__':
    parser = optparse.OptionParser('usage: %prog [options]')
    parser.add_option('-p', '--port', type=int, default=2333, help='The port from server')

    (options, args) = parser.parse_args()
    if len(args) > 0:
        parser.print_help()
        sys.exit(0)

    s = Sniff(port=options.port)

    s.run()
