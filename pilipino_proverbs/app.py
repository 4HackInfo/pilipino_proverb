from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)


proverbs = [
    {
        "id": 1,
        "filipino": "Ang hindi marunong lumingon sa pinanggalingan ay hindi makararating sa paroroonan.",
        "english": "He who does not look back to where he came from will never get to his destination.",
        "meaning": "We should learn to look back and honor our roots."
    },
    {
        "id": 2,
        "filipino": "Pag may tiyaga, may nilaga.",
        "english": "If there is perseverance, there is reward.",
        "meaning": "Hard work and patience lead to success."
    },
    {
        "id": 3,
        "filipino": "Aanhin pa ang damo kung patay na ang kabayo?",
        "english": "What use is the grass if the horse is already dead?",
        "meaning": "Help or resources are useless if they come too late."
    },
       {
        "id": 4,
        "filipino": "Pag may JOROSS, May pogi .",
        "english": "If JOROSS it was , all of the above JOROSS.",
        "meaning": "JOROSS POGI. HANDSOME. ALL OF THE ABOVE."
    }
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/proverbs")
def get_proverbs():
    return jsonify(proverbs)


@app.route("/api/proverbs/random")
def get_random_proverb():
    return jsonify(random.choice(proverbs))


@app.route("/api/proverbs/<int:proverb_id>")
def get_proverb_by_id(proverb_id):
    proverb = next((p for p in proverbs if p["id"] == proverb_id), None)
    if not proverb:
        return jsonify({"message": "Proverb not found"}), 404
    return jsonify(proverb)

if __name__ == "__main__":
    app.run(debug=True)
