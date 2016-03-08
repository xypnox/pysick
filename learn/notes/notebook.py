class note:
    def __init__(self, title, content, tags=[]):
        self.title = title
        self.tags = tags


class notebook:
    def __init__(self):
        self.notelist = []

    def newnote(self, title, content, tags=[]):
        self.notelist.append(note(title, content, tags))
