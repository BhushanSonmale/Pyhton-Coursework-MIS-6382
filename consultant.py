from employee import Employee
class Consultant(Employee):
    
    def __init__(self, ename, eadd, veh, hoursWorked, ProjectType):
        super().__init__(ename, eadd, veh)
        self.__hWorked = hoursWorked
        self.__pType = ProjectType
        
    def get_hWorked(self):
        return self.__hWorked
    def get_pType(self):
        return self.__pType
    
    def set_hWorked(self, hoursWorked):
        self.__hWorked = hoursWorked
    def set_pType(self, ProjectType):
        self.__pType = ProjectType
        
    
    def cal_compensation(self):
        if(self.__pType == 1):
            compensation = self.__hWorked * 55.0
            return compensation
        if(self.__pType == 2):
            compensation = self.__hWorked * 70.0
            return compensation
        if(self.__pType == 3):
            compensation = self.__hWorked * 85.0
            return compensation
        
    def __str__(self):
        EmpDataStore = super().__str__()
        EmpDataStore = "\nDetails of Consultant are: " + EmpDataStore
        EmpDataStore += "\nHours Worked: " + str(self.__hWorked) + "\nProject Type: " + str(self.__pType)
        return EmpDataStore