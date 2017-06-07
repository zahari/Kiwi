# -*- coding: utf-8 -*-
"""
    Helper functions which facilitate actual communications with Bugzilla.
"""

import warnings
import threading

from django.conf import settings
from django.core.urlresolvers import reverse


class BugzillaThread(threading.Thread):
    """
        Execute Bugzilla RPC code in a thread!

        Executed from the IssueTracker interface methods.
    """

    def __init__(self, rpc, testcase, bug):
        """
            @rpc - Bugzilla XML-RPC object
            @testcase - TestCase object
            @bug - TestCaseBug object
        """

        self.rpc = rpc
        self.testcase = testcase
        self.bug = bug
        super(BugzillaThread, self).__init__()

    def run(self):
        """
            Using Bugzilla's XML-RPC try to link the test case with
            the bug!
        """

        try:
            text = """---- Bug confirmed via test case ----
URL: %s
Summary: %s""" % (settings.KIWI_BASE_URL + reverse('testcases-get', args=[self.testcase.pk]),
                  self.testcase.summary)

            self.rpc.update_bugs(self.bug.bug_id, {'comment': {'comment': text, 'is_private': False}})
        except Exception, err:
            message = '%s: %s' % (err.__class__.__name__, err)
            warnings.warn(message)
