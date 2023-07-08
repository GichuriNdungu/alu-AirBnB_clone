import json
class FileStorage:
    '''class to serializes objects into Json
        Additionally desializes Json into objects'''
    __file_path = "file_json"
    def __init__(self):
        '''class constructor''' 
        self.__objects = {}
    
    def all(self):
        '''Returns a list of all instance objects'''
        return self.__objects
    def new(self, obj):
        '''set in __objects a new object'''
        obj_id = obj.id
        cls_name = obj.__class__.__name__
        key = cls_name + '.' + obj_id
        value = obj.to_dict()
        self.__objects[key] = value
    def save(self):
        '''serializes objects into a Json file'''
        data = self.__objects
        file = self.__file_path
        with open(file, "w") as f:
            json.dump(data, f)
    def reload(self):
        '''Desiralizes Json into objects'''
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.loads(f)
        except: 
            pass
    