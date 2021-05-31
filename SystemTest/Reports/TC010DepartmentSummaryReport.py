from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

dsr = A()

dsr.openBrowser()
dsr.login(foUserId, foUserPwd)
dsr.counteractivation()
dsr.getDepartmentSummary()
dsr.patientquickentry(0, 'Cash')
dsr.preSystemDepartmentSummary()
dsr.getDepartmentSummary()
dsr.verifyDepartmentSummary(cash=500, cashreturn=0, credit=0, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
dsr.returnBillingInvoice("This is cash return.")
dsr.preSystemDepartmentSummary()
dsr.getDepartmentSummary()
dsr.verifyDepartmentSummary(cash=0, cashreturn=500, credit=0, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
dsr.patientquickentry(0, 'CREDIT')
dsr.preSystemDepartmentSummary()
dsr.getDepartmentSummary()
dsr.verifyDepartmentSummary(cash=0, cashreturn=0, credit=500, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
dsr.returnBillingInvoice("This is credit return.")
dsr.preSystemDepartmentSummary()
dsr.getDepartmentSummary()
dsr.verifyDepartmentSummary(cash=0, cashreturn=0, credit=0, creditreturn=500, discount=0, provisional=0, provisionalcancel=0)
dsr.logout()
dsr.closeBrowser()
