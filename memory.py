class Memory:
    def __init__(self):
        self.history = []

    def store(self, text):
        self.history.append(text)

    def retrieve(self):
        return self.history

    def clear(self):
        self.history = []
