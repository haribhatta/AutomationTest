import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LP
import Library.LibModuleADT as LADT
import time

# front desk user login
itUserId = GSV.itUserID
itUserPwd = GSV.itUserPwD
opdAmt = GSV.opdRate
user = GSV.foUserID
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(itUserId, itUserPwd)
LB.counteractivation(EMR)
time.sleep(2)
InvoiceNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).InvoiceNo
LBR.getTotalItemsBill(EMR)
LBR.preSystemTotalItemsBill()
LB.returnBillingInvoice(EMR, InvoiceNo, "This is cash return.")
LBR.getTotalItemsBill(EMR)
LBR.verifyTotalItemsBill(returnamt=opdAmt)
time.sleep(2)
AC.logout()
AC.closeBrowser()
