from flask import Blueprint, render_template,request,redirect,url_for

sessions_blueprint = Blueprint ('sessions',
__name__, template_folder='templates')

@sessions_blueprint.route('/new')