from flask import Flask
from routes.agents import agents_bp

app = Flask(__name__)
app.register_blueprint(agents_bp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
