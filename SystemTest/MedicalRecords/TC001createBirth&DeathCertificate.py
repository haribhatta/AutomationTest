import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleMedicalRecords as LMR
import Library.LibModuleADT as ADT
EMR = AC.openBrowser()
#############
# front desk user login
MRUserId = GSV.adminUserID
MRUserPwd = GSV.adminUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
############
AC.login(MRUserId, MRUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
#can.verifyopdinvoice(deposit=0, billamt=500)
print("Status:Passed - > TC001 CreateAppointmentNew")
ADT.admitDisTrans(EMR, 1, 0, 0, HospitalNo, 0, doctorGynae, departmentGynae)

certNo = LMR.addBirthCertificate(danpheEMR=EMR, HospitalNo=HospitalNo)
LMR.verifyaddbirthCertificate(EMR, certNo)
ADT.admitDisTrans(EMR, 0, 1, 0, HospitalNo, 0, doctorGynae, departmentGynae)
LMR.addMRwithDischargeTypeDeath(EMR, HospitalNo)

#1/ Create Birth Certificate
#2. Verify Birth Certificate
#3/ Create Death Certificate
#4. Verify Death Certificate

AC.logout()
AC.closeBrowser()


