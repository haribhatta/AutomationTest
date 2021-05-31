from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD

ir = A()
paymode = "Cash"
itemprice = GSV.opdRate

# incentive % = 60%

ir.openBrowser()
ir.login(adminUserId, adminUserPwd)
ir.counteractivation()
ir.synchBilingIncentive()
ir.patientquickentry(discountpc=0, paymentmode=paymode)
ir.getIncentiveTransactionReport()
ir.preIncentiveTransactionReport()
ir.synchBilingIncentive()
ir.getIncentiveTransactionReport()
ir.verifyIncentiveTransactionReport(cash=itemprice, credit=0)
ir.logout()
ir.closeBrowser()
