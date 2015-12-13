#!/usr/bin/env python

#####################
#Name: port scan main
#Author: Larry
#Time:2015-12-12
#####################

import logging
import optparse
import sys

class PortScan(object):
    def __init__(self,module,ip,port,verbose):
        self.module = module + "Scan"
        self.ip = ip
        self.port = port
        self.verbose = verbose
        self._config_log()
        self._get_port()
        self._get_module()

    def _config_log(self):
        '''
        configure the log output to console by using logging module
        in verbose, output the debug message
        otherwise, output the info message
        '''
        self.portscan_logger = logging.getLogger("portscan")
        self.portscan_logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter("[+] %(levelname)s : %(message)s")
        console_handler.setFormatter(formatter) 
        if self.verbose:
            console_handler.setLevel(logging.DEBUG)
        else:
            console_handler.setLevel(logging.INFO)
        self.portscan_logger.addHandler(console_handler)

    def _get_port(self):
        '''
        get ip scope,for example:
        -p 80    -> 80
        -p 80,81 -> 80 81
        -p 80-81 -> 80 81
        '''
        if ',' in self.port:
            self.portlist = self.port.split(',')
        elif '-' in self.port:
            self.portlist = [str(x) for x in xrange(int(self.port.split('-')[0]),int(self.port.split('-')[1])+1)]
        else:
            self.portlist = []
            self.portlist.append(self.port)

    def _get_module(self):
        '''
        get scan module dynamically
        UDPScan SYNScan ACKScan HTTPScan
        '''
        if self.module not in ['UDPScan','SYNScan','ACKScan','HTTPScan']:
            self.portscan_logger.warning("The mode is unlawful")
            sys.exit(0)
        self.scan_module = __import__("%s.%s" % (self.module,self.module))
        self.scan_sub_module = getattr(self.scan_module,self.module)
        self.scan_class = getattr(self.scan_sub_module,self.module)

    def run(self):
        '''
        use the instance to scan
        multithreading?
        '''
        for i in xrange(len(self.portlist)):
            self.scan_class(ip=self.ip,port=self.portlist[i]).run()

if __name__ == "__main__":
    parser = optparse.OptionParser("usage: %prog [options] ip")
    parser.add_option("-m","--module",default="SYN",help="The scan module to choose")
    parser.add_option("-p","--port",default="80",help="The port to scan")
    parser.add_option("-v","--verbose",action="store_true",help="The verbose output")

    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.print_help()
        sys.exit(0)

    p = PortScan(module=options.module,ip=args[0],port=options.port,verbose=options.verbose)
    p.run()
