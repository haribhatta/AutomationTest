import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.adminUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.departmentGyno
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType="Normal")
LB.returnBillingInvoice(EMR, InvoiceNo, "This is credit bill return")
LB.createCopyItemInvoice(EMR, 'CREDIT')
LB.returnBillingInvoice(EMR, InvoiceNo,  "This is copy bill return")
LB.createCopyItemInvoice(EMR, 'Cash')
AC.logout()
AC.closeBrowser()
