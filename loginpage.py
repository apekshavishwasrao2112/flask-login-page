from flask import Flask , render_template , request  
import os

app=Flask(__name__)

user={}

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login" , methods=["GET" , "POST"])
def login():
    err=None
    
    if request.method=="POST":

        username=request.form.get("username")
        password=request.form.get("password")

        if username in user  and user[username] == password:
            return render_template("welcome.html" , username=username)
        
        else:
           err= "Invalid Username and password!! Try Again"

    return render_template("login.html" , err=err)


@app.route("/signup" , methods=["GET" , "POST"])
def signup():
    success=None

    if request.method=="POST":

        username=request.form.get("username")
        password=request.form.get("password")

        user[username]=password 

        success= "Signup Sucessfully!!"

    return render_template("signup.html" , success=success)
      


@app.route("/welcome" )
def welcome():
    return render_template("welcome.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)