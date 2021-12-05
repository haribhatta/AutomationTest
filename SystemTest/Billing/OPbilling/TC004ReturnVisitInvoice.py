''''
Objective: Return Happy Path
The AIM of this test script is to test below scenarios:
1. Create an appointment for new patient.
2. Return above visit invoice.
'''
import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA

AC.applicationSelection()
AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation()
# 1. Create an appointment for new patient.
InvoiceNo = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).InvoiceNo
print("Status:Passed - > TC001 CreateAppointmentNew")
# 2. Create an appointment for old patient.
#LB.getBillingDashboard()
LB.returnBillingInvoice(InvoiceNo=InvoiceNo, returnmsg='This is cash return')
#rvi.preSystemDataBillingDashboard()
#rvi.getBillingDashboard()
#rvi.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=OPD, credit=0, creditReturn=0, settlement=0, provisional=0
#                           , provisionalcancel=0)
AC.logout()
AC.closeBrowser()
