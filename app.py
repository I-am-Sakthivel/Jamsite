from flask import Flask,request,render_template,redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from dotenv import load_dotenv
import os
load_dotenv()
app=Flask(__name__,template_folder='Templates')
app.secret_key=os.getenv('secret')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
    id = 1
    username = os.getenv('u')
    password = os.getenv('p')

@login_manager.user_loader
def load_user(user_id):
    if user_id==str(user.id):
        return user
    return None
user = User()

@app.route("/",methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        u,p=os.getenv('u'),os.getenv('p')
        if u==username and p==password:
            login_user(user)
            return redirect(os.getenv('index'))
        else:
            return render_template("failed_login.html")
    return render_template("login.html")

@app.route(os.getenv('index'))
@login_required
def ind():
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

if __name__ == '__main__':

    app.run()

