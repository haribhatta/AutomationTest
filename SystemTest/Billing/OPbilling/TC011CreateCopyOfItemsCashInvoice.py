from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

bil = A()
bil.openBrowser()
bil.login(foUserId, foUserPwd)
bil.counteractivation()
bil.patientquickentry(0, 'Cash')
bil.returnBillingInvoice("This is cash return 1.")
bil.createCopyItemInvoice('Cash')
bil.returnBillingInvoice("This is cash return 2.")
bil.createCopyItemInvoice('CREDIT')
bil.logout()
bil.closeBrowser()
