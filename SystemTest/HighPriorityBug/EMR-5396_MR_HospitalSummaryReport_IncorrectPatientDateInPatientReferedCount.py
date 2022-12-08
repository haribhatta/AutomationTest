import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleMedicalRecordsReports as LMRR
import Library.LibModuleMedicalRecords as LM

adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
########
opdAmt = GSV.opdRate
user = GSV.foUserID
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
LM.OutpatientList(danpheEMR=EMR, HospitalNo=HospitalNo, DoctorName=doctorGynae)
LM.addFinalDiagnosisOutPatient(danpheEMR=EMR, isReferredOutpatient="yes", diagnosis=GSV.dianosis1)
LMRR.getHospitalServiceSummaryReport(EMR)
LMRR.preHospitalServiceSummaryReport()
LM.OutpatientList(danpheEMR=EMR, HospitalNo=HospitalNo, DoctorName=doctorGynae)
LM.editFinalDiagnosisOutPatient(danpheEMR=EMR, diagnosis=GSV.dianosis2)
LMRR.getHospitalServiceSummaryReport(danpheEMR=EMR)
LMRR.verifyReferredOutPatientAfterUpdate()
print("This isuue will be blocked if EMR-5393 still exists")
AC.logout()
AC.closeBrowser()
