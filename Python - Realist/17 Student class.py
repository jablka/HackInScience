class Student:
    def __init__(self, name) -> None:
        self.name = name
        self.grade = []

    def add_exam(self, grade:float):
        self.grade.append(grade)

    def get_mean(self): # 
        return sum(self.grade) / len(self.grade)
    


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.student = []
        # self.best_student = None

    def add_student(self, student):      
        self.student.append(student)
    
    def get_mean(self):
        buffer = []
        for i in self.student:
            buffer.append( i.get_mean() )
        return sum(buffer) / len(buffer)

    def get_best_student(self):
        buffer = []
        for i in self.student:
            buffer.append( (i, i.get_mean()) )
        result = max(buffer, key=lambda x:x[1])[0]    
        return result # best grade is maximum



class City:
    def __init__(self, name) -> None:
        self.name = name
        self.school = []
    
    def add_school(self, school):
        self.school.append(school)

    def get_mean(self):
        buffer = []
        for i in self.school:
            buffer.append( i.get_mean() )
        return sum(buffer) / len(buffer)

    def get_best_school(self): 
        buffer = []
        for i in self.school:
            buffer.append( (i, i.get_mean()) )
        return max(buffer, key=lambda x:x[1] )[0] # best grade is maximum

    def get_best_student(self):
        buffer = []
        for i in self.school:
            buffer.append( i.get_best_student() )
        return max(buffer) # best grade is maximum