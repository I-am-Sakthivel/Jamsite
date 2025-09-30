from flask import Flask,request,render_template,redirect
from dotenv import load_dotenv
import os
load_dotenv()
app=Flask(__name__,template_folder='Templates')
@app.route("/",methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        u,p=os.getenv('u'),os.getenv('p')
        if u==username and p==password:
            return redirect(os.getenv('index'))
        else:
            return render_template("failed_login.html")
    return render_template("login.html")

@app.route(os.getenv('index'))
def ind():
    return render_template('index.html')


if __name__ == '__main__':

    app.run()


