import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
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
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
LBR.getTotalItemsBill(EMR)
LBR.preSystemTotalItemsBill()
LB.returnBillingInvoice(EMR, InvoiceNo, "This is cash return.")
LBR.getTotalItemsBill(EMR)
LBR.verifyTotalItemsBill(returnamt=opdAmt)
time.sleep(2)
AC.logout()
AC.closeBrowser()
