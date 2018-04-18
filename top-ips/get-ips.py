

import socket
import sys
import os.path

__author__ = "Abhimanyu Nagurkar"
__copyright__ = "Copyright (C) Nginx Inc. All rights reserved."
__license__ = ""
__maintainer__ = "Abhimanyu Nagurkar"
__email__ = "abhimanyu.nagurkar@nginx.com"


"""
Assumption here is that the access.log will have IP address as first column
"""

if len(sys.argv) > 1:
    if os.path.isfile(sys.argv[1]):
        ips = {}
        file = open(sys.argv[1], "r");
        content = file.readlines()
        for line in content:
            ip = line.split(" ")[0]
            try:
                # for ip address validation only
                socket.inet_aton(ip)
                ips[ip] = ips.get(ip, 0) + 1
            except socket.error:
                print "Address not valid"

        sorted_ips = [(k,v) for v,k in sorted([(v,k) for k,v in ips.items()],reverse=True)]

        for ip in sorted_ips[:10]:
            print  ip[1] , ip[0]
        file.close()
    else:
        print "Provide correct access log path"
else:
    print "Provide access log path"
