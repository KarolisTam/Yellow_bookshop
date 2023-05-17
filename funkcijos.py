from backend import *


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
    
    def get_table_el_list(self):
        return session.query(self.lentele).all()
    
    def join_element_relationship(self):
        pass

#LentelesFunkcijos(Customer).delete_element(1)
#LentelesFunkcijos(Status).add_element(name='name1')
#LentelesFunkcijos(Status).set_element(1, name='name2', name2='name3')
#LentelesFunkcijos(SecurityQuestions).add_element(question_text='Pirmo augintinio vardas ?')
# LentelesFunkcijos(Product).add_element(book_name='Lord of the rings',author='Ted', realease_date='2000', price=12, quantity=5)
#LentelesFunkcijos(Customer).set_element(1, security_key='GreenDay')
