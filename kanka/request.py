import requests
from kanka.error import APIError, Unauthorized

headers = {'Authorization': 'None', 'Accept': 'application/json'}


def login(token):
    global headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'}


def _work_with_response(resp):
    if resp.status_code == 401:
        if headers['Authorization'] == 'None':
            raise Unauthorized("You need to call login with your token first.")
        else:
            raise Unauthorized("You passed a wrong token or made a typo somewhere. Try again :)")
        # This means you didn't login.
    elif resp.status_code != 201:
        if resp.status_code is 200 or resp.status_code is 201:
            pass
        elif resp.status_code is 204:
            return None
        else:
            # This means something went wrong.
            raise APIError('Something went wrong. Head over to Discord if you need more help. '
                           'The error code is {}.\n{}.'.format(resp.status_code, resp.json()))
    return resp.json()


def _url(path):
    return 'https://kanka.io/api/1.0/' + path


def _get(endpoint):
    url = _url(endpoint)
    return _work_with_response(requests.get(url, headers=headers))
