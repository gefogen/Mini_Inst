import pytest
from app import app


def test_api_all_posts():
    """ Тестируем """
    resp = app.test_client().get('/api/posts', follow_redirects=True)
    assert resp.status_code == 200, "Статус код (/api/posts) не верный"
    assert type(resp.json) == list, "Это не список!"


def test_api_post_keys_names():
    """ Тестируем количество ключей и их имен """
    posts_keys_names = {"poster_name", "poster_avatar",
                        "pic", "content", "views_count",
                        "likes_count", "pk"}
    resp = app.test_client().get('/api/posts/1', follow_redirects=True)

    assert len(resp.json.keys()) == len(posts_keys_names), "Ошибка в кол-ве ключей"
    assert set(resp.json.keys()) == posts_keys_names, "Ошибка в названии ключей!"


def test_api_one_post():
    """ Тестируем один пост """
    resp = app.test_client().get('/api/posts/1', follow_redirects=True)
    assert resp.status_code == 200, "Статус код (/api/posts/1) не верный"
    assert type(resp.json) == dict, "Это не словарь!"