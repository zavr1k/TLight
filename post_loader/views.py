import requests
from django.shortcuts import render, redirect
from . import models


USER_DATA = 'http://jsonplaceholder.typicode.com/users'
POST_DATA = 'http://jsonplaceholder.typicode.com/posts'


def get_data(url):
    return requests.get(url)


def load_users(data):
    users = get_data(data).json()
    for user in users:
        address = models.Address()
        address.city = user['address']['city']
        address.street = user['address']['street']
        address.suite = user['address']['suite']
        address.zipcode = user['address']['zipcode']
        address.lat = user['address']['geo']['lat']
        address.lng = user['address']['geo']['lng']
        address.save()

        company = models.Company()
        company.name = user['company']['name']
        company.catchPhrase = user['company']['catchPhrase']
        company.bs = user['company']['bs']
        company.save()

        u = models.User()
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
        p = models.Post()
        p.user_id = models.User.objects.get(id=post['userId'])
        p.title = post['title']
        p.body = post['body']
        p.save()


def load_data(request):
    load_users(USER_DATA)
    load_posts(POST_DATA)
    return redirect('/')


def drop_data(request):
    models.User.objects.all().delete()
    models.Address.objects.all().delete()
    models.Company.objects.all().delete()
    models.Post.objects.all().delete()
    return redirect('/')


def index(request):
    posts = models.Post.objects.select_related('user_id').only('user_id__name', 'title', 'body')
    return render(request, 'index.html', {'posts': posts})
