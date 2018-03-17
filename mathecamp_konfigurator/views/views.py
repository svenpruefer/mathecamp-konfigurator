from mathecamp_konfigurator import app


@app.route('/')
def index():
    return 'Hello, World!'
