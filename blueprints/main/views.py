from flask import Blueprint, render_template, request, redirect
from utils import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")


@main_blueprint.route("/")
def page_index():
    """ Отображение главной страницы """
    posts = get_posts_all()  # Получаем все посты
    return render_template("index.html",
                           posts=posts)


@main_blueprint.route("/search")
def page_post():
    """ Поиск поста по тексту """
    content = request.args.get("content", "")  # Получаем тег по строковому вводу
    posts = search_by_text(content)  # Получаем результат функции
    return render_template("search.html",
                           content=content,
                           posts=posts,
                           quantity=len(posts))


@main_blueprint.route("/post/<int:pk>")
def page_post_by_pk(pk):
    """ Поиск поста по идентификатору """
    post = get_post_by_pk(pk)  # Получаем пост по pk
    comments = get_comments_by_post_id(pk)  # Получаем комментарии к посту
    post["content"] = marking_tag(post["content"])
    return render_template("post.html",
                           post=post,
                           comments=comments,
                           quantity_comments=len(comments))


@main_blueprint.route("/users/<user_name>")
def page_user(user_name):
    """ Поиск постов по имени """
    posts = get_posts_by_user_name(user_name)  # Получаем посты по имени
    return render_template("user-feed.html",
                           posts=posts,
                           user_name=user_name)


@main_blueprint.route("/tag/<tagname>")
def page_tag(tagname):
    """ Вывод поиска по тегу """
    posts = search_by_text("#"+tagname)
    return render_template("tag.html",
                           posts=posts,
                           tagname=tagname)


@main_blueprint.route("/bookmarks/")
def page_bookmarks():
    """ Страница закладок """
    posts = get_all_bookmarks()
    return render_template("bookmarks.html",
                           posts=posts)


@main_blueprint.route("/bookmarks/add/<int:pk>")
def page_add_bookmark(pk):
    """ Добавление закладки """
    post = get_post_by_pk(pk)
    add_bookmark(post)  # Добавляем пост в закладки
    return redirect("/", code=302)  # Переадресация на главную


@main_blueprint.route("/bookmarks/remove/<int:pk>")
def page_delete_bookmark(pk):
    """ Удаление закладки """
    post = get_post_by_pk(pk)
    delete_bookmark(post)   # Удаляем пост из закладок
    return redirect("/", code=302)  # Переадресация на главную
