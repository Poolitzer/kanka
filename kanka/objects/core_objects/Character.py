from kanka.objects.base import Entity, KankaObject
import io
from kanka.utils.helpers import time_converter
from typing import List as _List


class Character(Entity):
    """This object represents a Kanka character. Although it always has all attributes, some may be None,
    depending if you created it or get it from the server.
    Attributes:
        name  (:obj:`str`): Required. Name of the character
        title  (:obj:`str`): Title of the character
        age  (:obj:`str`): Age of the character
        sex  (:obj:`str`): Gender of the character
        character_type  (:obj:`str`): Type of the character. Type (as used in the API= is a reserved word in python, we
        use character_type instead
        family_id  (:obj:`int`): Family id
        location_id  (:obj:`int`): Location id
        race_id  (:obj:`int`): Race id
        tags  (_List[int]): Array of tag ids
        is_dead  (:obj:`bool`): If the character is dead
        is_private  (:obj:`bool`): If the character is only visible to *admin* members of the campaign
        image  (`filelike object`): Please use ``open(filename, 'rb')`` with this attribute to upload a local picture
        image_url  (:obj:`str`): URL to a picture to be used for the character
        personality_name  (_List[str]): An array representing the name of personality traits. For example
        *["Goals", "Fears"]*
        personality_entry  (_List[str]): An array representing the values of personality traits. For example
        *["To become a King", "Quiet places"]*
        appearance_name  (_List[str]): An array representing the name of appearance traits. For example
        *["Hair", "Eyes"]*
        appearance_entry  (_List[str]): An array representing the values of appearance traits. For example
        *["Curly black", "Light Green"]*
    These are the ones you can define. If you get a character from the server, there are more which you can find in
    the documentation of :class:`kanka.objects.base.Entity`.
    Also note that there is the (:class:`Traits`) which get returned from the server.
    """
    def __init__(self, name: str, entry="", title="", age="", sex="", character_type="", family_id=0, location_id=0,
                 race_id=0, tags=None, is_dead=False, is_private=False, image=False, image_url="",
                 personality_name=None, personality_entry=None, appearance_name=None, appearance_entry=None,
                 character_id=0, entity_id=0, traits=None, image_path="", image_full="", image_thumb="",
                 created_at=None, created_by=None, updated_at=None, updated_by=None):
        super().__init__(character_id, name, entry, image_path, image_full, image_thumb, is_private, entity_id, tags,
                         created_at, created_by, updated_at, updated_by)
        self.title = str(title)
        self.age = str(age)
        self.sex = str(sex)
        self.type = str(character_type)
        if family_id:
            self.family_id = int(family_id)
        else:
            self.family_id = None
        if location_id:
            self.location_id = int(location_id)
        else:
            self.location_id = None
        if race_id:
            self.race_id = int(race_id)
        else:
            self.race_id = None
        self.is_dead = bool(is_dead)
        if isinstance(image, io.BufferedReader):
            self.image = image
        else:
            self.image = None
        self.image_url = str(image_url)
        if personality_name is None:
            personality_name = []
        self.personality_name = list(personality_name)
        if personality_entry is None:
            personality_entry = []
        self.personality_entry = list(personality_entry)
        if appearance_name is None:
            appearance_name = []
        self.appearance_name = list(appearance_name)
        if appearance_entry is None:
            appearance_entry = []
        self.appearance_entry = list(appearance_entry)
        if traits is None:
            self.traits = None
        else:
            self.traits = Traits(traits["data"], traits["sync"])

    @classmethod
    def from_dict(cls, dictionary: dict):
        obj = Character(dictionary["name"])
        for key, value in dictionary.items():
            for class_key in vars(obj):
                if key == class_key:
                    setattr(obj, key, value)
        return obj


class Traits(KankaObject):
    """This object represents traits and it's sync attribute
    Attributes:
        traits  (_List[:class:`Trait`]): Array of Trait objects
        sync  (:class:`datetime.datetime``): A datetime object of the last time this object was changed.
            The library deals with it, but its there for convenience.
    """
    def __init__(self, traits, sync):
        temp = []
        for trait in traits:
            temp.append(Trait(trait["id"], trait["name"], trait["entry"], trait["section"], trait["is_private"],
                              trait["default_order"]))
        self.traits = temp
        self.sync = time_converter(sync)


class Trait(KankaObject):
    """This object represents a trait, returned by the server for the character.
    Attributes:
        trait_id  (int): The id of the trait. *Note*: id is a reserved word in python, we use trait_id instead.
        name  (str): The name of the trait.
        entry  (str): The entry of the trait.
        section  (str): The section of the trait. Currently either *personality* or *appearance*.
        is_private  (bool): If the trait is private for everyone who isn't the owner or admin
        default_order  (int): No fucking clue how this works.
    """
    def __init__(self, trait_id, name, entry, section, is_private, default_order):
        self.trait_id = int(trait_id)
        self.name = str(name)
        self.entry = str(entry)
        self.section = str(section)
        self.is_private = bool(is_private)
        self.default_order = int(default_order)
