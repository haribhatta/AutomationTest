from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

usgtest = GSV.USG
usgprice = GSV.usgRate

CPB = A()
CPB.openBrowser()
CPB.login(foUserId, foUserPwd)
CPB.counteractivation()
CPB.getBillingDashboard()
CPB.patientRegistration()
CPB.createProvisionalBill(usgtest)  #provisional=usgprice
CPB.preSystemDataBillingDashboard()
CPB.getBillingDashboard()
CPB.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0, settlement=0,
                            provisional=usgprice, provisionalcancel=0)
CPB.logout()
CPB.closeBrowser()
