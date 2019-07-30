from kanka.utils.helpers import time_converter


class Attribute:
    """
    An object representing an attribute of an entity.
    Attributes:
        name  (:class:`str`): Required. Name of the attribute
        entity_id  (:class:`int`): Required. The attribute's parent entity
        value  (:class:`str`): The attribute's value
        default_order  (:class:`int`): The attribute's order
        attribute_type  (:class:`str`): The attribute's type (*block* or *checkbox*). *Note*: type is a reserved word
        in python, we use attribute_type instead.
        is_private  (:class:`bool`): If the attribute is only visible to *admin* members of the campaign
        api_key  (:class:`str`): A custom field only shown in the API for you to link attributes to your system ids.
    You can define these attributes by yourself. If you receive an Attribute, the following fields are added:
    Attributes:
        attribute_id  (:class:`int`): The id of the attribute to identify it against other attributes *Note*: id is a
        reserved word in python, we use attribute_id instead.
        created_at (:class:`datetime.datetime`): This value returns a datetime object for the time this campaign was
        created_by  (:class:`int`): The :class:`kanka.objects.User`'s id who created the object.
        updated_at (:class:`datetime.datetime`):  This value returns a datetime object for the time this campaign was
        last updated.
        updated_by  (:class:`int`): The :class:`kanka.objects.User`'s id who last updated the object.
    """
    def __init__(self, name, entity_id, value="", default_order=None, attribute_type="", is_private=None, api_key="",
                 attribute_id=None, created_at=None, created_by=None, updated_at=None, updated_by=None):
        self.name = str(name)
        self.entity_id = int(entity_id)
        self.value = str(value)
        if default_order:
            self.default_order = int(default_order)
        else:
            self.default_order = None
        self.attribute_type = attribute_type
        self.is_private = bool(is_private)
        self.api_key = str(api_key)
        if attribute_id:
            self.attribute_id = int(attribute_id)
        else:
            self.attribute_id = None
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
