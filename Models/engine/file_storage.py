import json
class FileStorage:
    '''class to serializes objects into Json
        Additionally desializes Json into objects'''
    __file_path = "file_json" 
    __objects = {}

    def __init__(self):
        '''class constructor'''
        pass
    def all(self):
        '''Returns a list of all instance objects'''
        return self.__objects
    def new(self, obj):
        '''set in __objects a new object'''
        obj_id = obj.id
        cls_name = obj.__class__.__name__
        key = cls_name + '.' + obj_id
        FileStorage.__objects[key] = obj
    def save(self):
        '''serializes objects into a Json file'''
        dictionary = {}
        for obj in FileStorage.__objects:
            dictionary[obj] = FileStorage.__objects[obj].to_dict()
        with open(self.__file_path, "w") as f:
                json.dump(dictionary, f)
    def reload(self):
        '''Desiralizes Json into objects'''
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.loads(f)
        except: 
            pass
    