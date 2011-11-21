import os, sys

# Add lib directory to path
current_path = os.path.abspath(os.path.dirname(__file__))
sys.path[0:0] = [
    os.path.join(current_path, 'lib'),
]

# DEBUG: True of False.  When True, verbose messages are logged at the
# DEBUG level.  Also, this flag is causes tracebacks to be shown in
# the web UI when an exception occurs.  (Tracebacks are always logged
# at the ERROR level as well.)
appstats_DEBUG = False



def webapp_add_wsgi_middleware(app):
    from google.appengine.ext.appstats import recording
    app = recording.appstats_wsgi_middleware(app)
    return app