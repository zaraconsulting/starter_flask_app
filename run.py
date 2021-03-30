from app import create_app, cli

from app.blueprints.blog.models import Post

app = create_app()
cli.register(app)

@app.shell_context_processor
def makeShellContext():
    return dict(Post=Post)