from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

tibr = A()
itemname = GSV.LDH

tibr.openBrowser()
tibr.login(foUserId, foUserPwd)
tibr.counteractivation()
tibr.insurancePatientRegistration()
tibr.insuranceNewVisit()
#tibr.insuranceBilling(itemname)
#tibr.getInsuranceTotalItemsBill()
#tibr.returnInsuranceBillingInvoice("This is cash return.")

#tibr.preSystemInsuranceTotalItemsBill()
#tibr.getInsuranceTotalItemsBill()
#tibr.verifyInsuranceTotalItemsBill(returnamt=500, discountamt=0)
#tibr.logout()
#tibr.closeBrowser()
