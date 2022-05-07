'''
Objective:
To test below checkpoints:
1. return out patient cash invoice.
2. verify return invoice is correctly generated.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
paymode = "Cash"
itemrate = GSV.opdRate
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage= LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
LB.returnBillingInvoice(EMR, InvoiceNo, returnmsg="This is test return")
LB.verifyReturnBillingInvoice(EMR, InvoiceNo, itemrate)
AC.logout()
AC.closeBrowser()