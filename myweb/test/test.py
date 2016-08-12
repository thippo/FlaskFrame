from flask import Blueprint, render_template, redirect, session, url_for, request, jsonify
from flask_oauthlib.client import OAuth

test_test_blueprint = Blueprint('test', __name__, url_prefix='/test', template_folder='templates', static_folder='static')
oauth = OAuth(test_test_blueprint)

github = oauth.remote_app(
    'github',
    consumer_key='f471042e92244df202b8',
    consumer_secret='55339d5ffe35874fcf73656972b0339e7be75cfb',
    request_token_params={'scope': 'meiyou'},
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)

@test_test_blueprint.route('/test')
def index():
    if 'github_token' in session:
        me = github.get('user')
        return str(me.data)+"<br><a href='/test/logout'>logout</a>"
    return "<a href='/test/login'>github</a>"

@test_test_blueprint.route('/login')
def login():
    return github.authorize(callback=url_for('test.authorized', _external=True))

@test_test_blueprint.route('/logout')
def logout():
    session.pop('github_token', None)
    return redirect(url_for('test.index'))

@test_test_blueprint.route('/login/authorized')
def authorized():
    resp = github.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error'],
            request.args['error_description']
        )
    session['github_token'] = (resp['access_token'], '')
    return redirect(url_for('test.index'))

@github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')