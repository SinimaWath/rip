class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.used = []
        self.index = 0
        self.ignore_case = kwargs.get('ignore_case')

    def __next__(self):
        while True:
            if self.index == len(self.items):
                raise StopIteration

            item_to_insert = self.items[self.index]

            if self.ignore_case:
                item_to_insert = self.items[self.index].lower()

            if item_to_insert not in self.used:
                self.used.append(item_to_insert)
                self.index += 1
                return self.items[self.index - 1]

            self.index += 1

    def __iter__(self):
        return self