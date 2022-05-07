''''
Objective: Return Happy Path
The AIM of this test script is to test below scenarios:
1. Create an appointment for new patient.
2. Return above visit invoice.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA

#AC.applicationSelection()
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
# 1. Create an appointment for new patient.
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
print("Status:Passed - > TC001 CreateAppointmentNew")
# 2. Create an appointment for old patient.
#LB.getBillingDashboard()
LB.returnBillingInvoice(EMR, InvoiceNo=InvoiceNo, returnmsg='This is cash return')
#rvi.preSystemDataBillingDashboard()
#rvi.getBillingDashboard()
#rvi.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=OPD, credit=0, creditReturn=0, settlement=0, provisional=0
#                           , provisionalcancel=0)
AC.logout()
AC.closeBrowser()
