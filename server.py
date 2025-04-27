from flask import Flask, render_template

app = Flask(__name__)

nav = [
    
    { "title": "Бард", "URL": "/bard" },
    { "title": "Волшебник", "URL": "/wizard" },
    { "title": "Друид", "URL": "/druid" },
    { "title": "Жрец", "URL": "/cleric" },
    { "title": "Глоссарий", "URL": "/gloss" },
    { "title": "Об авторе", "URL": "/" },
]

@app.route("/")
@app.route("/author")
def author():
    return render_template("author.html", name = "Об авторе", nav=nav)
@app.route("/bard")
def bard():
    return render_template("bard.html", name = "Бард", nav=nav)
@app.route("/cleric")
def cleric():
    return render_template("cleric.html", name = "Жрец", nav=nav)
@app.route("/druid")
def druid():
    return render_template("druid.html", name = "Друид", nav=nav)
@app.route("/gloss")
def gloss():
    return render_template("gloss.html", name = "Глоссарий", nav=nav)
@app.route("/wizard")
def wizard():
    return render_template("wizard.html", name = "Волшебник", nav=nav)
