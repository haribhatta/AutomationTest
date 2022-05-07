import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LP
import Library.LibModuleADT as LADT
import Library.LibModuleMedicalRecordsReports as LMRR
import Library.LibModuleADT as ADT
import time
import Library.LibModuleSettings as LS

# MR user login
mrUserId = GSV.MRUserID
mrUserPwd = GSV.MRUserPwD
# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
########
opdAmt = GSV.opdRate
user = GSV.foUserID
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
TFT = GSV.TFT
########
EMR = AC.openBrowser()
########
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
AC.logout()
AC.login(mrUserId, mrUserPwd)
########
### Check for 'Total Laboratory Service Provided'
LB.counteractivation(EMR)
LMRR.getHospitalServiceSummaryReport(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
LB.createLabInvoice(danpheEMR=EMR, HospitalNo=HospitalNo, labtest=TFT)
LMRR.preHospitalServiceSummaryReport(EMR)
LMRR.getHospitalServiceSummaryReport(EMR)
LMRR.verifyHospitalServiceSummaryReport(danpheEMR=EMR, labBill=1, admit=0)
### Check for 'Total Patients Admitted'
LMRR.preHospitalServiceSummaryReport(EMR)
ADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, trasfer=0, deposit=0, HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=isDoctorMandatory)
LMRR.getHospitalServiceSummaryReport(EMR)
LMRR.verifyHospitalServiceSummaryReport(danpheEMR=EMR, labBill=0, admit=1) ## TestAction: Failed: EMR-4817
time.sleep(2)
AC.logout()
AC.closeBrowser()
