import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleInsurance as LIC
import Library.LibModuleBilling as LB
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

itemname = GSV.LDH

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
LIC.insurancePatientRegistration()
LIC.insuranceNewVisit()
#tibr.insuranceBilling(itemname)
#tibr.getInsuranceTotalItemsBill()
#tibr.returnInsuranceBillingInvoice("This is cash return.")

#tibr.preSystemInsuranceTotalItemsBill()
#tibr.getInsuranceTotalItemsBill()
#tibr.verifyInsuranceTotalItemsBill(returnamt=500, discountamt=0)
#tibr.logout()
#tibr.closeBrowser()
