from django.shortcuts import render
from django.http import HttpRequest
import requests
from requests.exceptions import HTTPError


def index(request):
    assert isinstance(request, HttpRequest)
    data_list = []
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/todos/')
        data_list = response.json()
        print(data_list)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')

    return render(
        request,
        'index.html',
        {
            'title': 'Home Page',
            'message': 'Hello world!',
            'data_list': data_list,
        }
    )