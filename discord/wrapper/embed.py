import json


class Embed:
    __slots__ = (
        "colour",
        "color",
        "title",
        "description",
        "fields",
        "author",
    )

    def __init__(self, **kwargs):
        self.color = kwargs.pop("color", None)
        self.colour = kwargs.pop("colour", None)
        self.title = kwargs.get("title", None)
        self.description = kwargs.pop("description", "DEFAULT")
        self.fields = []

    def set_author(self, name: str):
        self.author = {"name": name}
        return self

    def add_field(self, name: str, value: str, inline: bool = True):
        self.fields.append({"name": name, "value": value, "inline": inline})
        return self

    def __repr__(self):
        fmt = ""
        for attr in self.__slots__:
            val = getattr(self, attr, None)
            if val:
                fmt += " {}={}".format(attr, val)
                break
        return f"<Embed{fmt}>"

    def to_dict(self, to_json=True):
        """Turns the object into a dictionary"""
        d = {
            "embed": {
                key: getattr(self, key)
                for key in self.__slots__
                if hasattr(self, key) and getattr(self, key)
            }
        }
        new = json.dumps(d)
        if to_json:
            return json.dumps(d)
        else:
            return str(new)
