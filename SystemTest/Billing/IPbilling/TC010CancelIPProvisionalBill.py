from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

usgtest = GSV.USG
usgprice = GSV.usgRate
deposit = 0
admisioncharge = GSV.admitRate


CPB = A()
CPB.openBrowser()
CPB.login(foUserId, foUserPwd)

# 9. Cancel Provisional Bill
# 8.2 Provisional IP Bill
CPB.patientRegistration()
CPB.counteractivation()
CPB.dischargeRandomPatient()
CPB.getBillingDashboard()
CPB.admitDisTrans(1, 0, 0, deposit)
CPB.preSystemDataBillingDashboard()
CPB.getBillingDashboard()
CPB.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                          settlement=0, provisional=admisioncharge, provisionalcancel=0)

CPB.createIPprovisionalBill(usgtest)
CPB.preSystemDataBillingDashboard()
CPB.getBillingDashboard()
CPB.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                          settlement=0, provisional=usgprice, provisionalcancel=0)
CPB.getBillingDashboard()
CPB.cancelIPprovisionalBill(usgtest)
CPB.preSystemDataBillingDashboard()
CPB.getBillingDashboard()
CPB.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0, settlement=0,
                            provisional=0, provisionalcancel=usgprice)
CPB.logout()
CPB.closeBrowser()