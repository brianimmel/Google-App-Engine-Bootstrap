from utils import BaseHandler
from webapp2 import cached_property
import logging
from models import *


class HomeHandler(BaseHandler):
    def get(self):
        context = {
            "firstname": 'firstname',
            "lastname": 'lastname',
            "email": 'email',
            "comments": 'what did you think?'
        }
        return self.render_template('index.html', **context)