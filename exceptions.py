class JwtError(Exception):
    """
    Exception for JWT Error
    """

class AdminPasswordError(Exception):
    """
    Exception for failed login admin
    """

class AdminNotFoundError(Exception):
    """
    Exception if admin is not found
    """

class AdminIsNotLoginError(Exception):
    """
    Exception if admin is not login
    """