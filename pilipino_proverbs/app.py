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
    },
    {
        "id": 5,
        "filipino": "Kapag ang tao’y matipid, maraming maililigpit.",
        "english": "If a person is thrifty, much can be saved.",
        "meaning": "Saving and being thrifty leads to financial stability."
    },
    {
        "id": 6,
        "filipino": "Ang taong walang kibo, nasa loob ang kulo.",
        "english": "A quiet person may be boiling inside.",
        "meaning": "Silent people often hide strong emotions."
    },
    {
        "id": 7,
        "filipino": "Huwag gawin sa iba ang ayaw mong gawin sa iyo.",
        "english": "Do not do unto others what you do not want done to you.",
        "meaning": "Treat others the way you want to be treated."
    },
    {
        "id": 8,
        "filipino": "Nasa Diyos ang awa, nasa tao ang gawa.",
        "english": "Mercy is with God, but action is with man.",
        "meaning": "Prayers must be accompanied by action."
    },
    {
        "id": 9,
        "filipino": "Kung ano ang itinanim, siya ring aanihin.",
        "english": "What you plant is what you harvest.",
        "meaning": "You reap what you sow."
    },
    {
        "id": 10,
        "filipino": "Daig ng maagap ang masipag.",
        "english": "The prompt surpasses the diligent.",
        "meaning": "Being early and proactive is better than just being hardworking."
    },
    {
        "id": 11,
        "filipino": "Ubos-ubos biyaya, bukas nakatunganga.",
        "english": "Spend all blessings today, have nothing tomorrow.",
        "meaning": "Be wise in using your blessings to avoid future problems."
    },
    {
        "id": 12,
        "filipino": "Lumilipas ang panahon, ngunit ang alaala’y nananatili.",
        "english": "Time passes, but memories remain.",
        "meaning": "Memories are lasting even as time moves on."
    },
    {
        "id": 13,
        "filipino": "Ang hindi marunong magmahal sa sariling wika ay higit pa sa hayop at malansang isda.",
        "english": "He who does not love his own language is worse than an animal or a smelly fish.",
        "meaning": "Love and respect your native language."
    },
    {
        "id": 14,
        "filipino": "Kung hindi ukol, hindi bubukol.",
        "english": "If it’s not meant to be, it will not happen.",
        "meaning": "Destiny cannot be forced."
    },
    {
        "id": 15,
        "filipino": "Bato-bato sa langit, ang tamaan huwag magagalit.",
        "english": "Rocks thrown into the sky, whoever gets hit should not be angry.",
        "meaning": "Take criticism lightly if it applies to you."
    },
    {
        "id": 16,
        "filipino": "Kapag ang puno’t dulo ay mali, mali rin ang bunga.",
        "english": "If the root is wrong, the fruit will also be wrong.",
        "meaning": "A wrong foundation leads to wrong outcomes."
    },
    {
        "id": 17,
        "filipino": "Ang buhay ay parang gulong, minsan nasa ibabaw, minsan nasa ilalim.",
        "english": "Life is like a wheel, sometimes on top, sometimes at the bottom.",
        "meaning": "Life is full of ups and downs."
    },
    {
        "id": 18,
        "filipino": "Hindi lahat ng kumikinang ay ginto.",
        "english": "Not everything that glitters is gold.",
        "meaning": "Not everything that looks valuable is truly precious."
    },
    {
        "id": 19,
        "filipino": "Mahirap gisingin ang nagtutulog-tulugan.",
        "english": "It’s hard to wake someone pretending to be asleep.",
        "meaning": "You can’t convince those who refuse to listen."
    },
    {
        "id": 20,
        "filipino": "Matibay ang walis, palibhasa’y magkabigkis.",
        "english": "A broom is sturdy because its strands are tightly bound.",
        "meaning": "Unity is strength."
    },
    {
        "id": 21,
        "filipino": "Ang taong walang utang na loob ay masahol pa sa hayop.",
        "english": "A person without gratitude is worse than an animal.",
        "meaning": "Always be grateful for the help you receive."
    },
    {
        "id": 22,
        "filipino": "Habang may buhay, may pag-asa.",
        "english": "As long as there is life, there is hope.",
        "meaning": "Never give up while you are still alive."
    },
    {
        "id": 23,
        "filipino": "Ang sakit ng kalingkingan, ramdam ng buong katawan.",
        "english": "The pain of the little finger is felt by the whole body.",
        "meaning": "The suffering of one affects all."
    },
    {
        "id": 24,
        "filipino": "Kung walang tiyaga, walang nilaga.",
        "english": "Without perseverance, there is no reward.",
        "meaning": "Success requires patience and effort."
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
