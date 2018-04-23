
import sys
import os.path
import collections

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
        cnt = collections.Counter()
        with open(sys.argv[1]) as infile:
            for line in infile:
                ip = line.split(" ")[0]
                cnt[ip] += 1

        for ip in cnt.most_common(10)[:10]:
            print  ip[1] , ip[0]

    else:
        print "Provide correct access log path"
else:
    print "Provide access log path"
