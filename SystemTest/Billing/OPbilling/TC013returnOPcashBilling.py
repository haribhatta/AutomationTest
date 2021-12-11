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

paymode = "Cash"
itemrate = GSV.opdRate

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
InvoiceNo = LA.patientquickentry(EMR, discountpc=0, paymentmode=paymode, department=GSV.departmentGyno, doctor=GSV.doctorGyno).InvoiceNo
LB.returnBillingInvoice(EMR, InvoiceNo, returnmsg="This is test return")
LB.verifyReturnBillingInvoice() # this function need to add in LibModuleBilling library file.