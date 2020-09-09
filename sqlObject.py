class Employee:
    def __init__(self, first, last, position, salary, birthday, mail='gmail'):
        self.first = first
        self.last = last
        self.position = position
        self.salary = salary
        self.birthday = birthday

    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@{mail}.com'
    
    def __repr__(self):
        return f'Employee: ({self.first}, {self.last}, {self.salary})'