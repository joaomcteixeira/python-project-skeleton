class SampleClass:
    """
    This is the documentation of the SampleClass.
    """
    def __init__(self):
        """
        And this is the documentation of the init
        method of the SampleClass.
        """
        return
    def true(self):
        """
        Returns True my friend.
        """
        return True

    @classmethod
    def false(cls):
        """
        Docstrings should not start with Returns...

        Nonetheless, returns False
        """
        return False
