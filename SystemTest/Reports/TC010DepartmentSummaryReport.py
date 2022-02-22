'''
Objective:
To test Department Summary Report with below check points:
1.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.adminUserPwD
opdRae = GSV.opdRate
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
LBR.getDepartmentSummary(EMR)
LBR.preSystemDepartmentSummary()
InvoiceNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).InvoiceNo
LBR.getDepartmentSummary(EMR)
LBR.verifyDepartmentSummary(cash=opdRae, cashReturn=0, credit=0, creditReturn=0, discount=0, provisional=0, provisionalCancel=0)
LB.returnBillingInvoice(EMR, InvoiceNo, "This is cash return.")
LBR.preSystemDepartmentSummary()
LBR.getDepartmentSummary(EMR)
LBR.verifyDepartmentSummary(cash=0, cashReturn=opdRae, credit=0, creditReturn=0, discount=0, provisional=0, provisionalCancel=0)
InvoiceNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Credit', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).InvoiceNo
LBR.preSystemDepartmentSummary()
LBR.getDepartmentSummary(EMR)
LBR.verifyDepartmentSummary(cash=0, cashReturn=0, credit=opdRae, creditReturn=0, discount=0, provisional=0, provisionalCancel=0)
LB.returnBillingInvoice(EMR, InvoiceNo, "This is credit return.")
LBR.preSystemDepartmentSummary()
LBR.getDepartmentSummary(EMR)
LBR.verifyDepartmentSummary(cash=0, cashReturn=0, credit=0, creditReturn=opdRae, discount=0, provisional=0, provisionalCancel=0)
AC.logout()
AC.closeBrowser()
