'''
Objective: Happy Path of OPD billing.
The AIM of this test script is to verify below scenarios:
1. Create an OPD invoice of - lab item and xray item.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
EMR = AC.openBrowser()

#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
# 1. Create an appointment for new patient.
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType="Normal", case='+ve')
#can.verifyopdinvoice(deposit=0, billamt=500)
print("Status:Passed - > TC001 CreateAppointmentNew")
#oblx.verifyopdinvoice(deposit=0, billamt=500)
LBR.getPaymentWiseReport(danpheEMR=EMR)
LBR.storePaymentWiseReport()
totalPrice = LB.createlabxrayinvoiceOtherPayment(danpheEMR=EMR, HospitalNo=HospitalNo, labtest=GSV.TFT, imagingtest=GSV.USG)
#oblx.verifylabxrayinvoice()
print("Total Price is :", totalPrice)
LBR.getPaymentWiseReport(danpheEMR=EMR)
LBR.verifyPaymentWiseReport(totalPrice=totalPrice)
AC.logout()
AC.closeBrowser()
print("Status:Passed -> TC002OPDbillingLabXray.py")
