from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

uc = A()
user = GSV.UserBilling

opdRate = GSV.opdRate

uc.openBrowser()
uc.login(foUserId, foUserPwd)
uc.counteractivation()
uc.getUserCollectionReport(user)
uc.patientquickentry(0, 'Cash')
uc.preSystemUserCollectionReport()
uc.getUserCollectionReport(user)
uc.verifyUserCollectionReport(cash=opdRate, cashreturn=0, credit=0, creditreturn=0, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
uc.returnBillingInvoice("This is cash return.")
uc.preSystemUserCollectionReport()
uc.getUserCollectionReport(user)
uc.verifyUserCollectionReport(cash=0, cashreturn=opdRate, credit=0, creditreturn=0, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
uc.patientquickentry(0, 'CREDIT')
uc.preSystemUserCollectionReport()
uc.getUserCollectionReport(user)
uc.verifyUserCollectionReport(cash=0, cashreturn=0, credit=opdRate, creditreturn=0, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
uc.returnBillingInvoice("This is credit return.")
uc.preSystemUserCollectionReport()
uc.getUserCollectionReport(user)
uc.verifyUserCollectionReport(cash=0, cashreturn=0, credit=0, creditreturn=opdRate, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
uc.logout()
uc.closeBrowser()
