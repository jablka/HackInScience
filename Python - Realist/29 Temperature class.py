class Temperature:
    def __init__(self):
        self.data = [None, None, None ] # kelvin, celsius, fahrenheit

    @property
    def kelvin(self):
        return self.data[0]
    
    @kelvin.setter
    def kelvin(self, value):
        self.data[0] = value
        self.data[1] = self.kelvin - 273.15 # K_to_C()
        self.data[2] = self.kelvin*(9/5)-459.67  #  K_to_F() 

    @property
    def celsius(self):
        return self.data[1]

    @celsius.setter
    def celsius(self, value):
        self.data[1] = value        
        self.data[0] = self.celsius + 273.15 # C_to_K
        self.data[2] = self.kelvin*(9/5)-459.67  # K_to_F
 
    @property
    def fahrenheit(self):
        return self.data[2]

    @fahrenheit.setter
    def fahrenheit(self,value):
        self.data[2] = value        
        self.data[0] = (self.fahrenheit +459.67)*(5/9) # F_to_K
        self.data[1] = self.kelvin - 273.15 # K_to_C        
