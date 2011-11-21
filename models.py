# -*- coding: utf-8 -*-
from google.appengine.ext import db, blobstore
from google.appengine.ext.db import polymodel
from google.appengine.api import images
from google.appengine.api import users
from webapp2 import cached_property
from datetime import datetime
import logging

class ExampleUser(db.Model):
    """
    What is this model used for?
    """
    is_enabled = db.BooleanProperty(default=True)
    
    firstname = db.StringProperty(required=True)
    lastname = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
    
    @property
    def id(self):
        if self.key():
            try:
                return self.key().id()
            except:
                return str(self.key().name())
        return None
        
    def __str__(self):
        return self.id