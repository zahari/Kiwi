# Copyright (c) 2019 Alexander Todorov <atodorov@MrSenko.com>

# Licensed under the GPL 2.0: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

from modernrpc.core import rpc_method

from tcms.testruns.models import TestExecutionStatus


@rpc_method(name='TestExecutionStatus.filter')
def filter(query):  # pylint: disable=redefined-builtin
    """
    .. function:: XML-RPC TestExecutionStatus.filter(query)

        Search and return the list of test case run statuses.

        :param query: Field lookups for :class:`tcms.testruns.models.TestExecutionStatus`
        :type query: dict
        :return: Serialized list of :class:`tcms.testruns.models.TestExecutionStatus` objects
        :rtype: list(dict)
    """
    return TestExecutionStatus.to_xmlrpc(query)
