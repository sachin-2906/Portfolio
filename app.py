from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Serve main portfolio page
@app.route("/")
def portfolio():
    return render_template("index.html")   # ✅ your HTML file is index.html inside /templates

# Serve JSON data
@app.route("/data")
def data():
    with open("data.json", "r", encoding="utf-8") as f:   # ✅ your JSON file is data.json
        portfolio_data = json.load(f)
    return jsonify(portfolio_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"✅ Portfolio running at: http://127.0.0.1:{port}/")
    app.run(host="0.0.0.0", port=port, debug=True)
