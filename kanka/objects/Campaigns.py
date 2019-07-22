from kanka.objects import KankaObject, Campaign
from kanka.utils.helpers import time_converter
from typing import List as _List


class Campaigns(KankaObject):
    """This object represents campaigns. It consists of all the campaigns a user has and some meta info.
    Attributes:
          campaigns (_List[:class:`kanka.objects.Campaign`]): A list of campaigns from the user
          links (:class:`kanka.objects.Campaigns.Links`): The link object. I have also no idea
          meta (:class:`kanka.objects.Campaigns.Meta`): The meta object. Has some meta infos - I guess?
          sync (:obj:`datetime.datetime`): A datetime object of the last time this object was changed. The library
          deals with it, but its there for convenience.
    """
    def __init__(self, campaigns: _List[dict], sync: dict, links: dict, meta: dict):
        temp = []
        for campaign in campaigns:
            temp.append(Campaign(campaign_id=campaign["id"], name=campaign["name"], locale=campaign["locale"],
                        entry=campaign["entry"], image=campaign["image"], image_full=campaign["image_full"],
                        image_thumb=campaign["image_thumb"], visibility=campaign["visibility"],
                        created_at=campaign["created_at"], updated_at=campaign["updated_at"],
                        members=campaign["members"], sync=campaign["members"]["sync"]))
        self.campaigns = temp
        self.links = Links(links["first"], links["last"], links["prev"], links["next"])
        self.meta = Meta(meta["current_page"], meta["from"], meta["last_page"], meta["path"], meta["per_page"],
                         meta["to"], meta["total"])
        self.sync = time_converter(sync)


class Links(KankaObject):
    """This object represents the link attribute of the campaigns object.
    Attributes:
        first  (:obj:`str`): An URL. To the first page of smth? I have no clue
        last (:obj:`str`): Also an URL, for me its the same as first. Like wtf?
        prev: This is just None.
        next: This as well.
    """
    def __init__(self, first: str, last: str, prev, next_link):
        self.first = first
        self.last = last
        self.prev = prev
        self.next = next_link


class Meta(KankaObject):
    """This object represents the meta attribute of the campaigns object. Note that from is a reserved word in python,
    from_meta is used instead.
    Attributes:
        current_page (:obj:`int`): seems to be an integer of the current page. hehe.
        from_meta (:obj:`int`): its the same integer as above. No idea...
        last_page (:obj:`int`): same. I have no idea.
        path (:obj:`str`): That's the URL of this method. So great. We have that now.
        per_page (:obj:`int`): This is the pagination of the User. Figured that out :D
        to (:obj:`int`): ?
        total  (:obj:`int`): ??? If you ask me, I'd say the amounts of campaigns someone has. Maybe?
    """
    def __init__(self, current_page: int, from_meta: int, last_page: int, path: str, per_page: int, to: int,
                 total: int):
        self.current_page = current_page
        self.from_meta = from_meta
        self.last_page = last_page
        self.path = path
        self.per_page = per_page
        self.to = to
        self.total = total
