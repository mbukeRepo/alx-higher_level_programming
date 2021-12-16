#!/usr/bin/python3
# lists cities in database with its state

import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                                   FROM `cities` \
                                   INNER JOIN states \
                                   ON cities.state_id = states.id \
                                   ORDER BY cities.id")

    [print(city) for city in cur.fetchall()]
