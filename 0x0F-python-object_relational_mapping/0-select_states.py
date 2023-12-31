#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa:
"""

import MySQLdb
import sys

if __name__ == "__main__":

    usr, pwd, datab = sys.argv[1:4]
    lh = "localhost"
    p = 3306
    db = MySQLdb.connect(host=lh, port=p, user=usr, passwd=pwd, db=datab)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
