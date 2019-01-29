from django.shortcuts import render
import requests


def index(request):
    context = None
    user = request.user
    try:
        social = user.social_auth.get(provider='vk-oauth2')
        friends_request_params = {
            'client_id': '6829253',
            'grant_type': 'client_credentials',
            'client_secret': 'eGJBUDb5aCaHky1hZiZC',
            'access_token': social.extra_data['access_token'],
            'v': 5.92,
            'count': 5,
            'order': 'name',
            'fields': 'first_name'
        }
        response = requests.get('https://api.vk.com/method/friends.get',
                                params=friends_request_params)
        friends = response.json()
        print(friends)
        id_username = {}
        for friend in friends:
            username = str(friend['first_name'] + ' ' + friend['last_name'])
            url = 'https://vk.com/id' + str(friend['id'])
            id_username[url] = username
        context = {'id_username': id_username}
    except AttributeError:
        pass
    return render(request, 'oauth/index.html', context)
