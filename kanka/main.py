import requests


class ApiError(Exception):
    pass


headers = {'Authorization': 'None', 'Accept': 'application/json'}


def error(resp):
    if resp.status_code == 401:
        if headers['Authorization'] == 'None':
            raise ApiError("You need to call login with your token first.")
        else:
            raise ApiError("You passed a wrong token. Try again :)")
        # This means you didn't login.
    elif resp.status_code != 201:
        if resp.status_code is 200 or resp.status_code is 201:
            pass
        elif resp.status_code is 204:
            return None
        else:
            # This means something went wrong.
            raise ApiError('Something went wrong. Head over to Discord if you need more help. '
                           'The error code is {}.\n{}.'.format(resp.status_code, resp.json()))
    return resp.json()


def _url(path):
    return 'https://kanka.io/api/v1' + path


def login(token):
    global headers
    headers = {
        'Authorization': 'Bearer {}'.format(token),
        'Accept': 'application/json'}


def get_campaigns():
    url = _url('/campaigns')
    return error(requests.get(url, headers=headers))


def get_campaign(campaign_id):
    url = _url('/campaigns/{}').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_campaign_users(campaign_id):
    url = _url('/campaigns/{}/users').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_calendars(campaign_id):
    url = _url('/campaigns/{}/calendars').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_calendar(campaign_id, calendar_id):
    url = _url('/campaigns/{}/calendars/{}').format(campaign_id, calendar_id)
    return error(requests.get(url, headers=headers))


# Todo, API says no :D
def create_calendar(campaign_id, name, dayname, monthname, yearname, private=None, section=None, entry=None,
                    has_leap_year=None, leap_days=None, leap_months=None, leap_repeat=None, leap_start=None,
                    image=None):
    url = _url('/campaigns/{}/calendars'.format(campaign_id))
    data = {
        'name': name,
        'month_name': monthname,
        'weekday': dayname,
        'year_name': yearname,
        'is_private': private,
        'section_id': section,
        'entry': entry,
        'has_leap_year': has_leap_year,
        'leap_year_amount': leap_days,
        'leap_year_month': leap_months,
        'leap_year_offset': leap_repeat,
        'leap_year_start': leap_start,
    }
    if image:
        files = {'image': open("{}".format(image), 'rb')}
        return error(requests.post(url, files=files, data=data, headers=headers))
    else:
        return error(requests.post(url, json=data, headers=headers))


def update_calendar(campaign_id, calender_id, name=None, dayname=None, monthname=None, yearname=None, private=None,
                    section=None, entry=None, has_leap_year=None, leap_days=None, leap_months=None, leap_repeat=None,
                    leap_start=None, image=None):
    url = _url('/campaigns/{}/calendars/{}'.format(campaign_id, calender_id))
    data = {
        'name': name,
        'month_name': monthname,
        'weekday': dayname,
        'year_name': yearname,
        'is_private': private,
        'section_id': section,
        'entry': entry,
        'has_leap_year': has_leap_year,
        'leap_year_amount': leap_days,
        'leap_year_month': leap_months,
        'leap_year_offset': leap_repeat,
        'leap_year_start': leap_start
    }
    if image:
        files = {'image': open("{}".format(image), 'rb')}
        return error(requests.post(url, files=files, data=data, headers=headers))
    else:
        return error(requests.post(url, json=data, headers=headers))


