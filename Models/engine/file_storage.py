<<<<<<< HEAD
import json
class FileStorage:
    '''class to serializes objects into Json
        Additionally desializes Json into objects'''
    __file_path = "file.json" 
    __objects = {}
    def __init__(self):
        '''class constructor'''
        pass
    def all(self):
        '''Returns a list of all instance objects'''
        return self.__objects
    def new(self, obj):
        '''set in __objects a new object'''
        cls_name = obj.__class__.__name__
        self.__objects["{}.{}".format(cls_name, obj.id)] = obj

    def save(self):
        '''serializes objects into a Json file'''
        dictionary = {}
        for obj in self.__objects:
            dictionary[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dictionary, f)
    def reload(self):
        '''Desiralizes Json into objects'''

        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
        except: 
            pass
    
=======
>>>>>>> 9747274da1cd61d918d1c52e0a60e7cc125b169c
