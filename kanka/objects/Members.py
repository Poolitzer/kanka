from kanka.objects import KankaObject, User
from kanka.utils.helpers import time_converter
from typing import List as _List


class Members(KankaObject):
    """This object represents a Kanka member list. There is no way to create a member list with the API (yet).
        Attributes:
            members (_List[:class:`kanka.objects.User`]): Returns a list of User objects
            sync (:obj:`datetime.datetime`): A datetime object of the last time this object was changed.
            The library deals with it, but its there for convenience.
    """
    def __init__(self, members: dict, sync: dict):
        temp = []
        for member in members:
            # this block is there for the two different ways this list is created. If with a campaign call, the first
            # block is used. If with the designated member call, the second. A user generating a members list for any
            # reason shouldn't see a difference, it will just work.
            try:
                temp.append(User(campaign_member_table_id=member["id"], user_id=member["user"]["id"],
                                 name=member["user"]["name"], avatar=member["user"]["avatar"]))
            except KeyError:
                temp.append(User(user_id=member["id"], name=member["name"], avatar=member["avatar"]))
        self.members = temp
        self.sync = time_converter(sync)
