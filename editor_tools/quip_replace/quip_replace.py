#!/usr/bin/env python
#encode=utf-8

import optparse
import sys
import os
import re

class QuipReplace(object):
    def __init__(self, oldfile):
        self.oldfile = oldfile
        self.newfile = oldfile + '.new'

    def replace_image(self):
        old_image_num = len(re.findall(r'\[Image: .*?\]', self.old_file))
        for i in xrange(old_image_num):
            self.old_file = re.sub(r'\[Image: .*?\]', '![][%d]\n\n' % (i+1), self.old_file, 1)

    def replace_url(self):
        old_url = re.findall(r'\[_.*?_\]\(.*?\)', self.old_file)
        for i in xrange(len(old_url)):
            url = re.search(r'(?<=\().*?(?=\))', old_url[i]).group()
            self.old_file = re.sub(r'\[_.*?_\]\(.*?\)', '<%s>' % (url), self.old_file, 1)

    def main(self):
        with open(self.oldfile) as old:
            self.old_file = old.read()
        self.replace_image()
        self.replace_url()
        with open(self.newfile, 'w') as new:
            new.write(self.old_file)
        print '[+] Done!'

if __name__ == '__main__':
    parser = optparse.OptionParser('usage: %prog quip_markdown_file')
    parser.add_option('-f', '--filename', default='larry', help='The quip markdown file to replace image')

    (options, args) = parser.parse_args()
    if not os.path.exists(options.filename):
        parser.print_help()
        sys.exit(0)

    q = QuipReplace(options.filename)
    q.main()
