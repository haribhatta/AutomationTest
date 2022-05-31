'''
Objective:
To test high priority bug EMR-4216:

'''
import Library.GlobalShareVariables as GSV
from Library import ApplicationConfiguration as AC
from Library import LibModuleBilling as LB
from Library import LibModuleAppointment as LA
import time     


# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.foUserPwD
opdAmt = GSV.opdRate
user = GSV.foUserID

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
time.sleep(2)
paymode = "Credit"
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode=paymode, department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType="Normal", case="+ve")
LB.createProvisionalBill(EMR, HospitalNo, usgtest=GSV.USG)
time.sleep(2)
LB.creditSettlements(EMR, HospitalNo=HospitalNo, ProvisionalSlip="Yes", cashdiscount=0)
AC.logout()
AC.closeBrowser()
