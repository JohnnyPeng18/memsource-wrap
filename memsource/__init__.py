from . import api


class Memsource(object):
    def __init__(self, user_name=None, password=None, token=None):
        """
        If token is given, use the token.
        Otherwise authenticate with user_name and password, and get token.
        """
        self.auth = api.Auth()

        (lambda token: [
            setattr(self, c.lower(), getattr(api, c)(token)) for c in api.__all__
        ])(self.auth.login(user_name, password).token if token is None else token)
