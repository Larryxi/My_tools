# Author: Larry
# Time: 2016-05-28
# Version: 1.0
# TODO: compare with tcpdump
# Sniff interface to capture packets

#!/usr/bin/env python
#coding=utf-8

import optparse
import sys
import logging

from  scapy.all import *

class SniffPackets(object):
    """the class to sniff packets and show the infos
    run function:
        read_file: parse packets from the local file
        write_file: write the sniffed packets into particular file
    """
    def __init__(self, interface, capture_filter, count, read_file, write_file, verbose):
        """init class with options list"""
        self.interface = interface
        self.capture_filter = capture_filter
        self.count = count
        self.read_file = read_file
        self.write_file = write_file
        self.verbose = verbose

        # the packets list to store
        self.capture_packets = []

        # init the module logger
        self.__log_init()

    def __log_init(self):
        """the logger initialize"""
        # remove scapy'handlers
        self.logger = logging.getLogger('scapy')
        for h in self.logger.handlers:
            self.logger.removeHandler(h)
        self.logger.setLevel(logging.INFO)

        # add the customer StreamHandler to stdout
        custome_console_handler = logging.StreamHandler(sys.stdout)
        custome_console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(fmt='%(asctime)s %(message)s',
                                      datefmt='%H:%M:%S')
        custome_console_handler.setFormatter(formatter)

        self.logger.addHandler(custome_console_handler)

    def __read_pcap(self):
        """read pcap file and show or summary out"""
        try:
            # use rdpcap function of scapy and return a list
            packets = rdpcap(self.read_file)
        except BaseException as e:
            self.logger.error(e)
        else:
            for pkt in packets:
                if self.verbose:
                    self.logger.info(pkt.show())
                else:
                    self.logger.info(pkt.summary())

    def __write_pcap(self):
        """write packets list into file"""
        # check store or not by -w
        if self.write_file:
            try:
                # use wrpcap function of scapy
                wrpcap(self.write_file, self.capture_packets)
            except BaseException as e:
                self.logger.error(e)

    def __sniff_callback(self, pkt):
        """sniff callback function to show or summary packets info"""
        # append pkt to the packets list
        self.capture_packets.append(pkt)
        if self.verbose:
            self.logger.info(pkt.show())
        else:
            self.logger.info(pkt.summary())

    def __sniff_pcap(self):
        """the main sniff code"""
        try:
            # use sniff function of scapy and pass pkt to callback function
            sniff(iface=self.interface, filter=self.capture_filter,
                  prn=self.__sniff_callback, store=0, count=self.count)
        except BaseException as e:
            self.logger.error(e)
        finally:
            self.__write_pcap()

    def run(self):
        """read packets file or sniff packets"""
        # choose the function to call
        if  self.read_file:
            self.__read_pcap()
        else:
            self.__sniff_pcap()

if __name__ == '__main__':
    parser = optparse.OptionParser('usage: %prog [options]')

    parser.add_option('-i', '--iface',
                      dest='interface', default='eth0',
                      help='listen packets on the given interface')
    parser.add_option('-f', '--filter',
                      dest='capture_filter', default=None,
                      help='provide a BPF capture filter')
    parser.add_option('-c', '--count',
                      dest='count', type='int', default=0,
                      help='number of packets to capture')
    parser.add_option('-r', '--read',
                      dest='read_file', default=None,
                      help='parse packets from the file')
    parser.add_option('-w', '--write',
                      dest='write_file', default=None,
                      help='write the sniffed packets into pcap file')
    parser.add_option('-v', '--verbose',
                      dest='verbose', action='store_true', default=False,
                      help='print the verbose packets info')

    (options, args) = parser.parse_args()

    if len(args) > 0:
        parser.print_help()
        sys.exit(0)
    if options.read_file and options.write_file:
        parser.error('cannot write pcap file from the existing file')
        sys.exit(0)

    sniff_packets = SniffPackets(interface=options.interface, capture_filter=options.capture_filter, count=options.count,
                                 read_file=options.read_file, write_file=options.write_file,
                                 verbose=options.verbose)
    sniff_packets.run()
