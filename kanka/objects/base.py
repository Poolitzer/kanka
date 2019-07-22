class KankaObject(object):
    """Base class for Kanka objects"""

    def __repr__(self):
        return str(vars(self))
