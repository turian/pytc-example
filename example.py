#!/usr/bin/python
#
#  This code is based upon example.pl from the Perl TokyoCabinet API.
#

import sys

from pytc import HDB, HDBOWRITER, HDBOCREAT
hdb = HDB()
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
