from flask import Blueprint, render_template

errors_errors_blueprint = Blueprint('errors', __name__, template_folder='templates', static_folder='static')

@errors_errors_blueprint.app_errorhandler(404)
def error_404(e):
    return render_template('404')