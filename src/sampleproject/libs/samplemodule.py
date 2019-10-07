"""
samplemodule that performs sample operations.

Contains:
    - sampleclass
"""


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
