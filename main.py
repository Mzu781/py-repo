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


def displayEmployees(employees):
    if(len(employees) == 0):
        print("No employees detected...")
        return
    for employee in employees :
        print(employee)


employees = [
    Employee('Emily', 'Johnson', 'Software Engineer', 'TechCorp', 435879),
    Employee('James', 'Smith', 'Data Analyst', 'DataWorks', 389500),
    Employee('Sophia', 'Brown', 'Product Manager', 'InnoTech', 512000),
    Employee('Michael', 'Davis', 'Cybersecurity Specialist', 'SecureNet', 470000),
    Employee('Olivia', 'Wilson', 'UI/UX Designer', 'CreativeHub', 398000)
]

displayEmployees(employees)
