#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Usage:
#
#

import getopt
import sys
import os



def exe_test_command(fout, BIN, ARGS):
    pop = sp.Popen(ARGS, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
    rcode = sp.Popen.wait(pop)
    stdout, stderr = pop.communicate()
    print_fas(fout, "\n")
    if stdout or stderr:
        print_fas(fout, "Output:\n", stdout, stderr)
    if rcode:
        print_fas(fout, "Got non zero return code:%s\nRet = %d" %
                  (str(BIN), rcode))
    return


if __name__ == '__main__':
    with open(TESTCASE_CSV) as f:
        lines = f.readlines()

    try:
        ol, args = getopt.getopt(sys.argv[1:], "t:vxd:")
    except getopt.GetoptError:
        print_cmd_usage()

    # 引数のパース
    for o, arg in ol:
        if o == "-v":
            QUIET_OUTPUT = False
        if o == "-x":
            SPHINX = True
        if o == "-d":
            test_categories = arg.split(",")
        if o == "-t":
            hoges = arg.split(",")
