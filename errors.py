"""Initializes all the custom exceptions raised by the API."""
# TODO: Add Description and messages for the exceptions.


class AuthTokenMissingError(Exception):
    pass


class AuthTokenInvalidError(Exception):
    pass


class InvalidObjectIdError(Exception):
    pass


class ObjectNotFoundError(Exception):
    pass


class InvalidRequestParametersError(Exception):
    pass


class UserNotFoundError(Exception):
    pass


class IncorrectPasswordError(Exception):
    pass
