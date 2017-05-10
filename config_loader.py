#!/usr/bin/python

import os
import sys


def load_test_config(filename):
    dict = {}
    if os.path.exists(filename):
        with open(filename, 'rb') as in_file:
            for line in in_file:
                if not line.startswith('#')
                    lst = line.strip().split("=")
                    dict[lst[0]] = lst[1]
    else:
        print >> sys.stderr, "Error, Please create test_config at %s" % os.path.join(
            sys.path[0])
        sys.exit(-1)

    return dict