def delete_calendar(campaign_id, calender_id):
    url = _url('/campaigns/{}/calendars/{}'.format(campaign_id, calender_id))
    data = {
        'name': 'Random',
        'month_name': 'Gibberish',
        'weekday': 'Random',
        'year_name': 'Gibberish',
        'is_private': 'Random',
        'section_id': 'Gibberish',
        'entry': 'Random',
        'has_leap_year': 'Gibberish',
        'leap_year_amount': 'Random',
        'leap_year_month': 'Gibberish',
        'leap_year_offset': 'Random',
        'leap_year_start': 'Gibberish'
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_characters(campaign_id):
    url = _url('/campaigns/{}/characters').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_character(campaign_id, character_id):
    url = _url('/campaigns/{}/characters/{}').format(campaign_id, character_id)
    return error(requests.get(url, headers=headers))


def create_character(campaign_id, name, private=None, section=None, entry=None, location=None, family=None, dead=None,
                     age=None, race=None, kind=None, sex=None, image=False):
    url = _url('/campaigns/{}/characters').format(campaign_id)
    data = {
        'name': name,
        'is_private': private,
        'section_id': section,
        'entry': entry,
        'family_id': family,
        'location_id': location,
        'is_dead': dead,
        'age': age,
        'race': race,
        'type': kind,
        'sex': sex
    }
    if image:
        files = {'image': open("{}".format(image), 'rb')}
        return error(requests.post(url, files=files, data=data, headers=headers))
    else:
        return error(requests.post(url, data=data, headers=headers))


def update_character(campaign_id, character_id, name=None, private=None, section=None, entry=None, location=None,
                     family=None, dead=None, age=None, race=None, kind=None, sex=None, image=False):
    url = _url('/campaigns/{}/characters/{}').format(campaign_id, character_id)
    if name:
        data = {
            'name': name,
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'family_id': family,
            'location_id': location,
            'is_dead': dead,
            'age': age,
            'race': race,
            'type': kind,
            'sex': sex
        }
    else:
        temp = get_character(campaign_id, character_id)
        data = {
            'name': temp["data"]["name"],
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'family_id': family,
            'location_id': location,
            'is_dead': dead,
            'age': age,
            'race': race,
            'type': kind,
            'sex': sex
        }
    if image:
        files = {'image': open("{}".format(image), 'rb')}
        return error(requests.put(url, files=files, data=data, headers=headers))
    else:
        return error(requests.put(url, data=data, headers=headers))


def delete_character(campaign_id, character_id):
    url = _url('/campaigns/{}/characters/{}').format(campaign_id, character_id)
    data = {
        'name': 'Random'
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_dice_rolls(campaign_id):
    url = _url('/campaigns/{}/dice_rolls').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_dice_roll(campaign_id, roll_id):
    url = _url('/campaigns/{}/dice_rolls/{}').format(campaign_id, roll_id)
    return error(requests.get(url, headers=headers))


# Todo, API says no :D
def create_dice_roll(campaign_id, name, roll, private=None, section=None, character=None, image=None):
    url = _url('/campaigns/{}/dice_rolls').format(campaign_id)
    data = {
        'name': name,
        'parameters': roll,
        'is_private': private,
        'character_id': character,
        'section_id': section
    }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.post(url, data=data, files=image, headers=headers))
    else:
        return error(requests.post(url, data=data, headers=headers))


def update_dice_roll(campaign_id, roll_id, name=None, roll=None, private=False, section=None, character=None,
                     image=None):
    url = _url('/campaigns/{}/dice_rolls/{}').format(campaign_id, roll_id)
    if name and roll:
        data = {
            'name': name,
            'parameters': roll,
            'is_private': private,
            'character_id': character,
            'section_id': section
        }
    elif roll:
        temp = get_dice_roll(campaign_id, roll_id)
        data = {
            'name': temp["data"]["name"],
            'parameters': roll,
            'is_private': private,
            'character_id': character,
            'section_id': section
        }
    elif name:
        temp = get_dice_roll(campaign_id, roll_id)
        data = {
            'name': name,
            'parameters': temp["data"]["parameters"],
            'is_private': private,
            'character_id': character,
            'section_id': section
        }
    else:

        temp = get_dice_roll(campaign_id, roll_id)
        data = {
            'name': temp["data"]["name"],
            'parameters': temp["data"]["parameters"],
            'is_private': private,
            'character_id': character,
            'section_id': section
        }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.put(url, data=data, files=image, headers=headers))
    else:
        return error(requests.put(url, json=data, headers=headers))


