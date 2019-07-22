from kanka.objects import KankaObject


class User(KankaObject):
    """This object represents a Kanka User. Currently, you either can get it for yourself with more details
    (marked as optional) or you can get members of a campaign with only basic information.

    Attributes:
        id (:obj:`int`): Unique identifier for this user
        name (:obj:`str`): Users name
        avatar (:obj:`str`): URL to the avatar of the user
        avatar_thumb (:obj:`str`): Optional. URL to the avatar thumbnail of the user
        locale (:obj:`str`): Optional. Country code, currently taken from the language the user chose
        timezone (:obj:`str`): Optional. Timezone of the user
        date_format(:obj:`str`): Optional. Date format of the user, can be changed in the layout settings
        default_pagination (:obj:`int`): Optional. Pagination (elements per page) of the user, can be changed
        in the layout settings
        last_campaign_id (:obj:`int`): Optional. Latest campaign of the user
        is_patreon (:obj:`bool`): Optional. True if the user is a patreon and linked the account to their Kanka profile
        campaign_member_table_id (:obj:`int`): Optional. Only returned in campaign member section
    """
    def __init__(self, user_id: int, name: str, avatar: str, avatar_thumb="", locale="", timezone="", date_format="",
                 default_pagination=0, last_campaign_id=0, is_patreon="", campaign_member_table_id=0):
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
        self.campaign_member_table_id = campaign_member_table_id
