import random

class Repository:
    def __init__(self):
        self.entries = []

    def load_entries(self, file_path):
        """Load the sentences from a text file and store them in the repository"""
        with open(file_path, 'r') as file:
            for line in file:
                self.entries.append(line.strip())
        return self.entries


    def get_random_entry(self):
        """Return a random sentence from the repository"""
        random.shuffle(self.entries)
        return self.entries[0]