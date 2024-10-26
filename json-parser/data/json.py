class JSON:
    def __init__(self, key_to_values):
        self.key_to_values = key_to_values

    def get(self, key):
        return self.key_to_values.get(key)

    def get_all_keys(self):
        keys = []
        for key in self.key_to_values.keys():
            keys.append(key)
        return keys

    def is_leaf(self):
        return (len(self.key_to_values) == 1 and 
                next(iter(self.key_to_values.values())) is None)
    
    def __str__(self):
        return f"{self.key_to_values}"