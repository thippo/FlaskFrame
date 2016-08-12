from flask import Blueprint, render_template

home_index_blueprint = Blueprint('index', __name__, url_prefix='/home', template_folder='templates', static_folder='static')

@home_index_blueprint.route('/')
def index():
    return render_template('index')