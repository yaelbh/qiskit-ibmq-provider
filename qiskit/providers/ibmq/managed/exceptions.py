# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Exception for the job manager modules."""

from ..exceptions import IBMQError


class IBMQJobManagerError(IBMQError):
    """Base class for errors raise by job manager."""
    pass


class IBMQJobManagerInvalidStateError(IBMQJobManagerError):
    """Errors raised when an operation is invoked in an invalid state."""
    pass


class IBMQJobManagerTimeoutError(IBMQJobManagerError):
    """Errors raised when a job manager operation times out."""
    pass
