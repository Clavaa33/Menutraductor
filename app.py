import os, requests
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

VISION_KEY      = os.getenv("VISION_KEY")
VISION_ENDPOINT = os.getenv("VISION_ENDPOINT")
TRANSLATOR_KEY  = os.getenv("TRANSLATOR_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ocr", methods=["POST"])
def ocr():
    image = request.files["image"].read()
    url = VISION_ENDPOINT.rstrip("/") + "/vision/v3.2/ocr"
    headers = {"Ocp-Apim-Subscription-Key": VISION_KEY, "Content-Type": "application/octet-stream"}
    params  = {"language": "unk", "detectOrientation": "true"}
    r = requests.post(url, headers=headers, params=params, data=image)
    r.raise_for_status()
    regions = r.json().get("regions", [])
    text = " ".join(
        word["text"]
        for region in regions
        for line in region["lines"]
        for word in line["words"]
    )
    return jsonify({"text": text})

@app.route("/translate", methods=["POST"])
def translate():
    body   = request.get_json()
    text   = body.get("text", "")
    target = body.get("target_lang", "ca")
    url     = "https://api.cognitive.microsofttranslator.com/translate"
    headers = {
        "Ocp-Apim-Subscription-Key": TRANSLATOR_KEY,
        "Ocp-Apim-Subscription-Region": os.getenv("TRANSLATOR_REGION"),
        "Content-Type": "application/json"
    }
    params  = {"api-version": "3.0", "to": target}
    r = requests.post(url, headers=headers, params=params, json=[{"text": text}])
    r.raise_for_status()
    translated = r.json()[0]["translations"][0]["text"]
    return jsonify({"translated": translated})

if __name__ == "__main__":
    app.run(debug=True)