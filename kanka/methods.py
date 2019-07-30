from kanka.objects import (User as _User, Campaign as _Campaign, Campaigns as _Campaigns, Members as _Members,
                           Character as _Character)
from kanka.request import _get, _post


def get_user():
    # no sync attribute here (yet?)
    profile = _get("profile")["data"]
    return _User(user_id=profile["id"], name=profile["name"], avatar=profile["avatar"],
                 avatar_thumb=profile["avatar_thumb"], locale=profile["locale"], timezone=profile["timezone"],
                 date_format=profile["date_format"], default_pagination=profile["default_pagination"],
                 last_campaign_id=profile["last_campaign_id"], is_patreon=profile["is_patreon"])


def get_campaigns():
    campaigns = _get("campaigns")
    return _Campaigns(campaigns["data"], campaigns["sync"], campaigns["links"], campaigns["meta"])


def get_campaign(campaign_id: int):
    # no sync attribute here (yet?)
    campaign = _get(f"campaigns/{int(campaign_id)}")["data"]
    return _Campaign(campaign_id=campaign["id"], name=campaign["name"], locale=campaign["locale"],
                     entry=campaign["entry"], image=campaign["image"], image_full=campaign["image_full"],
                     image_thumb=campaign["image_thumb"], visibility=campaign["visibility"],
                     created_at=campaign["created_at"], updated_at=campaign["updated_at"], members=campaign["members"],
                     sync=campaign["members"]["sync"])


def get_campaign_members(campaign_id: int):
    members = _get(f"campaigns/{int(campaign_id)}/users")
    return _Members(members["data"], members["sync"])


def get_campaign_characters(campaign_id: int, related=None):
    if related:
        params = {"related": 1}
    else:
        params = None
    characters = _get(f"campaigns/{int(campaign_id)}/characters", params)
    return characters


def get_campaign_character(campaign_id: int, character_id: int, related=None):
    # no sync attribute here (yet?)
    if related:
        params = {"related": 1}
    else:
        params = None
    character = _get(f"campaigns/{int(campaign_id)}/characters/{character_id}", params)
    character = character["data"]
    return _Character(character["name"], character["entry"], character["title"], character["age"],
                      character["sex"], character["type"], character["family_id"], character["location_id"],
                      character["race_id"], character["tags"], character["is_dead"], character["is_private"],
                      character_id=character["id"], entity_id=character["entity_id"], image_path=character["image"],
                      image_full=character["image_full"], image_thumb=character["image_thumb"],
                      created_at=character["created_at"], created_by=character["created_by"],
                      updated_at=character["updated_at"], updated_by=character["updated_by"],
                      traits=character["traits"])


def create_character(campaign_id: int, character: _Character):
    if isinstance(character, _Character):
        pass
    else:
        raise TypeError("Please input a Character object tyvm")
    params = vars(character)
    if character.image:
        image = {"image": character.image}
        del params["image"]
        character = _post(f"campaigns/{int(campaign_id)}/characters", params, image)
    else:
        character = _post(f"campaigns/{int(campaign_id)}/characters", params, None)
    return character
