from flask import Flask
from routes.task_api import task_bp

app = Flask(__name__)
app.register_blueprint(task_bp, url_prefix="/api/task")

@app.route("/")
def index():
    return "Omnipath API is running"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
