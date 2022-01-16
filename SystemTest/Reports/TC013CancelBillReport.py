import time
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC

import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
import Library.LibModuleADT as LADT
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
priceCategoryType = "Normal"
user = GSV.foUserID
USG = GSV.USG
TotalAmt = GSV.usgRate
#
opdRate = GSV.opdRate
#AC.applicationSelection()
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType).HospitalNo
LADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, trasfer=0, deposit=0,HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno)
LB.createIPprovisionalBill(danpheEMR=EMR, HospitalNo=HospitalNo, test=USG)
LB.cancelIPprovisionalBill(danpheEMR=EMR, HospitalNo=HospitalNo, canceltest=USG)
LBR.verifyCancelBillReport(danpheEMR=EMR, HospitalNo=HospitalNo, expectedTotalAmt=TotalAmt)
AC.logout()
AC.closeBrowser()