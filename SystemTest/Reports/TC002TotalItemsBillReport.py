'''
Objective:
To test Total Items Billing Reports with below scenarios:
1. CAH Alwa
2. Return Cash sales
3. Credit Sales
4. Return Credit Sales

'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LP
import Library.LibModuleADT as LADT
import time

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
opdAmt = GSV.opdRate
user = GSV.foUserID

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
time.sleep(2)
######## 1.Cash Sales
InvoiceNo = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno).InvoiceNo
LBR.getTotalItemsBill(EMR)
LBR.preSystemTotalItemsBill()
######## 2.Return Cash Sales
LB.returnBillingInvoice(EMR, InvoiceNo, "This is cash return.")
LBR.getTotalItemsBill(EMR)
LBR.verifyTotalItemsBill(returnamt=opdAmt)
time.sleep(2)
AC.logout()
AC.closeBrowser()
