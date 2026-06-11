from flask import Flask,render_template,request

app=Flask(__name__)
students={
        "Sufiyan":97,
        "Wais": 98,
        "Taufique": 95
        }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():

    
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username=="Tau" and password == "123":
            return render_template("result_portel.html",students=students)
        else:
            return "Wrong username or password! Please try again"
    return render_template("login.html")

app.run(debug=True)

