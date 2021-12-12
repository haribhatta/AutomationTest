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
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
opdRae = GSV.opdRate

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
LBR.getDepartmentSummary(EMR)
LBR.preSystemDepartmentSummary()
InvoiceNo = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno).InvoiceNo
LBR.getDepartmentSummary(EMR)
LBR.verifyDepartmentSummary(cash=opdRae, cashreturn=0, credit=0, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
LB.returnBillingInvoice(EMR, InvoiceNo, "This is cash return.")
LBR.preSystemDepartmentSummary()
LBR.getDepartmentSummary(EMR)
LBR.verifyDepartmentSummary(cash=0, cashreturn=opdRae, credit=0, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
InvoiceNo = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode='Credit', department=GSV.departmentGyno, doctor=GSV.doctorGyno).InvoiceNo
LBR.preSystemDepartmentSummary()
LBR.getDepartmentSummary(EMR)
LBR.verifyDepartmentSummary(cash=0, cashreturn=0, credit=opdRae, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
LB.returnBillingInvoice(EMR, InvoiceNo, "This is credit return.")
LBR.preSystemDepartmentSummary()
LBR.getDepartmentSummary(EMR)
LBR.verifyDepartmentSummary(cash=0, cashreturn=0, credit=0, creditreturn=opdRae, discount=0, provisional=0, provisionalcancel=0)
AC.logout()
AC.closeBrowser()
