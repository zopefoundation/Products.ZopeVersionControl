##############################################################################
#
# Copyright (c) 2003 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 1.2 (ZPL).  A copy of the ZPL should accompany this
# distribution.
#
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Run all Zope Version Control tests

$Id$"""

import unittest

from Products.ZopeVersionControl.tests import testVersionControl

try:
    from Products import References
except ImportError:
    # References product is not available
    testReferenceVersioning = None
else:
    # References product is available
    from Products.ZopeVersionControl.tests import testReferenceVersioning


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(testVersionControl.test_suite())
    if testReferenceVersioning is not None:
        suite.addTest(testReferenceVersioning.test_suite())
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest="test_suite")
