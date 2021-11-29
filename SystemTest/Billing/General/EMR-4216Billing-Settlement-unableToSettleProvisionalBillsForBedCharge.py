from Library import ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
from Library import LibModuleBilling as LB
from Library import LibModuleAppointment as LA

import time

# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.foUserPwD
opdAmt = GSV.opdRate
user = GSV.foUserID


AC.applicationSelection()
AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation()
time.sleep(2)
HospitalNo = LA.patientquickentry(0, 'Credit', GSV.departmentGyno, GSV.doctorGyno).HospitalNo
LB.createProvisionalBill(HospitalNo, usgtest=GSV.bed)
LB.createlabxrayinvoice('Credit', HospitalNo, GSV.USG, GSV.xray)
time.sleep(2)
LB.creditSettlements(HospitalNo, ProvisionalSlip="Yes")
AC.logout()
AC.closeBrowser()
