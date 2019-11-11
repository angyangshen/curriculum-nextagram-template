from flask import Blueprint, render_template,request,redirect,url_for,session,flash
from models.user import User_
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_required,login_user,logout_user,current_user


sessions_blueprint = Blueprint('sessions',
__name__, template_folder='templates')

@sessions_blueprint.route('/new',methods=['GET'])
def new():
    return render_template('sessions/new.html')

@sessions_blueprint.route('/',methods=['POST'])
def create():
    username = request.form.get('username')
    input_password = request.form.get('password')
    user = User_.get_or_none(username=username)   #get_or_none so that it wont show the bad looking error message when there's no such user in the db.
    if user:
        result = check_password_hash(user.password, input_password) 
        if result:
            flash("Log in successful!","success")
            login_user(user)
            return redirect(url_for('home'))
           
        else:
            flash("Wrong password, try again!")
            # session["user_id"]= user.id
            return redirect(url_for('sessions.new'))
    else:
        flash('No user with such username,try again!')
        return redirect(url_for('sessions.new')) 

# @sessions_blueprint('/destroy')
# @login_required
# def destroy():
#     logout_user()
#     flash("Successfully logged out.")
#     return redirect(url_for('home'))