import datetime
import uuid
class BaseModel:
    
    def __init__(self,*args, **kwargs):
        '''initialization of Basemodel objects'''
        if len(kwargs) != 0:
            if '__class__' in kwargs:
                del kwargs['__class__']
            for key, value in kwargs.items():
                    if key in ['created_at', 'updated_at']:
                       date_str = kwargs[key]
                       value = datetime.datetime.fromisoformat(kwargs[key])
                    setattr(self,key,value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
    def __str__(self):
        '''Modify __str__ '''
        class_name = self.__class__.__name__
        return f"[{class_name}], ({self.id}), {self.__dict__}"
    def save(self):
        '''update updated_at with current time'''
        self.updated_at = datetime.datetime.now()
    def to_dict(self):
        '''serializes objects into Json'''
        dict = {}
        cls_name = self.__class__.__name__
        self.__dict__['__class__'] = cls_name
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        dict = self.__dict__
        return dict