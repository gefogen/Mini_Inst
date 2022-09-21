from flask import Blueprint, render_template, request, redirect
from utils import *
from config1 import *

error_blueprint = Blueprint('error_blueprint', __name__, template_folder="templates")


@error_blueprint.app_errorhandler(404)
def handle_404(error):
    """ Обрабатываем ошибку 404 """
    return render_template('error.html', er_code=404), 404


@error_blueprint.app_errorhandler(500)
def handle_500(error):
    """ Обрабатываем ошибку 500 """
    return render_template('error.html', er_code=500), 500
