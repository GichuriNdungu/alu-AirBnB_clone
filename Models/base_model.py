import datetime
import uuid
class BaseModel:
    
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        '''Modify __str__ '''
        class_name = self.__class__.__name__
        return f"[{class_name}], ({self.id}), {self.__dict__}"
    def save(self):
        '''update updated_at with current time'''
        self.updated_at = datetime.datetime.now()
    
    
