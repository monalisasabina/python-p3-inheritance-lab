#!/usr/bin/env python



from user import User

class Student(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge =[]
    
    def learn(self,learn_string):
        self.knowledge.append(learn_string)
        return learn_string    
    

student = Student("Monalisa","Sabina")

student.learn("cassava farming")
print(student.knowledge)
print(f"{student.first_name} {student.last_name} wants to learn {student.knowledge}")