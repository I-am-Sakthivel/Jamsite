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
            return redirect('/6e686d5bd5cb58ae1c865206be71fc3560ea6fa8f32da3ed25bf99cda104ee1d')
        else:
            return render_template("failed_login.html")
    return render_template("login.html")

@app.route('/6e686d5bd5cb58ae1c865206be71fc3560ea6fa8f32da3ed25bf99cda104ee1d')
def ind():
    return render_template('index.html')


if __name__ == '__main__':

    app.run()

