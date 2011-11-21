from utils import BasePageHandler
from webapp2 import cached_property
import logging

class HomeHandler(BasePageHandler):
    def get(self):
        context = {

        }
        return self.render_template('index.html', **context)