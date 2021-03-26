##############################################################################
#
# Copyright (c) 2001 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################
"""Unit testing utilities."""
import transaction


def common_setUp(self):
    # Install a hack to make SimpleItem version aware, so that the
    # tests work. In normal development, you would mix in the
    # VersionSupport class on an as-needed basis.
    from AccessControl.SecurityManagement import newSecurityManager
    from OFS.Application import Application
    from OFS.DTMLDocument import addDTMLDocument
    from OFS.Folder import manage_addFolder
    from Testing.makerequest import makerequest

    import Products.ZopeVersionControl
    Products.ZopeVersionControl.install_hack()

    from six import StringIO

    from ZODB import DB
    from ZODB.DemoStorage import DemoStorage

    from Products.ZopeVersionControl.ZopeRepository import addRepository

    s = DemoStorage()
    self.connection = DB(s).open()
    try:
        r = self.connection.root()
        a = Application()
        r['Application'] = a
        self.root = a
        responseOut = self.responseOut = StringIO()
        self.app = makerequest(self.root, stdout=responseOut)
        self.app.acl_users.userFolderAddUser('UnitTester', '123', (), ())
        manage_addFolder(self.app, 'folder1')
        self.folder1 = getattr(self.app, 'folder1')
        manage_addFolder(self.folder1, 'folder2')
        self.folder2 = getattr(self.folder1, 'folder2')
        addDTMLDocument(self.folder2, 'document1', file='some text')
        self.document1 = getattr(self.folder2, 'document1')
        addDTMLDocument(self.folder2, 'document2', file='some text')
        self.document2 = getattr(self.folder2, 'document2')
        addDTMLDocument(self.folder2, 'document_nonversion', file='some?')
        self.document_nonversion = getattr(self.folder2,
                                           'document_nonversion')
        self.document_nonversion.__non_versionable__ = 1
        addRepository(self.folder1, 'repository')
        self.repository = getattr(self.folder1, 'repository')
        transaction.commit()
    except BaseException:
        self.connection.close()
        raise
    transaction.begin()
    user = self.app.acl_users.getUser('UnitTester')
    user = user.__of__(self.app.acl_users)
    newSecurityManager(None, user)


def common_tearDown(self):
    from AccessControl.SecurityManagement import noSecurityManager
    noSecurityManager()
    del self.folder1
    del self.folder2
    del self.document1
    del self.document2
    transaction.abort()
    self.app._p_jar.sync()
    self.connection.close()
    del self.app
    del self.responseOut
    del self.root
    del self.connection


def common_commit(self):
    if self.do_commits:
        transaction.commit()
