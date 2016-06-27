import subprocess
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

with open('config.ini') as f:
    for config in f:
        config = config.strip()
        while 1:
            output = subprocess.check_output(['python','new.py',config])
            if output:
                if 'No such file' not in output and 'Permission denied' not in output:
                    with open('result.txt','a') as c:
                        c.write(output)
                break
