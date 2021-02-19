import csv
import json
import requests
from xml.etree import ElementTree as et
from loguru import logger
import time
import os

# Configure logger
logger.add('collect_data_log.txt', format="{time} - {level} - {name} - {message}", level="INFO")

emails_filename = 'emails.csv'
emails = []
users = {}
get_users_url = 'https://jsonplaceholder.typicode.com/users'
get_users_posts = 'https://jsonplaceholder.typicode.com/users/{}/posts'
get_users_albums = 'https://jsonplaceholder.typicode.com/users/{}/albums'
get_users_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'


def create_xml(all_posts, all_albums, all_todos, uid, u_email):
    user = et.Element("user")
    user_id = et.SubElement(user, 'id')
    user_id.text = str(uid)
    user_email = et.SubElement(user, 'email')
    user_email.text = str(u_email)
    user_posts = et.SubElement(user, 'posts')
    user_albums = et.SubElement(user, 'albums')
    user_todos = et.SubElement(user, 'todos')

    for post in all_posts:
        new_post = et.SubElement(user_posts, 'post')
        post_id = et.SubElement(new_post, "id")
        post_id.text = str(post['id'])
        post_title = et.SubElement(new_post, "title")
        post_title.text = post['title']
        post_body = et.SubElement(new_post, "body")
        post_body.text = post['body']

    for album in all_albums:
        new_album = et.SubElement(user_albums, 'album')
        album_id = et.SubElement(new_album, "id")
        album_id.text = str(album['id'])
        album_title = et.SubElement(new_album, "title")
        album_title.text = album['title']

    for todo in all_todos:
        new_todo = et.SubElement(user_todos, 'todo')
        todo_id = et.SubElement(new_todo, "id")
        todo_id.text = str(todo['id'])
        todo_title = et.SubElement(new_todo, "title")
        todo_title.text = todo['title']
        todo_complete = et.SubElement(new_todo, "completed")
        todo_complete.text = str(todo['completed'])

    tree = et.ElementTree(user)
    try:
        logger.info('Creating new dir...')
        os.mkdir(f'.\\users\\{uid}')
    except FileExistsError:
        logger.error('Directory already exists')
        with open(f'.\\users\\{uid}\\data.xml', "wb") as fh:
            tree.write(fh, encoding='utf-8', xml_declaration=True)
            return
    except Exception as e:
        logger.error('Error while creating new dir! Error: {}', e)
        return
    with open(f'.\\users\\{uid}\\data.xml', "wb") as fh:
        tree.write(fh, encoding='utf-8', xml_declaration=True)


def collect_data(url, user_id=None):
    now = time.time()
    logger.info('Starts to collecting data from {url}', url=url.format(user_id))
    try:
        r = requests.get(url.format(user_id), verify=False)
    except Exception as e:
        logger.error('Catch error while getting data! Error {error}', error=e)
        return []
    r_data = json.loads(r.text)
    used_time = time.time() - now
    logger.info('Successfully collect all data from {url} by {time}', url=url.format(user_id), time=used_time)
    return r_data


def read_data_from_csv(filename, delimeter, quotechar):
    read_data = []
    with open(emails_filename) as f:
        logger.info('Open emails file {}', emails_filename)
        data = csv.reader(f, delimiter=',', quotechar='"')
        logger.info('Reading data...')
        for d in data:
            read_data.append(d[0])
        logger.info('Data successfully read')
        return read_data


try:
    emails = read_data_from_csv(emails_filename, ',', '"')
except Exception as e:
    logger.error('Catch error while reading data from {file}: {error}',
                 file=emails_filename, error=e)

# Make dict {id: email}
logger.info('Collecting data about users')
users_data = collect_data(get_users_url)
for user_info in users_data:
    if user_info['email'] in emails:
        users[user_info['id']] = {'email': user_info['email']}

logger.info('Start collecting data for {count} users', count=len(users))

for user_id in users:
    logger.info('Start parsing for {email}', email=users[user_id]['email'])
    user_posts = collect_data(get_users_posts, user_id)
    user_albums = collect_data(get_users_albums, user_id)
    user_todos = collect_data(get_users_todos, user_id)
    create_xml(user_posts, user_albums, user_todos, user_id, users[user_id]['email'])
