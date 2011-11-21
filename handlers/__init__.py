from utils import BaseHandler
from webapp2 import cached_property
from google.appengine.api import users
import logging
from uuid import uuid4 as uuid
import simplejson as json
from datetime import datetime
import time

from google.appengine.api import channel

from models import *

# NEW / NEED CLEANUP
import cgi
import pickle
from google.appengine.ext.webapp import RequestHandler, template
from google.appengine.ext import db
from google.appengine.api import taskqueue
import webapp2
import random
from os import urandom

class LoginHandler(BaseHandler):
    def get(self):
        next = '/'
        if 'next' in self.request.GET:
            next = self.request.GET['next']
        return self.redirect( '%s?next=%s' % (self.url_for('auth_login'), next) )

class LogoutHandler(BaseHandler):
    def get(self):
        #clear session on the way out
        self.session.clear()
        next = '/'
        if 'next' in self.request.GET:
            next = self.request.GET['next']
        return self.redirect( users.create_logout_url(next) )