def delete_dice_roll(campaign_id, roll_id):
    url = _url('/campaigns/{}/dice_rolls/{}').format(campaign_id, roll_id)
    data = {
        'name': 'random',
        'parameters': 'gibberish',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_events(campaign_id):
    url = _url('/campaigns/{}/events').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_event(campaign_id, event_id):
    url = _url('/campaigns/{}/events/{}').format(campaign_id, event_id)
    return error(requests.get(url, headers=headers))


def create_event(campaign_id, name, date=None, private=None, section=None, entry=None, location=None, kind=None,
                 image=None):
    url = _url('/campaigns/{}/events').format(campaign_id)
    data = {
        'name': name,
        'date': date,
        'is_private': private,
        'section_id': section,
        'entry': entry,
        'location_id': location,
        'type': kind
    }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.post(url, data=data, files=image, headers=headers))
    else:
        return error(requests.post(url, data=data, headers=headers))


def update_event(campaign_id, event_id, name=None, date=None, private=None, section=None, entry=None, location=None,
                 kind=None, image=None):
    url = _url('/campaigns/{}/events/{}').format(campaign_id, event_id)
    if name:
        data = {
            'name': name,
            'date': date,
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'location_id': location,
            'type': kind
        }
    else:
        temp = get_event(campaign_id, event_id)
        data = {
            'name': temp["data"]["name"],
            'date': date,
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'location_id': location,
            'type': kind
        }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.put(url, data=data, files=image, headers=headers))
    else:
        return error(requests.put(url, json=data, headers=headers))


def delete_event(campaign_id, event_id):
    url = _url('/campaigns/{}/events/{}').format(campaign_id, event_id)
    data = {
        'name': 'random',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_families(campaign_id):
    url = _url('/campaigns/{}/families').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_family(campaign_id, family_id):
    url = _url('/campaigns/{}/families/{}').format(campaign_id, family_id)
    return error(requests.get(url, headers=headers))


def create_family(campaign_id, name, private=None, section=None, entry=None, location=None,
                  image=None):
    url = _url('/campaigns/{}/families').format(campaign_id)
    data = {
        'name': name,
        'is_private': private,
        'section_id': section,
        'entry': entry,
        'location_id': location,
    }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.post(url, data=data, files=image, headers=headers))
    else:
        return error(requests.post(url, data=data, headers=headers))


def update_family(campaign_id, family_id, name=None, private=None, section=None, entry=None, location=None,
                  image=None):
    url = _url('/campaigns/{}/families/{}').format(campaign_id, family_id)
    if name:
        data = {
            'name': name,
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'location_id': location,
        }
    else:
        temp = get_family(campaign_id, family_id)
        data = {
            'name': temp["data"]["name"],
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'location_id': location,
        }

    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.put(url, data=data, files=image, headers=headers))
    else:
        return error(requests.put(url, json=data, headers=headers))


def delete_family(campaign_id, family_id):
    url = _url('/campaigns/{}/families/{}').format(campaign_id, family_id)
    data = {
        'name': 'random',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_items(campaign_id):
    url = _url('/campaigns/{}/items').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_item(campaign_id, item_id):
    url = _url('/campaigns/{}/items/{}').format(campaign_id, item_id)
    return error(requests.get(url, headers=headers))


def create_item(campaign_id, name, private=None, section=None, entry=None, location=None, kind=None, character=None,
                image=None):
    url = _url('/campaigns/{}/items').format(campaign_id)
    data = {
        'name': name,
        'is_private': private,
        'section_id': section,
        'entry': entry,
        'location_id': location,
        'character_id': character,
        'type': kind
    }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.post(url, data=data, files=image, headers=headers))
    else:
        return error(requests.post(url, data=data, headers=headers))


def update_item(campaign_id, item_id, name=None, private=None, section=None, entry=None, location=None, kind=None,
                character=None, image=None):
    url = _url('/campaigns/{}/items/{}').format(campaign_id, item_id)
    if name:
        data = {
            'name': name,
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'location_id': location,
            'character_id': character,
            'type': kind
        }
    else:
        temp = get_item(campaign_id, item_id)
        data = {
            'name': temp["data"]["name"],
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'location_id': location,
            'character_id': character,
            'type': kind
        }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.put(url, data=data, files=image, headers=headers))
    else:
        return error(requests.put(url, data=data, headers=headers))


