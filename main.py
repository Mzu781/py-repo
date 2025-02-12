class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def Name(self):
        return self.fname

    @Name.setter
    def Name(self, fname):  
        self.fname = fname

    @property
    def LastName(self):
        return self.lname

    @LastName.setter
    def LastName(self, lname):  
        self.lname = lname

    def __str__(self):
        return f'My name is {self.Name} {self.LastName}'


class Employee(Person):
    def __init__(self, fname, lname, job, company, salary):
        super().__init__(fname, lname)
        self.job = job
        self.company = company  
        self.salary = salary

    def __str__(self):
        return f'{super().__str__()}, I work as a {self.Job} 😊 at {self.company}, my salary is 💵 R{self.Salary}'

    @property
    def Salary(self):
        return self.salary

    @Salary.setter
    def Salary(self, salary): 
        self.salary = salary

    @property
    def Job(self):
        return self.job

    @Job.setter
    def Job(self, job):  
        self.job = job  


person1 = Employee('Emily', 'Johnson', 'Software Engineer', 'TechCorp', 435879)
print(person1)
