#!/usr/bin/python3
# lists the states in hbtn_0e_0_usa database
# usage: ./0-select_states.py <username> <password> <dbname>

import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM `states`")
    [print(state) for state in cursor.fetchall()]
