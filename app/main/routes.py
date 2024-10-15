from flask import redirect, url_for, render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('.chat'))

@main.route('/chat')
def chat():
    return render_template('chat.html')
