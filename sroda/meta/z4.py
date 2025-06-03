class RequireAttribute(type):
    require_attributes = ["id", "name"]
    def __new__(cls, name, base, fields):
        obj = super().__new__(cls, name, base, fields)
        for req in cls.require_attributes:
            if req not in fields:
                raise AttributeError(f"No required field: {req}")
        return obj

class PassClass(metaclass=RequireAttribute):
    id = name = None

class FailClass(metaclass=RequireAttribute):
    def __init__(self, id, name):
        self.id = id
        self.name = name