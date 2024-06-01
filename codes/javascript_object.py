class JavascriptObject:
    def __init__(self, prototype=None):
        if prototype is not None:
            self.__dict__['prototype'] = prototype

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        if 'prototype' in self.__dict__:
            return self.__dict__['prototype'].__getattr__(item)
        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{item}'")

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def keys(self):
        proto_keys = self.__dict__['prototype'].keys(
        ) if 'prototype' in self.__dict__ else []
        return [k for k in set(list(self.__dict__.keys())+proto_keys) if k != 'prototype']

    def values(self):
        return [self.__getattr__(k) for k in self.keys()]

    def __iter__(self):
        return self.keys()


# Ejemplo de uso:
animal_proto = JavascriptObject()
animal_proto.speak = lambda self: print(f'{self.name} makes a noise.')

dog_proto = JavascriptObject(animal_proto)
dog_proto.speak = lambda self: print(f'{self.name} barks.')

dog = JavascriptObject(dog_proto)
dog.name = 'Rex'
dog.speak(dog)
print(dog.values())
