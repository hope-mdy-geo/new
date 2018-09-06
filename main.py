
from flask import Flask , render_template, request, jsonify
import Uni_To_Zg
import Zg_To_Uni
import Win_To_Uni
import Uni_To_Win
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/unitozawgyi")
def unitozawgyi():
    return render_template("unitozawgyi.html")

@app.route("/convert", methods=["POST"])
def convert():
    myinput = request.form['myinput']
    myinput = Uni_To_Zg.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "No input text!"})

@app.route("/zawgyitouni")
def zawgyitouni():
    return render_template("zawgyitouni.html")

@app.route("/convert1", methods=["POST"])
def convert1():
    myinput = request.form['myinput']
    myinput = Zg_To_Uni.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "No input text!"})

@app.route("/wintouni")
def wintouni():
    return render_template("wintouni.html")

@app.route("/convert2", methods=["POST"])
def convert2():
    myinput = request.form['myinput']
    myinput = Win_To_Uni.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "No input text!"})

@app.route("/unitowin")
def unitowin():
    return render_template("unitowin.html")

@app.route("/convert3", methods=["POST"])
def convert3():
    myinput = request.form['myinput']
    myinput = Uni_To_Win.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': ""})


@app.route("/wintozawgyi")
def wintozawgyi():
    return render_template("wintozawgyi.html")

@app.route("/convert4", methods=["POST"])
def convert4():
    myinput = request.form['myinput']
    myinput = Win_To_Uni.convert(myinput)
    myinput = Uni_To_Zg.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "No input text!"})

@app.route("/zawgyitowin")
def zawgyitowin():
    return render_template("zawgyitowin.html")

@app.route("/convert5", methods=["POST"])
def convert5():
    myinput = request.form['myinput']
    myinput = Zg_To_Uni.convert(myinput)
    myinput = Uni_To_Win.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': ""})

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/howitwork")
def howitwork():
    return render_template("howitwork.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/question")
def question():
    return render_template("question.html")

@app.route("/about1")
def about1():
    return render_template("about1.html")

@app.route("/howitwork1")
def howitwork1():
    return render_template("howitwork1.html")

@app.route("/resources1")
def resources1():
    return render_template("resources1.html")

@app.route("/contact1")
def contact1():
    return render_template("contact1.html")

@app.route("/question1")
def question1():
    return render_template("question1.html")

if __name__ == "__main__":
    app.run(debug=True)
