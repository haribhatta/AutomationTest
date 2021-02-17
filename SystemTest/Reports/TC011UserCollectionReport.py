from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

uc = A()
user = 'Ms. Billing Billing'

uc.openBrowser()
uc.login(foUserId, foUserPwd)
uc.counteractivation()
uc.getUserCollectionReport(user)
uc.patientquickentry(0, 'Cash')
uc.preSystemUserCollectionReport()
uc.getUserCollectionReport(user)
uc.verifyUserCollectionReport(cash=500, cashreturn=0, credit=0, creditreturn=0, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
uc.returnBillingInvoice("This is cash return.")
uc.preSystemUserCollectionReport()
uc.getUserCollectionReport(user)
uc.verifyUserCollectionReport(cash=0, cashreturn=500, credit=0, creditreturn=0, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
uc.patientquickentry(0, 'CREDIT')
uc.preSystemUserCollectionReport()
uc.getUserCollectionReport(user)
uc.verifyUserCollectionReport(cash=0, cashreturn=0, credit=500, creditreturn=0, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
uc.returnBillingInvoice("This is credit return.")
uc.preSystemUserCollectionReport()
uc.getUserCollectionReport(user)
uc.verifyUserCollectionReport(cash=0, cashreturn=0, credit=0, creditreturn=500, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
uc.logout()
uc.closeBrowser()
