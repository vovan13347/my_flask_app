from flask import *


app = Flask(__name__)


@app.route('/about')
def about():
    return 'О себе'

username = 'admin'
@app.route('/user/<username>')
def show_user_profile(username):
    return ('Добро пожаловать,' + username)

page_num = 6
@app.route('/page/<int:page_num>')
def get_page(page_num):
    return f'Страница: {page_num}'



admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
def admin_dashboard():
    return 'Admin Dashboard'

app.register_blueprint(admin_bp)

@app.errorhandler(404)
def page_not_fount(e):
    return 'Страница не найдена', 404


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bestuser'}
    return render_template('index.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)