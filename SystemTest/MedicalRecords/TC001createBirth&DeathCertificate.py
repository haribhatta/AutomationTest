import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleMedicalRecords as LMR

EMR = AC.openBrowser()
#############
# front desk user login
MRUserId = GSV.MRUserID
MRUserPwd = GSV.MRUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
#############
AC.login(MRUserId, MRUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).HospitalNo
#can.verifyopdinvoice(deposit=0, billamt=500)
print("Status:Passed - > TC001 CreateAppointmentNew")
LMR.addBirthCertificate(HospitalNo)
#1/ Create Birth Certificate
#2. Verify Birth Certificate
#3/ Create Death Certificate
#4. Verify Death Certificate

AC.logout()
AC.closeBrowser()
print("Status:Passed - > TC001 oldPatientAppointment")


