#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/10/15 11:43:08 (UT+8) daisuke>
#

# importing sqlite module
import sqlite3

# importing contextlib module
import contextlib

# database file name
file_db = 'hip.db'

# SQL command for making a table
sql_maketable = f'create table hip (hip integer primary key, ' \
    + f'ra_hms text, ra_deg real, dec_dms text, dec_deg real, ' \
    + f'vmag real, bv real, vi real, parallax real, ' \
    + f'pmra real, pmdec real, sptype text);'

# opening a connection to database
with contextlib.closing (sqlite3.connect (file_db)) as conn:
    # constructing a cursor object
    cursor = conn.cursor ()

    # making a table
    cursor.execute (sql_maketable)

    # committing transaction
    conn.commit ()
