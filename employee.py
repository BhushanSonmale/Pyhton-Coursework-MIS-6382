from vehicle import Vehicle
class Employee:
    
    def __init__(self, ename, eadd, veh):
        self.__emp_name = ename
        self.__emp_add = eadd
        self.__veh_data = veh
        
    def get_emp_name(self):
        return self.__emp_name
    def get_emp_add(self):
        return self.__emp_add
    def get_veh_data(self):
        return self.__veh_data
    def get_option4(self, lst):
             if(self.__veh_data.get_mil() > 78000):
                    result = "Employee name is: " + self.__emp_name + " Make: " + self.__veh_data.get_make()
                    result += "; Model: " + self.__veh_data.get_model() 
                    result += "; Year of Manufacture: " + str(self.__veh_data.get_yr_mfd()) + "; Mileage: " + str(self.__veh_data.get_mil())
                    print(result)
                    
    def set_emp_name(self, ename):
        self.__emp_name = ename
    def set_emp_add(self, eadd):
        self.__emp_add = eadd
    def set_veh_data(self, veh):
        self.__veh_data = veh
        
    def cal_compensation(self):
        pass
    
    def __str__(self):
        DataStore = "\nEmployee Name: " + self.__emp_name + "; Employee Address: " + self.__emp_add + "\n" + self.__veh_data.__str__()
        return DataStore