import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.adminUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
InvoiceNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType='Normal').InvoiceNo
LB.returnBillingInvoice(EMR, InvoiceNo, "This is cash return 1.")
LB.createCopyItemInvoice(EMR, 'Cash')
LB.returnBillingInvoice(EMR, InvoiceNo, "This is cash return 2.")
LB.createCopyItemInvoice(EMR, 'CREDIT')
AC.logout()
AC.closeBrowser()
