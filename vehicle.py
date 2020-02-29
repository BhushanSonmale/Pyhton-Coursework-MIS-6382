class Vehicle:
    
    #Constructor to accept values of all instance variables
    def __init__(self, make, model, yr_mfd, mil):
        self.__veh_make = make
        self.__veh_model = model
        self.__veh_yr_mfd = yr_mfd
        self.__veh_mil = mil
        
    #Defining accessor and mutator methods
    def get_make(self):
        return self.__veh_make
    def get_model(self):
        return self.__veh_model
    def get_yr_mfd(self):
        return self.__veh_yr_mfd
    def get_mil(self):
        return self.__veh_mil
    
    def set_make(self, make):
        self.__veh_make = make
    def set_model(self, make):
        self.__veh_model = model
    def set_yr_mfd(self, make):
        self.__veh_yr_mfd = yr_mfd
    def set_mil(self, make):
        self.__veh_mil = mil
    
    #Redefining __str__() method to return a single string
    def __str__(self):
        return "Make: " + self.__veh_make + "; Model: " + self.__veh_model + "; Year of Manufacture: " + str(self.__veh_yr_mfd) + "; Mileage: " + str(self.__veh_mil)
    