# run_web.py
from easyagent.webui import web_bp
from flask import Flask
# EXAMPLE
app = Flask(__name__)
app.register_blueprint(web_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4090)
