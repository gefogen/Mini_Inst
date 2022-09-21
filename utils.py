from config1 import *
import json


def load_content_from_json_data():
    """ Загружаем json_data """
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        content_posts = json.load(file)
        return content_posts


def load_content_from_json_comments():
    """ Загружаем json_comments """
    with open(COMMENTS_PATH, "r", encoding="utf-8") as file:
        comments_post = json.load(file)
        return comments_post


def get_all_bookmarks():
    """ Возвращает все закладки """
    with open(BOOKMARKS_PATH, "r", encoding="utf-8") as file:
        bookmarks_content = json.load(file)
        return bookmarks_content


def get_posts_all():
    """ Выводит все посты """
    content_posts = load_content_from_json_data()
    posts = []
    for post in content_posts:
        posts.append(post)
    return posts


def get_posts_by_user_name(user_name):
    """ Поиск постов по имени """
    content_posts = load_content_from_json_data()
    posts = []
    for post in content_posts:
        if user_name.lower() in post['poster_name']:
            posts.append(post)
    return posts


def search_by_text(content):
    """ Ищем соответствия по тексту """
    if content in (" ", ""):
        return []
    content_posts = load_content_from_json_data()
    posts = []
    for post in content_posts:
        if content.lower() in post['content'].lower():
            posts.append(post)
    return posts


def get_post_by_pk(pk):
    """ Поиск пользователя по pk """
    content_posts = load_content_from_json_data()
    for post in content_posts:
        if post['pk'] == pk:
            return post


def get_comments_by_post_id(post_id):
    """ Поиск комментариев к посту """

    current_comments = []

    for post in load_content_from_json_comments():
        if post["post_id"] == post_id:
            current_comments.append(post)
    return current_comments


def add_bookmark(content):
    """ Добавляем закладку """
    bookmarks_content = get_all_bookmarks()
    bookmarks_content.append(content)

    with open(BOOKMARKS_PATH, 'w+', encoding='utf-8') as file:
        json.dump(bookmarks_content, file, ensure_ascii=False, indent=4)


def delete_bookmark(content):
    """ Удаляем закладку """
    bookmarks_content = get_all_bookmarks()
    bookmarks_content.remove(content)

    with open(BOOKMARKS_PATH, 'w+', encoding='utf-8') as file:
        json.dump(bookmarks_content, file, ensure_ascii=False, indent=4)


def marking_tag(text):
    """ Возвращаем слова-ссылки """

    tags = []

    for word in text.split():
        if word.startswith("#"): # если начинается с "#"
            tags.append(word.strip("#")) # добавляем в список тегов слово с убранным #

    tags = sorted(tags, reverse=True)
    result_text = text

    for tag in tags:
            result_text = result_text.replace(f"#{tag}", f'<a class="item__tag" href="/tag/{tag}"><[heshteg]>{tag}</a>')
    return result_text.replace("<[heshteg]>", "#")



