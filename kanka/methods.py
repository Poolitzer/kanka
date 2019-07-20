from kanka.objects import User
from kanka.request import get


def get_user():
    profile = get("profile")
    return User(user_id=profile["id"], name=profile["name"], avatar=profile["avatar"],
                avatar_thumb=profile["avatar_thumb"], locale=profile["locale"], timezone=profile["timezone"],
                date_format=profile["date_format"], default_pagination=profile["default_pagination"],
                last_campaign_id=profile["last_campaign_id"], is_patreon=profile["is_patreon"])
