import datetime
import uuid
class BaseModel:
    
    def __init__(self,*args, **kwargs):
        '''initialization of Basemodel objects'''
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.datetime.strptime(kwargs['created_at'],tform)
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.datetime.strptime(kwargs['updated_at'], tform)
            self.__dict__.update(kwargs)
        Models.storage.new(self)
    def __str__(self):
        '''Modify __str__ '''
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
    def save(self):
        '''update updated_at with current time'''
        self.updated_at = datetime.datetime.now()
        Models.storage.save()
    def to_dict(self):
        '''serializes objects into Json'''
        dict = self.__dict__.copy()
        cls_name = self.__class__.__name__
        dict['__class__'] = cls_name
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
