class KankaObject(object):
    """Base class for Kanka objects"""


class User(KankaObject):
    """This object represents a Kanka User. Currently, you either can get it for yourself with more details or you
    can get members of a campaign.

    Attributes:
        id (:obj:`int`)


    """
    def __init__(self, user_id, name, avatar, avatar_thumb=None, locale=None, timezone=None, date_format=None,
                 default_pagination=0, last_campaign_id=0, is_patreon=None):
        # Required
        self.id = int(user_id)
        self.name = str(name)
        self.avatar = str(avatar)
        # Optional
        self.avatar_thumb = str(avatar_thumb)
        self.locale = str(locale)
        self.timezone = str(timezone)
        self.date_format = str(date_format)
        self.default_pagination = int(default_pagination)
        self.last_campaign_id = int(last_campaign_id)
        self.is_patreon = is_patreon

    def __repr__(self):
        return str(vars(self))