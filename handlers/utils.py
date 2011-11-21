from webapp2 import RequestHandler, cached_property
from webapp2_extras import jinja2, sessions
import webapp2
import logging
from datetime import datetime
from google.appengine.api import channel

def login_required(handler_method):
    def check_login(self, *args, **kwargs):
        if self.request.method != 'GET':
            self.abort(400, detail='The login_required decorator can only be used for GET requests.')
        if self.user.is_anonymous:
            return self.redirect( "%s?next=%s" % (self.url_for('auth_login'), self.request.path)  )
        else:
            handler_method(self, *args, **kwargs)
    return check_login

class BasePageHandler(RequestHandler):
    def __init__(self, request=None, response=None):
        super(BasePageHandler, self).__init__(request, response)
        # Add some common stuff to context. 
        self.context = { 
            #'current_url': self.request.url, 
            'current_path': self.request.path,
            'is_production': self.is_production, 
            'is_dev': not self.is_production, 
            #'request': request, 
        } 

    # Some stuff that is updated later 
    def update_context(self, values): 
        self.context.update(values) 
        self.context.update({ 
            'messages': self.get_messages(), 
            'user': self.user,
            "session_id": self.session,
            'url_for': self.url_for,
        })

    @cached_property
    def user(self):
        return user
        
    def set_message(self, message, level="info"):
        self.session.add_flash(message, str(level))
        
    def get_messages(self):
        return self.session.get_flashes()
        
    def send_socket_data(self, socket_key, data):
        channel.send_message(socket_key, data)
 
    def render_template(self, _filename, **context):
        self.update_context(context) 
        return self.response.write(self.jinja2.render_template(_filename, **self.context))
        
    @cached_property
    def is_production(Self):
        app = webapp2.get_app()
        return app.config.get('server')['PRODUCTION']

    @cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)
        
    # Session support
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session(backend='securecookie')