def delete_item(campaign_id, item_id):
    url = _url('/campaigns/{}/items/{}').format(campaign_id, item_id)
    data = {
        'name': 'random',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_journals(campaign_id):
    url = _url('/campaigns/{}/journals').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_journal(campaign_id, journal_id):
    url = _url('/campaigns/{}/journals/{}').format(campaign_id, journal_id)
    return error(requests.get(url, headers=headers))


def create_journal(campaign_id, name, private=None, section=None, entry=None, kind=None, character=None,
                   image=None):
    url = _url('/campaigns/{}/journals').format(campaign_id)
    data = {
        'name': name,
        'is_private': private,
        'section_id': section,
        'entry': entry,
        'character_id': character,
        'type': kind
    }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.post(url, data=data, files=image, headers=headers))
    else:
        return error(requests.post(url, data=data, headers=headers))


def update_journal(campaign_id, journal_id, name=None, private=None, section=None, entry=None, kind=None,
                   character=None, image=None):
    url = _url('/campaigns/{}/journals/{}').format(campaign_id, journal_id)
    if name:
        data = {
            'name': name,
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'character_id': character,
            'type': kind
        }
    else:
        temp = get_journal(campaign_id, journal_id)
        data = {
            'name': temp["data"]["name"],
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'character_id': character,
            'type': kind
        }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.put(url, data=data, files=image, headers=headers))
    else:
        return error(requests.put(url, data=data, headers=headers))


def delete_journal(campaign_id, journal_id):
    url = _url('/campaigns/{}/journals/{}').format(campaign_id, journal_id)
    data = {
        'name': 'random',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_locations(campaign_id):
    url = _url('/campaigns/{}/locations').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_location(campaign_id, location_id):
    url = _url('/campaigns/{}/locations/{}').format(campaign_id, location_id)
    return error(requests.get(url, headers=headers))


def create_location(campaign_id, name, private=None, section=None, entry=None, kind=None, parent_location=None,
                    image=None):
    url = _url('/campaigns/{}/locations').format(campaign_id)
    data = {
        'name': name,
        'is_private': private,
        'section_id': section,
        'entry': entry,
        'parent_location': parent_location,
        'type': kind
    }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.post(url, data=data, files=image, headers=headers))
    else:
        return error(requests.post(url, data=data, headers=headers))


def update_location(campaign_id, location_id, name=None, private=None, section=None, entry=None, kind=None,
                    parent_location=None, image=None):
    url = _url('/campaigns/{}/locations/{}').format(campaign_id, location_id)
    if name:
        data = {
            'name': name,
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'parent_location': parent_location,
            'type': kind
        }
    else:
        temp = get_location(campaign_id, location_id)
        data = {
            'name': temp["data"]["name"],
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'parent_location': parent_location,
            'type': kind
        }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.put(url, data=data, files=image, headers=headers))
    else:
        return error(requests.put(url, data=data, headers=headers))


def delete_location(campaign_id, location_id):
    url = _url('/campaigns/{}/locations/{}').format(campaign_id, location_id)
    data = {
        'name': 'random',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_map_points(campaign_id, location_id):
    url = _url('/campaigns/{}/locations/{}/map_points').format(campaign_id, location_id)
    return error(requests.get(url, headers=headers))


# Todo, API says no :D
def create_map_points(campaign_id, location_id, axis_x, axis_y, colour, name=None):
    url = _url('/campaigns/{}/locations/{}/map_points').format(campaign_id, location_id)
    if name:
        data = {
            'axis_x': axis_x,
            'axis_y': axis_y,
            'name': location_id,
            'colour': colour,
        }
    else:
        data = {
            'axis_x': axis_x,
            'axis_y': axis_y,
            'target_id': location_id,
            'colour': colour,
        }
    return error(requests.post(url, data=data, headers=headers))


def get_organisations(campaign_id):
    url = _url('/campaigns/{}/organisations').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_organisation(campaign_id, organisation_id):
    url = _url('/campaigns/{}/organisations/{}').format(campaign_id, organisation_id)
    return error(requests.get(url, headers=headers))


def create_organisation(campaign_id, name, private=None, section=None, entry=None, kind=None, location=None,
                        image=None):
    url = _url('/campaigns/{}/organisations').format(campaign_id)
    data = {
        'name': name,
        'is_private': private,
        'section_id': section,
        'entry': entry,
        'location_id': location,
        'type': kind
    }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.post(url, data=data, files=image, headers=headers))
    else:
        return error(requests.post(url, data=data, headers=headers))


