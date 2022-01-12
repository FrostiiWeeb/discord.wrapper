import json


class Content:
    """
    A class that formats content.
    """

    def add_content(self, content, tts: bool = False):
        self.tts = tts
        self.content = content
        return self

    def __repr__(self) -> str:
        return f"<Content tts={self.tts!r} text={self.content!r}>"

    def to_dict(self):
        data = {"tts": self.tts, "content": self.content}
        return json.dumps(data)
