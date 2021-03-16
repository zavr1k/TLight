import requests
from django.shortcuts import render, redirect

from .models import Post, User, Company, Address

USER_DATA = 'http://jsonplaceholder.typicode.com/users'
POST_DATA = 'http://jsonplaceholder.typicode.com/posts'


def get_data(url):
    return requests.get(url)


def load_users(data):
    users = get_data(data).json()
    for user in users:
        address = Address()
        address.city = user['address']['city']
        address.street = user['address']['street']
        address.suite = user['address']['suite']
        address.zipcode = user['address']['zipcode']
        address.lat = user['address']['geo']['lat']
        address.lng = user['address']['geo']['lng']
        address.save()

        company = Company()
        company.name = user['company']['name']
        company.catchPhrase = user['company']['catchPhrase']
        company.bs = user['company']['bs']
        company.save()

        u = User()
        u.id = user['id']
        u.name = user['name']
        u.username = user['username']
        u.email = user['email']
        u.address = address
        u.phone = user['phone']
        u.website = user['website']
        u.company = company
        u.save()


def load_posts(data):
    posts = get_data(data).json()
    for post in posts:
        p = Post()
        p.user_id = User.objects.get(id=post['userId'])
        p.title = post['title']
        p.body = post['body']
        p.save()


def load_data(request):
    load_users(USER_DATA)
    load_posts(POST_DATA)
    return redirect('/')


def drop_data(request):
    User.objects.all().delete()
    Address.objects.all().delete()
    Company.objects.all().delete()
    Post.objects.all().delete()
    return redirect('/')


def index(request):
    posts = Post.objects.select_related('user_id').\
        only('user_id__name', 'title', 'body')
    return render(request, 'index.html', {'posts': posts})
