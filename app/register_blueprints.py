from flask import current_app as app
from app.blueprints.auth import bp as auth
from app.blueprints.blog import bp as blog
from app.blueprints.api import bp as api
from app.blueprints.main import bp as main

app.register_blueprint(auth)
app.register_blueprint(blog)
app.register_blueprint(api)
app.register_blueprint(main)