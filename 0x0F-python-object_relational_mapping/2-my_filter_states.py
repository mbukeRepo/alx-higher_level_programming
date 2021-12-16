#!/usr/bin/python3
# lists states that matches the name passed

import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM `states` \
                            WHERE BINARY `name` = '{}'".format(sys.argv[4]))

    [print(state) for state in cur.fetchall()]
