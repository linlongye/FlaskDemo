from app.api import api


@api.route("/hell")
def index():
    return "hello"
