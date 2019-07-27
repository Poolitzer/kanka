from kanka.objects.base import KankaObject
from kanka.objects import Members
from kanka.utils.helpers import time_converter


class Campaign(KankaObject):
    """This object represents a Kanka campaign. It features information about a specific campaign and Kanka users
    with basic information as a members list. There is no way to create a campaign with the API (yet).
    Attributes:
          id  (:obj:`int`): Unique identifier for this campaign
          name (:obj:`str`): Name of the campaign
          locale (:obj:`str`): Locale, means the language of the campaign.
          entry (:obj:`str`): Entry is the description of the campaign
          image (:obj:`str`): URL to the campaigns image, is None by default (maybe depreciated?)
          image_full (:obj:`str`): URL to the campaigns image, seems to be the standard now
          image_thumb (:obj:`str`): URL to the campaigns image as a thumbnail
          visibility (:obj:`str`): If this is True, other people can see your campaign
          created_at (:obj:`datetime.datetime`): This value returns a datetime object for the time this campaign was
          created.
          updated_at (:obj:`datetime.datetime`):  This value returns a datetime object for the time this campaign was
          last updated.
          members (:class:`kanka.objects.Members`): This value returns a members object, with members and sync as
          attributes.

    """
    def __init__(self, campaign_id: int, name: str, locale: str, entry: str, image: str, image_full: str,
                 image_thumb: str, visibility: str, created_at: dict, updated_at: dict, members: dict, sync: dict):
        self.id = int(campaign_id)
        self.name = str(name)
        self.locale = str(locale)
        self.entry = str(entry)
        self.image = str(image)
        self.image_full = str(image_full)
        self.image_thumb = str(image_thumb)
        self.visibility = str(visibility)
        self.created_at = time_converter(created_at)
        self.updated_at = time_converter(updated_at)
        self.sync = time_converter(sync)
        self.members = Members(members["data"], members["sync"])
