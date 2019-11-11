from flask import Blueprint, render_template,request,redirect,url_for
from models.user import User_ as u 
from werkzeug.security import generate_password_hash

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')


@users_blueprint.route('/', methods=['POST'])
def create():
    
    username = request.form.get('username')
    password = generate_password_hash(request.form.get('password'))
    email = request.form.get('email')
    u(username=username,password=password,email=email).save()
    return redirect(url_for('home'))



@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass

@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
