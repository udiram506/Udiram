print("***********************************************************************************NCCS Higher Secondary School Result Making with Cchirag Aaplication***********************************************************")
print("")
print("")
print("Total marks is 500")
print("Total percentage: 100%")
print("Total G.P.A: 4.0")
print("")
print("")
class markSheet:



    def __init__(self,computer,english,Account,nepali,business,operator,userName):
        self.computer=computer
        self.english=english
        self.Account=Account
        self.nepali=nepali
        self.business=business
        self.operator=operator
        self.userName=userName
       
    
    def markk(self):
        if self.operator=="":
            self.total=self.computer+self.english+self.Account+self.nepali+self.business
            self.percentage=self.total/500 * 100
            self.businessP=self.business/100*100
            self.businessG=(self.businessP/20)-1
            self.accountP=self.Account/100*100
            self.accountG=(self.accountP/20)-1
            self.nepaliP=self.nepali/100*100
            self.nepaliG=(self.nepaliP/20)-1
            self.businessP=self.business/100*100
            self.businessG=(self.businessP/20)-1
            
 
            self.gpa=(self.percentage/20)-1
          
        if (self.percentage >= 50):
            print("he is passed .")
        else:
            print("he is not passed")
       
        if self.businessP == 60:
            print("b+")



  
#why I should put it inside the block not outside the block
userName=input("Type your name:")  
computer =int(input("computer: "))
english = int(input("english:"))
Account = int(input("Account: "))
nepali=int(input("Nepali: "))
business=int(input("business: "))   
operator=input("press enter to find the result: ")
             
mark = markSheet(computer, Account, english, nepali, business, operator, userName)
mark.markk()
# print(mark.total())

print("_____________________________________________________________________________________________________________________________________________________________________________")
print("")
print("subjects                              fullmarks                      obtained marks               G.P.A")
print("Account **************************** 100 **********************",mark.Account,"*************************",mark.accountG )
print("Business *************************** 100 **********************",mark.business,"************************",mark.businessG)
print
print("_______________________________________________________________________________________________________________________________________________________________________________")
print("")
print("********************************************************************************************************************************************************************************************")
print("")
print(mark.userName," Marksheet is prepared.")
print("")
print("*****************************************************************************************************************************************************************************************")
print("obtained marks:",mark.total)
print("Total percentage:",mark.percentage)
print("G.P.A:",mark.gpa)
print(mark.userName," can do better than this . ")
print("")
print("do you want to make another marksheet for another students:")


