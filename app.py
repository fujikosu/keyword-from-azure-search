from flask import render_template, request, jsonify, Flask
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import analize_important_words

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def hello():
    return "Hello from an Azure Web App running on Linux! try SSH"


# API endpoint for keyword extraction
@app.route("/keyword", methods=["POST"])
def getlists():
    if request.method == "POST":
        response = {}
        response["keyword"] = analize_important_words.featured_words(
            request.json)
        return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)