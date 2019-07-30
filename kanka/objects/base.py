from kanka.utils.helpers import time_converter
from typing import List as _List


class KankaObject(object):
    """Base class for Kanka objects"""

    def __repr__(self):
        return str(vars(self))


class Entity(KankaObject):
    """Base class with common attributes for all Entities as defined in the documentation. Although every field is
    always present, its value may be None.
    Attributes:
        object_id  (:obj:`int`): The id identifying the object against all other objects of the same type. *Note*: id is
         a reserved word in python, we use object_id instead.
        name  (:obj:`str`): The name representing the object.
        entry  (:obj:`str`): The html description of the object.
        image  (:obj:`str`): The local path to the picture of the object.
        image_full  (:obj:`str`): The url to the picture of the object.
        image_thumb (:obj:`str`): The url to the thumbnail of the object.
        is_private  (:obj:`bool`): Determines if the object is only visible by *admin* members of the campaign. If the
        user requesting the API isn't a member of the *admin* role, such objects won't be returned.
        entity_id  (:obj:`int`): The id identifying the objects against all other entities.
        tags  (_List[int]): An array of tags that the object is related to.
        created_at (:obj:`datetime.datetime`): This value returns a datetime object for the time this campaign was
        created_by  (:obj:`int`): The :class:`kanka.objects.User`'s id who created the object.
        updated_at (:class:`datetime.datetime`):  This value returns a datetime object for the time this campaign was
        last updated.
        updated_by  (:class:`int`): The :class:`kanka.objects.User`'s id who last updated the object.

    """
    def __init__(self, object_id=0, name="", entry="", image_path="", image_full="", image_thumb="", is_private=False,
                 entity_id=None, tags=None, created_at=None, created_by=None, updated_at=None, updated_by=None):
        if object_id:
            self.object_id = int(object_id)
        else:
            self.object_id = None
        self.name = str(name)
        self.entry = str(entry)
        self.image = str(image_path)
        self.image_full = str(image_full)
        self.image_thumb = str(image_thumb)
        self.is_private = bool(is_private)
        if entity_id:
            self.entity_id = int(entity_id)
        else:
            self.entity_id = None
        if tags is None:
            tags = []
        self.tags = list(tags)
        if created_at:
            self.created_at = time_converter(created_at)
        else:
            self.created_at = None
        if created_by:
            self.created_by = int(created_by)
        else:
            self.created_by = None
        if updated_at:
            self.updated_at = time_converter(updated_at)
        else:
            self.updated_at = None
        if updated_by:
            self.updated_by = int(updated_by)
        else:
            self.updated_by = None


class Related(KankaObject):
    """Base class with related attributes, used when the user requests related objects"""
    def __init__(self, ):
        print("yeah")
