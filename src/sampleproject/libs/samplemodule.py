"""
samplemodule that performs sample operations.

Contains:
    - SampleClass
"""


def this_is_and_undocumented_function(some_parameter):  # noqa: D103
    return


class SampleClass:
    """Documentation of the SampleClass."""

    def __init__(self):
        """Initiatlizes samples class."""
        return

    @staticmethod
    def true():
        """Return True my friend."""
        return True

    @classmethod
    def false(cls):
        """
        Docstrings should not start with Returns...

        Nonetheless, returns False
        """
        return False
