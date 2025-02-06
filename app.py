from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# List of your AI web apps
# Load the list of AI web apps from a JSON file
with open(os.path.join(os.path.dirname(__file__), 'ai-apps.json')) as f:
    apps = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", apps=apps)

if __name__ == "__main__":
    app.run(debug=True)
