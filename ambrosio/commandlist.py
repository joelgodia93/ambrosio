


class CommandList(object):
    def __init__(self):
        super(CommandList, self).__init__()
        self.commands = []


    def next(self):
        return self.commands.pop(0)


    def append(self, command):
        self.commans.append(command)


    def lenght(self):
        return len(self.commands)
