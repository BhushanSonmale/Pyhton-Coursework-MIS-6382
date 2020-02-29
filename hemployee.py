from employee import Employee
class HourlyEmployee(Employee):
    
    def __init__(self, ename, eadd, veh, hoursWorked, hourlyRate):
        super().__init__(ename, eadd, veh)
        self.__hWorked = hoursWorked
        self.__hRate = hourlyRate
        
    def get_hWorked(self):
        return self.__hWorked
    def get_hRate(self):
        return self.__hRate
    
    def set_hWorked(self, hoursWorked):
        self.__hWorked = hoursWorked
    def set_hRate(self, hourlyRate):
        self.__hRate = hourlyRate
        
    def cal_compensation(self):
        if(self.__hWorked <= 40):
            compensation = self.__hWorked * self.__hRate
            return compensation
        else:
            comp1 = 40 * self.__hRate
            comp2 = (self.__hWorked - 40) * self.__hRate * 1.8
            compensation = comp1 + comp2
            return compensation
        
    def __str__(self):
        EmpDataStore = super().__str__()
        EmpDataStore = "\nDetails of Hourly Employee are: " + EmpDataStore
        EmpDataStore += "\nHours Worked: " + str(self.__hWorked) + "\nHourly Rate: " + str(int(self.__hRate))
        return EmpDataStore