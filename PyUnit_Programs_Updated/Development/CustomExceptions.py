class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueOutOfBoundError(Error):
	""" Raise when value is not in given bound """
	pass

class NegativeValueError(Error):
	""" Raise when value is negative """
	pass

class ValueError(Error):
	""" Raise when value is not a number """
	pass

class ValueTooSmallError(Error):
	""" Raise when value is less then or equal to 0 """
	pass

class IndexError(Error):
	""" Raise when all value is not entered """
	pass