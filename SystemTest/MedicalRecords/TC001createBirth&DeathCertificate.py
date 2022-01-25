import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleMedicalRecords as LMR
import Library.LibModuleADT as LADT

EMR = AC.openBrowser()
#############
# front desk user login
MRUserId = GSV.MRUserID
MRUserPwd = GSV.MRUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
###
foUserID = GSV.foUserID
foUserPwd = GSV.foUserPwD
#############
AC.login(foUserID, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
LADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, trasfer=0, HospitalNo=HospitalNo, deposit=0, doctor=doctorGynae, department=departmentGynae)
#can.verifyopdinvoice(deposit=0, billamt=500)
print("Status:Passed - > TC001 CreateAppointmentNew")
AC.logout()
AC.login(MRUserId, MRUserPwd)
LMR.addBirthCertificate(danpheEMR=EMR, HospitalNo=HospitalNo)
AC.logout()
AC.login(foUserID, foUserPwd)
LB.counteractivation(EMR)
LADT.admitDisTrans(danpheEMR=EMR, admit=0, discharge=1, trasfer=0, HospitalNo=HospitalNo, deposit=0, doctor=doctorGynae, department=departmentGynae)
AC.logout()
AC.login(MRUserId, MRUserPwd)
LMR.addMRwithDischargeTypeDeath(danpheEMR=EMR)
LMR.addDeathCertificate(danpheEMR=EMR, HospitalNo=HospitalNo)
#1/ Create Birth Certificate
#2. Verify Birth Certificate
#3/ Create Death Certificate
#4. Verify Death Certificate
AC.logout()
AC.closeBrowser()
print("Status:Passed - > TC001 oldPatientAppointment")



