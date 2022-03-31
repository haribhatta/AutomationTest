import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleMedicalRecords as LMR
import Library.LibModuleADT as ADT
import Library.LibModuleSettings as LS
#############
# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
########
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
########
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType)
#can.verifyopdinvoice(deposit=0, billamt=500)
print("Status:Passed - > TC001 CreateAppointmentNew")
ADT.admitDisTrans(EMR, 1, 0, 0, HospitalNo, 0, doctorGynae, departmentGynae, isDoctorMandatory)
ADT.admitDisTrans(EMR, 0, 1, 0, HospitalNo, 0, doctorGynae, departmentGynae, isDoctorMandatory)
LMR.addBirthDetailsFromMRInpatientList(danpheEMR=EMR, HospitalNo=HospitalNo, babyWeight=10)
LMR.editBirthDetailsfromMRInpatientList(danpheEMR=EMR, editedWeight=3.5)
AC.logout()
AC.closeBrowser()