def update_organisation(campaign_id, organisation_id, name=None, private=None, section=None, entry=None, kind=None,
                        location=None, image=None):
    url = _url('/campaigns/{}/organisations/{}').format(campaign_id, organisation_id)
    if name:
        data = {
            'name': name,
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'location_id': location,
            'type': kind
        }
    else:
        temp = get_organisation(campaign_id, organisation_id)
        data = {
            'name': temp["data"]["name"],
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'location_id': location,
            'type': kind
        }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.put(url, data=data, files=image, headers=headers))
    else:
        return error(requests.put(url, data=data, headers=headers))


def delete_organisation(campaign_id, organisation_id):
    url = _url('/campaigns/{}/organisations/{}').format(campaign_id, organisation_id)
    data = {
        'name': 'random',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_organisation_members(campaign_id, organisation_id):
    url = _url('/campaigns/{}/organisations/{}/organisation_members').format(campaign_id, organisation_id)
    return error(requests.get(url, headers=headers))


def get_organisation_member(campaign_id, organisation_id, member_id):
    url = _url('/campaigns/{}/organisations/{}/organisation_members/{}').format(campaign_id, organisation_id, member_id)
    return error(requests.get(url, headers=headers))


def create_organisation_member(campaign_id, organisation_id, character_id, role, private=None):
    url = _url('/campaigns/{}/organisations/{}/organisation_members').format(campaign_id, organisation_id)
    data = {
        'organisation_id': organisation_id,
        'character_id': character_id,
        'role': role,
        'is_private': private,
    }
    return error(requests.post(url, data=data, headers=headers))


def update_organisation_member(campaign_id, organisation_id, member_id, character_id=None, role=None, private=None):
    url = _url('/campaigns/{}/organisations/{}/organisation_members/{}').format(campaign_id, organisation_id, member_id)
    if character_id:
        data = {
            'organisation_id': organisation_id,
            'character_id': character_id,
            'role': role,
            'is_private': private,
        }
    else:
        temp = get_organisation_member(campaign_id, organisation_id, member_id)
        data = {
            'organisation_id': organisation_id,
            'character_id': temp["data"]["character_id"],
            'role': role,
            'is_private': private,
        }
    return error(requests.put(url, data=data, headers=headers))


def delete_organisation_member(campaign_id, organisation_id, member_id):
    url = _url('/campaigns/{}/organisations/{}/organisation_members/{}').format(campaign_id, organisation_id, member_id)
    data = {
        'organisation_id': 'Random',
        'character_id': 'Gibberish',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_quests(campaign_id):
    url = _url('/campaigns/{}/quests').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_quest(campaign_id, quest_id):
    url = _url('/campaigns/{}/quests/{}').format(campaign_id, quest_id)
    return error(requests.get(url, headers=headers))


def create_quest(campaign_id, name, private=None, section=None, character=None, entry=None, kind=None, completed=None,
                 parent_quest=None, image=None):
    url = _url('/campaigns/{}/organisations').format(campaign_id)
    data = {
        'name': name,
        'is_private': private,
        'section_id': section,
        'entry': entry,
        'character_id': character,
        'is_completed': completed,
        'quest_id': parent_quest,
        'type': kind
    }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.post(url, data=data, files=image, headers=headers))
    else:
        return error(requests.post(url, data=data, headers=headers))


def update_quest(campaign_id, quest_id, name=None, private=None, section=None, character=None, entry=None, kind=None,
                 completed=None, parent_quest=None, image=None):
    url = _url('/campaigns/{}/quests/{}').format(campaign_id, quest_id)
    if name:
        data = {
            'name': name,
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'character_id': character,
            'is_completed': completed,
            'quest_id': parent_quest,
            'type': kind
        }
    else:
        temp = get_quest(campaign_id, quest_id)
        data = {
            'name': temp["data"]["name"],
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'character_id': character,
            'is_completed': completed,
            'quest_id': parent_quest,
            'type': kind
        }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.put(url, data=data, files=image, headers=headers))
    else:
        return error(requests.put(url, data=data, headers=headers))


