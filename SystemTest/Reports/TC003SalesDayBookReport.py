from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
rateOPD = 30

vsdbr = A()

vsdbr.openBrowser()
vsdbr.login(foUserId, foUserPwd)
vsdbr.counteractivation()
vsdbr.getSalesDayBook()
vsdbr.patientquickentry(0, 'Cash')
vsdbr.preSystemSalesDayBook()
vsdbr.getSalesDayBook()
vsdbr.verifySalesDayBook(cash=rateOPD, cashreturn=0, credit=0, creditreturn=0)
vsdbr.returnBillingInvoice(returnmsg="this is bill return 1")
vsdbr.preSystemSalesDayBook()
vsdbr.getSalesDayBook()
vsdbr.verifySalesDayBook(cash=0, cashreturn=rateOPD, credit=0, creditreturn=0)

vsdbr.patientquickentry(0, 'CREDIT')
vsdbr.preSystemSalesDayBook()
vsdbr.getSalesDayBook()
vsdbr.verifySalesDayBook(cash=0, cashreturn=0, credit=rateOPD, creditreturn=0)
vsdbr.returnBillingInvoice(returnmsg="this is bill retur 2n")
vsdbr.preSystemSalesDayBook()
vsdbr.getSalesDayBook()
vsdbr.verifySalesDayBook(cash=0, cashreturn=0, credit=0, creditreturn=rateOPD)
vsdbr.logout()
vsdbr.closeBrowser()
