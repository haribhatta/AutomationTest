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

# front desk user login
mrUserId = GSV.adminUserID
mrUserPwd = GSV.adminUserPwD
opdAmt = GSV.opdRate
user = GSV.foUserID
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
TFT = GSV.TFT
########
EMR = AC.openBrowser()
AC.login(mrUserId, mrUserPwd)
### Check for 'Total Laboratory Service Provided'
LB.counteractivation(EMR)
LMRR.getHospitalServiceSummaryReport(EMR)
HospitalNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
LB.createLabInvoice(danpheEMR=EMR, HospitalNo=HospitalNo, labtest=TFT)
LMRR.preHospitalServiceSummaryReport(EMR)
LMRR.getHospitalServiceSummaryReport(EMR)
LMRR.verifyHospitalServiceSummaryReport(danpheEMR=EMR, labBill=1, admit=0)
### Check for 'Total Patients Admitted'
LMRR.preHospitalServiceSummaryReport(EMR)
ADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, trasfer=0, deposit=0, HospitalNo=HospitalNo, department=departmentGynae, doctor=doctorGynae)
LMRR.getHospitalServiceSummaryReport(EMR)
LMRR.verifyHospitalServiceSummaryReport(danpheEMR=EMR, labBill=0, admit=1) ## TestAction: Failed: EMR-4817
time.sleep(2)
AC.logout()
AC.closeBrowser()
