class Student:
    school='AkiraChix'
    def __init__(self,firstname,lastname,age,country):#constructor
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.country=country
    def greet_student(self):
        return f"hello {self.firstname} {self.lastname}, welcome to {self.school}"  
    def year_of_birth(self,year): 
        currentyear=year-self.age
        return f"hello {self.firstname} {self.lastname},you were born in {currentyear}"  
    def show_full_name(self):
        return f"hello {self.firstname} {self.lastname}"  
    def  show_initials(self):
        return f"{self.firstname[0]} {self.lastname[0]}"
        