from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

tibr = A()

tibr.openBrowser()
tibr.login(foUserId, foUserPwd)
tibr.counteractivation()
tibr.patientquickentry(0, 'Cash')
tibr.getTotalItemsBill()
tibr.returnBillingInvoice("This is cash return.")
tibr.preSystemTotalItemsBill()
tibr.getTotalItemsBill()
tibr.verifyTotalItemsBill(returnamt=500, discountamt=0)
tibr.logout()
tibr.closeBrowser()
