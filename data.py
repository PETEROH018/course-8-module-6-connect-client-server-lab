class Event:
    def __init__(self,id,title):
        self.id = id
        self.title = title
    
    def to_dict(self):
        return {"id":self.id,"title":self.title}

events = [
    Event(1,"Hackathon"),
    Event(2,"Ted-Talk"),
    Event(3,"Meet and Greet")
    ]