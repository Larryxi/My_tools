**note**

use socket to enumerate file on tftp server.

**usage**

    $ python tftp_udp_enum.py 
    Usage: tftp_udp_enum.py [options] server

    Options:
    -h, --help            show this help message and exit
        -p PORT, --port=PORT  The port of TFTP server to enumerate files on it
        -f FILENAME, --filename=FILENAME
                                The file which contains the filenames to enumerate


**example**

    $ cat test_tftp
    larry
    testtest
    11111
    $ python tftp_udp.py -f test_tftp 192.168.1.108
    [+] The file 'larry' is on the server
    [+] The file 'testtest' is on the server
    [+] Enumserate Done!

