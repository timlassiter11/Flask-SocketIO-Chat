from flask import redirect, url_for, render_template
from . import main


@main.route('/', methods=['GET'])
def index():
    return render_template('chat.html')
