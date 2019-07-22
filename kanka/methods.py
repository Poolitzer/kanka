from kanka.objects import User as _User, Campaign as _Campaign, Campaigns as _Campaigns, Members as _Members
from kanka.request import _get


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
