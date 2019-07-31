import requests
import json
from datetime import datetime as _datetime
from kanka.error import APIError, Unauthorized
import os

headers = {'Authorization': 'None', 'Accept': 'application/json'}
sync = False


def login(token, sync_enable=False):
    global headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'}
    if sync_enable:
        global sync
        sync = True


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
                           'The error code is {}.\n{}.'.format(resp.status_code, resp.text))
    return resp.json()


def _url(path):
    return 'https://kanka.io/api/1.0/' + path


def _get(endpoint, params=None):
    if params is None:
        params = {}
    url = _url(endpoint)
    if sync:
        params["lastSync"] = _synchronisation(endpoint)
    return _work_with_response(requests.get(url, headers=headers, params=params))


def _post(endpoint, params, files):
    url = _url(endpoint)
    for key, value in list(params.items()):
        if isinstance(value, bool):
            if value:
                params[key] = 1
            else:
                params[key] = 0
        elif value is None:
            del params[key]
    return _work_with_response(requests.post(url, headers=headers, json=params, files=files))


def _synchronisation(path):
    time = _datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        db = json.load(open(f"{dir_path}/sync.json"))
    except FileNotFoundError:
        # first time using any method
        db = {}
    try:
        last_time = db[path]
        db[path] = time
    except KeyError:
        # first time using this method
        db[path] = time
        last_time = ""
    with open(f"{dir_path}/sync.json", "w") as outfile:
        json.dump(db, outfile, indent=4, sort_keys=True)
    return last_time
