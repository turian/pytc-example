#!/usr/bin/python
#
#  This code is based upon example.pl from the Perl TokyoCabinet API.
#

import sys

from pytc import HDB, HDBOWRITER, HDBOCREAT
hdb = HDB()
# Open a hashdb for writing if it exists, or create a new one
# This database is uncompressed. See hashdb.create for example of compression.
hdb.open("casket.tch", HDBOWRITER | HDBOCREAT)

# store records
hdb.put("foo", "hop")
hdb.put("bar", "step")
hdb.put("baz", "jump")

# retrieve records
print hdb.get("foo")

# traverse records
hdb.iterinit()
for key in hdb.keys():
    print "%s:%s" % (key, hdb.get(key))

# close the database
hdb.close()
