import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)       # instance of Flask stored in variable 'app'


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
# on final deployment change to *** debug=False ***
