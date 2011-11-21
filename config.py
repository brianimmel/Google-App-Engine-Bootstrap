# -*- coding: utf-8 -*-
import os
import sys

DEV = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')
PRODUCTION = not DEV

# Add lib directory to path
current_path = os.path.abspath(os.path.dirname(__file__))
sys.path[0:0] = [
    os.path.join(current_path, 'lib'),
]

# Begin App Config
config = {}

#Jinja
config['jinja2'] = {
    'template_path': 'templates'
}


# Sessions
config['webapp2_extras.sessions'] = {
    'secret_key': 'xxxxxxxxxxx',
    'cookie_name': 'ABC',
    'session_max_age': 86400 * 7, #days
    'cookie_args': { #details for cookie
        'max_age': 60 * 60 * 24 * 30 # 30 days till cookie expires
    },
    'backends': {
        'datastore': 'webapp2_extras.appengine.sessions_ndb.DatastoreSessionFactory', 
        'memcache': 'webapp2_extras.appengine.sessions_memcache.MemcacheSessionFactory', 
        'securecookie': 'webapp2_extras.sessions.SecureCookieSessionFactory'
    }
}


# Server Environment
config['server'] = {
    'DEV': DEV,
    'PRODUCTION': PRODUCTION,
    'DOMAIN': 'example.com',
    'PORT': ''
}