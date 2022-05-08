'''
Scripted by: Hari P. Bhatta
Title:
Billings | Dashboard: Mistake in return amount calculation for Cash Sale.

Description:
Issue : Return amount is not subtracted from Subtotal.

Steps to reproduce:
1. Navigate to the billing>make cash sales.
2. Now make sale return and check the billing dashboard.

Expected result:
The total amount in the billing dashboard(cash sales should be the subtract of subtotal amount and return amount).
Actual result:
The total amount is equal to the sub total amount(cash sales). This cause the calculation error in the net cash collection.

Test environment: http://202.51.74.168:168/

Version: SCH_V2.1.7-B
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LP
import Library.LibModuleADT as LADT
import Library.LibModuleSettings as LS
########
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
########
# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
########
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno

opdticket = GSV.opdRate
discountpct = 50
#discountamount = (discountpct*opdticket/100)
returnamount = opdticket
usgtest = GSV.USG
usgprice = GSV.usgRate
admisioncharge = GSV.admitRate
deposit = 1000
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
########
EMR = AC.openBrowser()
########
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
AC.logout()
AC.login(GSV.foUserID, GSV.foUserPwD)
########
LB.counteractivation(EMR)
########
# 1. Cash Invoice
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')  # cash = opdticket
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=opdticket, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 2. Return Cash Invoice
print("2. Return Cash Invoice")
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo, returnmsg="This is cash invoice return")
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=returnamount, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 3. Cash Discount Invoice
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
HospitalNo1, InvoiceNo1, discountPercentage1 = LA.patientquickentry(danpheEMR=EMR, discountScheme=50, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=opdticket, discountpc=discountpct, cashReturn=0, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

# 4. Return Cash Discount Invoice
LBR.getBillingDashboard(EMR)
LBR.preSystemDataBillingDashboard()
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo1, returnmsg="This is cash discount invoice return")
LBR.getBillingDashboard(EMR)
LBR.verifyBillingDashboard(cash=0, discountpc=discountpct, cashReturn=returnamount, credit=0, creditReturn=0,
                            settlement=0, provisional=0, provisionalcancel=0)

print(" EMR-2571: is existing bug to cancel provisional bill")
AC.logout()
AC.closeBrowser()
#End of the test case




