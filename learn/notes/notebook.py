import os


class note:
    def __init__(self, title, content='', tags=[]):
        self.title = title
        self.content = content
        self.tags = tags
        os.system('touch '+title+'.txt')
        self.file = open(str(title+'.txt'), 'r+')
        towrite = "Title : " + title + '\n'
        if len(tags) > 0:
            towrite += "Tags : " + tags + '\n'
        towrite += "\n" + content
        self.file.write(title+'\n'+repr(tags)+'\n'+content)

    def display(self):
        os.system('nano '+self.title+'.txt')

    def addtag(self, tag):
        self.tags.append(tag)

    def finish(self):
        self.file.close()


class notebook:
    def __init__(self):
        self.notelist = []

    def newnote(self, title, content='', tags=[]):
        self.notelist.append(note(title, content, tags))
