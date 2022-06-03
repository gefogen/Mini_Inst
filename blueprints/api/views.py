from flask import Blueprint, jsonify
import logging
from utils import *

logger = logging.getLogger('logger')    # Создаем регистратор
logger.setLevel(logging.INFO)

ch = logging.FileHandler('logs/api.log')    # Создаем обработчик для файла
ch.setLevel(logging.INFO)   # Установим уровень отладки

strfmt = '[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s'   # Формируем формат сообщения
datefmt = '%Y-%m-%d %H:%M:%S'   # Формируем индикатор времени сообщения
formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)  # Создаем форматтер

ch.setFormatter(formatter)  # Добавляем форматтер к обработчику
logger.addHandler(ch)   # Добавляем обработчик в регистратор


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts/')
def api_all_posts():
    """ Получаем api всех постов """
    logger.info('Запрос /api/posts/')
    posts = get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:pk>')
def api_one_post(pk):
    """ Получаем api одного поста """
    logger.info(f'Запрос /api/posts/{pk}')
    post = get_post_by_pk(pk)
    return jsonify(post)



