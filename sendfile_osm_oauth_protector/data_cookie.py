from http.cookies import SimpleCookie


class DataCookie:
    def __init__(self, config):
        """
        Args:
            config (Config): configuration
        """
        self.config = config

    def _output_cookie(self, logged_in, encrypted_signed_tokens=None):
        """
        Return an instance of http.cookies.SimpleCookie.

        See doc/cookie.md for a description of the contents of the cookie.

        Args:
            logged_in (boolean): if the user is logged in (successfully
                                 authenticated)
            encrypted_signed_tokens (str): encrypted and signed concatenation
                                           of the access token, access token
                                           secret and date of the next full
                                           verification

        Returns:
            http.cookies.SimpleCookie: the cookie
        """
        cookie = SimpleCookie()
        if logged_in:
            cookie[self.config.COOKIE_NAME] = "login|{}|{}".format(self.config.KEY_NAME, encrypted_signed_tokens)
        else:
            cookie[self.config.COOKIE_NAME] = "logout||"
        cookie[self.config.COOKIE_NAME]["httponly"] = True
        if self.config.COOKIE_SECURE:
            cookie[self.config.COOKIE_NAME]["secure"] = True
        return cookie[self.config.COOKIE_NAME].OutputString()

    def logout_cookie(self):
        """
        Return a cookie for a logged out user.

        Returns:
            http.cookies.SimpleCookie: the cookie
        """
        return self._output_cookie(False)