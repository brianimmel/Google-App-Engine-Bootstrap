from utils import BasePageHandler, login_required
from webapp2 import cached_property
import logging

class LoginHandler(BasePageHandler):
    def get(self):
        """
        next = '/'
        if 'next' in self.request.GET:
            next = self.request.GET['next']
        return self.redirect( '%s?next=%s' % (self.url_for('auth_login'), next) )
        """
        return self.response.write("LOGOUT")

class LogoutHandler(BasePageHandler):
    def get(self):
        #clear session on the way out
        self.session.clear()
        """
        next = '/'
        if 'next' in self.request.GET:
            next = self.request.GET['next']
        return self.redirect( users.create_logout_url(next) )
        """
        return self.response.write("LOGOUT")