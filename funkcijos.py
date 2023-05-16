from backend import *
from test import *



class LentelesFunkcijos:
    def __init__(self, lentele):
        self.lentele = lentele
        self.session = session
     
    def delete_element(self, el_id):
        self.session.delete(self.session.get(self.lentele, el_id))
        return self.session.commit()
     
    def add_element(self, **kw):
        self.session.add(self.lentele(**kw))
        return self.session.commit()
    
    def set_element(self, el_id, **kw):
        self.session.query(self.lentele).filter(self.lentele.id==el_id).update(kw)
        return self.session.commit()


#LentelesFunkcijos(Status).delete_element(3)
#LentelesFunkcijos(Status).add_element(name='name1')
LentelesFunkcijos(Status).set_element(1, name='name2', name2='name3')
print()