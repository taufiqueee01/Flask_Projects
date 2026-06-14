from flask import Flask,render_template,request,redirect,session
import json

app = Flask(__name__)
app.secret_key = "adfj1212aksd"

with open("db.json","r") as j:
    Open_db=json.load(j)





@app.route("/",methods=["POST","GET"])
def index():

    if session.get("username"):
        return render_template("chat_area.html",username=session.get("username"),Open_db=Open_db)

    if request.method=="POST":
        username=request.form.get("username")
        session["username"] = username
        return redirect("chat_area.html")
    
    return render_template("index.html")
       


@app.route("/chat_area.html",methods=["POST","GET"])
def chatarea():
    if  not session.get("username"):
        return redirect("/")
        
    if request.method=="POST":
        username=session.get("username")
        message=request.form.get("user_message")
        print("POST RECEIVED")
        print(request.form)
        print(message)
        print(Open_db)

        Open_db.append({
            username: message
        })
        with open("db.json","w")as Open_json:
            json.dump(Open_db,Open_json)

    return render_template("chat_area.html",Open_db=Open_db,username=session.get("username"))
    
        
    
    
app.run(debug=True)