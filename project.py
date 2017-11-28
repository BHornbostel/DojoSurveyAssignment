from flask import Flask,render_template,redirect,request
app = Flask(__name__)

@app.route('/')
def ind():
    return render_template("index.html")
@app.route("/result", methods=["POST"])
def res():
    name= request.form["name"]
    dojo = request.form["dojo"]
    favlang = request.form['favlang']
    comment = request.form['comment']
    return render_template('result.html',name= name, dojo = dojo, favlang= favlang,comment = comment)
app.run(debug= True)

