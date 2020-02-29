from employee import Employee
class FullTimeEmployee(Employee):
    
    def __init__(self, ename, eadd, veh, sal):
        super().__init__(ename, eadd, veh)
        self.__salary = sal
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, sal):
        self.__salary = sal
        
    def cal_compensation(self):
        if(self.__salary <= 45000):
            compensation = self.__salary - (0.18 * self.__salary)
            return compensation
        else:
            if(self.__salary > 45000 and self.__salary <= 82000):
                tx1 = 0.18 * 45000
                tx2 = 0.28 * (self.__salary - 45000)
                compensation = self.__salary - (tx1 + tx2)
                return compensation
            else:
                tx1 = 0.18 * 45000
                tx2 = 0.28 * (82000 - 45000)
                tx3 = 0.33 * (self.__salary - 82000)
                compensation = self.__salary - (tx1 + tx2 + tx3)
                return compensation
            
    def __str__(self):
        EmpDataStore = super().__str__()
        EmpDataStore = "\nDetails of Full Time Employee are: " + EmpDataStore
        EmpDataStore += "\nSalary: " + '{0}'.format(str("{0:.2f}".format(self.__salary)))
        return EmpDataStore