#!/usr/bin/env python
#encode=utf-8

from socket import *
import optparse
import os
import sys

class TFTPFileEnum(object):
    def __init__(self, server, port, filename):
        self.addr = (server, port)
        self.filename = filename
        self.udp_client = socket(AF_INET, SOCK_DGRAM)

    def enum(self):
        with open(self.filename) as f:
            for n in f:
                enum_file = n[:-1]
                rrq = '\x00\x01%s\x00octet\x00' % (enum_file)
                self.udp_client.sendto(rrq, self.addr)
                data, addr = self.udp_client.recvfrom(1024)
                if data[:2] == '\x00\x03':
                    print '[+] The file \'%s\' is on the server' % (enum_file)
        self.udp_client.close()
        print '[+] Enumserate Done!'

if __name__ == '__main__':
    parser = optparse.OptionParser('usage: %prog [options] server')
    parser.add_option('-p', '--port', type='int', default=69, help='The port of TFTP server to enumerate files on it')
    parser.add_option('-f', '--filename', default='larry', help='The file which contains the filenames to enumerate')

    (options, args) = parser.parse_args()
    if len(args) < 1 or not os.path.exists(options.filename):
        parser.print_help()
        sys.exit(0)

    e = TFTPFileEnum(server=args[0], port=options.port, filename=options.filename)
    e.enum()
