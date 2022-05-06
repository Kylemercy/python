#static method
#it can be defined using
#the @staticmethod decorator or 
#staticmethod() function.


class Employee(object):

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        print("done", requirement)
        # this print a list
    # to print out the items in the list we 
    #iterate using a for loop
        for task in requirement:
            print('Completed', task)
emp = Employee('Kelly', 12000, 'ABC Project')
emp1 = Employee('bily', 15800, 'DCA Project')
emp.work()
print("\n")
emp1.work()