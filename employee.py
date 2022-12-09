"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, amount, s_period, commission, c_period):
        self.name = name
        self.amount = amount
        self.s_period = s_period
        self.commission = commission
        self.c_period = c_period

    def get_pay(self):
        return ((self.amount * self.s_period) + (self.commission * self.c_period))
        

    def __str__(self):
        periodText = "monthly salary of " + str(self.amount)
        if(self.s_period != 1):
            periodText = "contract of " + str(self.s_period) + " hours at " + str(self.amount) + "/hour"
        
        if(self.commission == 0):
            finString = self.name + " works on a " + periodText + ". Their total pay is " + str(self.get_pay())
        
        elif(self.commission != 0):
            comText = " and receives a bonus commission of " + str(self.commission) + "."
            if(self.c_period != 1):
                comText = " and receives a commission for " + str(self.c_period) + " contract(s) at " + str(self.commission) + "/contract."


            finString = self.name + " works on a " + periodText + comText + " Their total pay is " + str(self.get_pay())

        return finString
            


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, 1, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 1, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 1, 1500, 1)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, 600, 1)