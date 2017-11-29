from flask import Flask,render_template,redirect,request,flash,session

app = Flask(__name__)
app.secret_key = "name"

@app.route('/')
def ind():
    return render_template("index.html")
@app.route("/result", methods=["POST"])
def res():
    dojo = request.form["dojo"]
    favlang = request.form['favlang']
    if 0 < len(request.form["name"]) < 121:
        name= request.form["name"]
    else:
        flash("name empty or too long!")
        return redirect("/")
    if 0 < len(request.form["comment"]) < 121:
        comment = request.form['comment']
        return render_template('result.html',name= name, dojo = dojo, favlang= favlang,comment = comment)
    else:
        flash(" comment empty or too long!")
        return redirect("/")
app.run(debug= True)

