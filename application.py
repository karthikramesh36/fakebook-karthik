import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()

def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    
    app.config.update(config_overrides)
    mongolab_uri = os.getenv('MONGOLAB_URI')

    #db.connect('fakebook36',mongolab_uri)
    db.init_app(app)
    
    from user.views import user_app
    app.register_blueprint(user_app)
    
    from relationship.views import relationship_app
    app.register_blueprint(relationship_app)
    
    return app