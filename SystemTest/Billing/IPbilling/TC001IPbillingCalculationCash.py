'''
TC_Smoke_TC002: Do IP Patient Billing (non Insurance - Lab, Radiology and Discharge).
Scenarios to test:
1. Create OP visit.
2. Admit above patient.
3. Do lab & xray billing for above inpatient.
4. Discharge the patient with payment mode cash.
'''
######## Import Libraries

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleADT as LADT
########
#AC.applicationSelection()
########
EMR = AC.openBrowser()
########
AC.login(GSV.foUserID, GSV.foUserPwD)
########
LB.counteractivation(EMR)
######## 1. Create OP visit.
HospitalNo = LA.patientquickentry(EMR, 0, 'Cash',department=GSV.departmentGyno, doctor=GSV.doctorGyno).HospitalNo
######## 2. Admit above patient.
LADT.admitDisTrans(EMR, admit=1, discharge=0, trasfer=0, hospitalNO=HospitalNo, deposit=0,doctor=GSV.doctorGyno, department=GSV.departmentGyno)
#LB.getIPbillingDetails(HospitalNo=HospitalNo, paymentmode=paymode)
#LB.preIPbillingDetails()
LB.createIPprovisionalBill(EMR, HospitalNo=HospitalNo, test=GSV.TFT)
#LB.getIPbillingDetails(HospitalNo=HospitalNo, paymentmode=paymode)
#LB.verifyIPbillingDetails(testrate=labTestTFTrate, canceltest=labTestTFT, paymentmode=paymode)
#LB.preIPbillingDetails()
LB.createIPprovisionalBill(EMR, HospitalNo=HospitalNo, test=GSV.USG)
#LB.getIPbillingDetails(HospitalNo=HospitalNo, paymentmode=paymode)
#LB.verifyIPbillingDetails(testrate=labTestTFTrate, canceltest=labTestTFT, paymentmode=paymode)
#LB.preIPbillingDetails()
#LB.cancelIPprovisionalBill(HospitalNo, labTestTFT)
#LB.getIPbillingDetails(HospitalNo, paymode)
#LB.verifyIPbillingDetails(labTestTFTrate, labTestTFT, paymode)
#LB.preIPbillingDetails()
#LB.modifyDischargeDate(HospitalNo)
#LB.getIPbillingDetails(HospitalNo, paymode)
#LB.verifyIPbillingDetails(testrate = 0, canceltest = 0, paymentmode=paymode)
LB.verifyConfirmDischarge(EMR, HospitalNo, 'Cash')
LB.verifyDischargeInvoice(EMR, paymentmode= 'Cash')
AC.logout()
AC.closeBrowser()