def delete_quest(campaign_id, quest_id):
    url = _url('/campaigns/{}/quests/{}').format(campaign_id, quest_id)
    data = {
        'name': 'random',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_quest_members(campaign_id, quest_id):
    url = _url('/campaigns/{}/quests/{}/quest_characters').format(campaign_id, quest_id)
    return error(requests.get(url, headers=headers))


def get_quest_member(campaign_id, quest_id, member_id):
    url = _url('/campaigns/{}/quests/quest_characters/{}').format(campaign_id, quest_id, member_id)
    return error(requests.get(url, headers=headers))


def create_quest_member(campaign_id, quest_id, character, description=None, private=None):
    url = _url('/campaigns/{}/quests/{}/quest_characters').format(campaign_id, quest_id)
    data = {
        'character_id': character,
        'is_private': private,
        'description': description
    }
    return error(requests.post(url, data=data, headers=headers))


def update_quest_member(campaign_id, quest_id, member_id, character=None, description=None, private=None):
    url = _url('/campaigns/{}/quests/{}/quest_characters/{}').format(campaign_id, quest_id, member_id)
    if character:
        data = {
            'character_id': character,
            'is_private': private,
            'description': description
        }
    else:
        temp = get_quest_member(campaign_id, quest_id, member_id)
        data = {
            'character_id': temp["data"]["character_id"],
            'is_private': private,
            'description': description
        }
    return error(requests.put(url, data=data, headers=headers))


def delete_quest_member(campaign_id, quest_id, member_id):
    url = _url('/campaigns/{}/quests/{}/quest_characters/{}').format(campaign_id, quest_id, member_id)
    data = {
        'character_id': 'random',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_quest_locations(campaign_id, quest_id):
    url = _url('/campaigns/{}/quests/{}/quest_locations').format(campaign_id, quest_id)
    return error(requests.get(url, headers=headers))


def get_quest_location(campaign_id, quest_id, location_id):
    url = _url('/campaigns/{}/quests/{}/quest_locations/{}').format(campaign_id, quest_id, location_id)
    return error(requests.get(url, headers=headers))


def create_quest_location(campaign_id, quest_id, location, description=None, private=None):
    url = _url('/campaigns/{}/quests/{}/quest_characters').format(campaign_id, quest_id)
    data = {
        'location_id': location,
        'is_private': private,
        'description': description
    }
    return error(requests.post(url, data=data, headers=headers))


def update_quest_location(campaign_id, quest_id, location_id, location=None, description=None, private=None):
    url = _url('/campaigns/{}/quests/{}/quest_characters/{}').format(campaign_id, quest_id, location_id)
    if location:
        data = {
            'location_id': location,
            'is_private': private,
            'description': description
        }
    else:
        temp = get_quest_member(campaign_id, quest_id, location_id)
        data = {
            'location_id': temp["data"]["location_id"],
            'is_private': private,
            'description': description
        }
    return error(requests.put(url, data=data, headers=headers))


def delete_quest_location(campaign_id, quest_id, location_id):
    url = _url('/campaigns/{}/quests/{}/quest_characters/{}').format(campaign_id, quest_id, location_id)
    data = {
        'location_id': 'random',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_sections(campaign_id):
    url = _url('/campaigns/{}/sections').format(campaign_id)
    return error(requests.get(url, headers=headers))


def get_section(campaign_id, section_id):
    url = _url('/campaigns/{}/sections/{}').format(campaign_id, section_id)
    return error(requests.get(url, headers=headers))


def create_section(campaign_id, name, private=None, section=None, entry=None, kind=None, character=None,
                   image=None):
    url = _url('/campaigns/{}/journals').format(campaign_id)
    data = {
        'name': name,
        'is_private': private,
        'section_id': section,
        'entry': entry,
        'character_id': character,
        'type': kind
    }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.post(url, data=data, files=image, headers=headers))
    else:
        return error(requests.post(url, data=data, headers=headers))


def update_section(campaign_id, section_id, name=None, private=None, section=None, entry=None, kind=None,
                   character=None, image=None):
    url = _url('/campaigns/{}/sections/{}').format(campaign_id, section_id)
    if name:
        data = {
            'name': name,
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'character_id': character,
            'type': kind
        }
    else:
        temp = get_section(campaign_id, section_id)
        data = {
            'name': temp["data"]["name"],
            'is_private': private,
            'section_id': section,
            'entry': entry,
            'character_id': character,
            'type': kind
        }
    if image:
        image = {'picture': open('{}'.format(image), 'rb')}
        return error(requests.put(url, data=data, files=image, headers=headers))
    else:
        return error(requests.put(url, data=data, headers=headers))


def delete_section(campaign_id, section_id):
    url = _url('/campaigns/{}/sections/{}').format(campaign_id, section_id)
    data = {
        'name': 'random',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_entity_attributes(campaign_id, entity_id):
    url = _url('/campaigns/{}/entities/{}/attributes').format(campaign_id, entity_id)
    return error(requests.get(url, headers=headers))


def get_entity_attribute(campaign_id, entity_id, attribute_id):
    url = _url('/campaigns/{}/entities/{}/attributes/{}').format(campaign_id, entity_id, attribute_id)
    return error(requests.get(url, headers=headers))


def create_entity_attribute(campaign_id, entity_id, name, value=None, default_order=None, private=None):
    url = _url('/campaigns/{}/entities/{}/attributes').format(campaign_id, entity_id)
    data = {
        'entity_id': entity_id,
        'name': name,
        'value': value,
        'default_order': default_order,
        'is_private': private
    }
    return error(requests.post(url, data=data, headers=headers))


def update_entity_attribute(campaign_id, entity_id, attribute_id, name=None, value=None, default_order=None,
                            private=None):
    url = _url('/campaigns/{}/entities/{}/attributes/{}').format(campaign_id, entity_id, attribute_id)
    if name:
        data = {
            'entity_id': entity_id,
            'name': name,
            'value': value,
            'default_order': default_order,
            'is_private': private
        }
    else:
        temp = get_entity_attribute(campaign_id, entity_id, attribute_id)
        data = {
            'entity_id': entity_id,
            'name': temp["data"]["name"],
            'value': value,
            'default_order': default_order,
            'is_private': private
        }
    return error(requests.post(url, data=data, headers=headers))


def delete_entity_attribute(campaign_id, entity_id, attribute_id):
    url = _url('/campaigns/{}/entities/{}/attributes/{}').format(campaign_id, entity_id, attribute_id)
    data = {
        'name': 'random',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_entity_notes(campaign_id, entity_id):
    url = _url('/campaigns/{}/entities/{}/entity_notes').format(campaign_id, entity_id)
    return error(requests.get(url, headers=headers))


def get_entity_note(campaign_id, entity_id, entity_note_id):
    url = _url('/campaigns/{}/entities/{}/entity_notes/{}').format(campaign_id, entity_id, entity_note_id)
    return error(requests.get(url, headers=headers))


def create_entity_note(campaign_id, entity_id, name, entry=None, private=None):
    url = _url('/campaigns/{}/entities/{}/entity_notes').format(campaign_id, entity_id)
    data = {
        'entity_id': entity_id,
        'name': name,
        'entry': entry,
        'is_private': private
    }
    return error(requests.post(url, data=data, headers=headers))


def update_entity_note(campaign_id, entity_id, entity_note_id, name=None, entry=None, private=None):
    url = _url('/campaigns/{}/entities/{}/entity_notes/{}').format(campaign_id, entity_id, entity_note_id)
    if name:
        data = {
            'entity_id': entity_id,
            'name': name,
            'entry': entry,
            'is_private': private
        }
    else:
        temp = get_entity_note(campaign_id, entity_id, entity_note_id)
        data = {
            'entity_id': entity_id,
            'name': temp["data"]["name"],
            'entry': entry,
            'is_private': private
        }
    return error(requests.post(url, data=data, headers=headers))


def delete_entity_note(campaign_id, entity_id, entity_note_id):
    url = _url('/campaigns/{}/entities/{}/entity_notes/{}').format(campaign_id, entity_id, entity_note_id)
    data = {
        'name': 'random',
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_entity_events(campaign_id, entity_id):
    url = _url('/campaigns/{}/entities/{}/entity_events').format(campaign_id, entity_id)
    return error(requests.get(url, headers=headers))


def get_entity_event(campaign_id, entity_id, entity_event_id):
    url = _url('/campaigns/{}/entities/{}/entity_events/{}').format(campaign_id, entity_id, entity_event_id)
    return error(requests.get(url, headers=headers))


# Todo, API says no :D
def create_entity_event(campaign_id, entity_id, name, date, length, entry=None, default_order=None, private=None):
    url = _url('/campaigns/{}/entities/{}/entity_events').format(campaign_id, entity_id)
    data = {
        'entity_id': entity_id,
        'name': name,
        'date': date,
        'length': length,
        'entry': entry,
        'default_order': default_order,
        'is_private': private
    }
    return error(requests.post(url, data=data, headers=headers))


def delete_entity_event(campaign_id, entity_id, entity_event_id):
    url = _url('/campaigns/{}/entities/{}/entity_events/{}').format(campaign_id, entity_id, entity_event_id)
    data = {
        'name': 'random',
        'date': 'gibberish',
        'length': '1'
    }
    return error(requests.delete(url, json=data, headers=headers))


def get_entity_relations(campaign_id, entity_id):
    url = _url('/campaigns/{}/entities/{}/relations').format(campaign_id, entity_id)
    return error(requests.get(url, headers=headers))


def get_entity_relation(campaign_id, entity_id, relation_id):
    url = _url('/campaigns/{}/entities/{}/relations/{}').format(campaign_id, entity_id, relation_id)
    return error(requests.get(url, headers=headers))


def create_entity_relation(campaign_id, entity_id, owner_id, target_id, relation, private=None, ):
    url = _url('/campaigns/{}/entities/{}/relations').format(campaign_id, entity_id)
    data = {
        "owner_id": owner_id,
        "target_id": target_id,
        "relation": relation,
        'is_private': private
    }
    return error(requests.post(url, data=data, headers=headers))


def update_entity_relation(campaign_id, entity_id, relation_id, owner_id=None, target_id=None, relation=None,
                           private=None):
    url = _url('/campaigns/{}/entities/{}/relations/{}').format(campaign_id, entity_id, relation_id)
    if owner_id and target_id and relation:
        data = {
            "owner_id": owner_id,
            "target_id": target_id,
            "relation": relation,
            'is_private': private
        }
    elif owner_id and target_id:
        temp = get_entity_relation(campaign_id, entity_id, relation_id)
        data = {
            "owner_id": owner_id,
            "target_id": target_id,
            "relation": temp["data"]["relation"],
            'is_private': private
        }
    elif owner_id and relation:
        temp = get_entity_relation(campaign_id, entity_id, relation_id)
        data = {
            "owner_id": owner_id,
            "target_id": temp["data"]["target_id"],
            "relation": relation,
            'is_private': private
        }
    elif target_id and relation:
        temp = get_entity_relation(campaign_id, entity_id, relation_id)
        data = {
            "owner_id": temp["data"]["owner_id"],
            "target_id": target_id,
            "relation": relation,
            'is_private': private
        }
    elif owner_id:
        temp = get_entity_relation(campaign_id, entity_id, relation_id)
        data = {
            "owner_id": owner_id,
            "target_id": temp["data"]["target_id"],
            "relation": temp["data"]["relation"],
            'is_private': private
        }
    elif target_id:
        temp = get_entity_relation(campaign_id, entity_id, relation_id)
        data = {
            "owner_id": temp["data"]["owner_id"],
            "target_id": target_id,
            "relation": temp["data"]["relation"],
            'is_private': private
        }
    elif relation:
        temp = get_entity_relation(campaign_id, entity_id, relation_id)
        data = {
            "owner_id": temp["data"]["owner_id"],
            "target_id": temp["data"]["target_id"],
            "relation": relation,
            'is_private': private
        }
    else:
        temp = get_entity_relation(campaign_id, entity_id, relation_id)
        data = {
            "owner_id": temp["data"]["owner_id"],
            "target_id": temp["data"]["target_id"],
            "relation": temp["data"]["relation"],
            'is_private': private
        }
    return error(requests.post(url, data=data, headers=headers))
