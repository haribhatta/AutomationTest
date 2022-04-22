#Tested Scenarios:
#  Same Day
# 1.Cash Invoice,
# 2.Return Cash Invoice,
# 3.Credit Invoice,
# 4.Return Credit Invoice,
# 5. Credit Payment,
# 6.Provisional billing,
# 7.Cancel Provisional bill,
# 8.Deposit,
# 9.Deduct Deposit,
# 10.Refund Deposit.
# 11.Repeat Scenarios 1-10 for different date.

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.foUserPwD
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Credit', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
InvoiceNo1 = LB.createCreditLabInvoice(danpheEMR=EMR, HospitalNo=HospitalNo, labtest=GSV.USG)
print(InvoiceNo1)
LBR.getPatientCreditSummary(EMR, invoiceNo=InvoiceNo1)
AC.logout()
AC.closeBrowser()