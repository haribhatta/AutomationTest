'''
TC_Smoke_TC002: Do IP Patient Billing (non Insurance - Lab, Radiology and Discharge).
'''

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleADT as LADT

AC.applicationSelection()
AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
labTestTFT = GSV.TFT
labTestTFTrate = GSV.TFTRate
radioTestUSG = GSV.USG
paymode = 'Cash'
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation()
HospitalNo = LA.patientquickentry(0, 'Cash',department=departmentGynae, doctor=doctorGynae).HospitalNo
LADT.admitDisTrans(admit=1, discharge=0, trasfer=0, hospitalNO=HospitalNo, deposit=0,doctor=doctorGynae, department=departmentGynae)
#LB.getIPbillingDetails(HospitalNo=HospitalNo, paymentmode=paymode)
#LB.preIPbillingDetails()
LB.createIPprovisionalBill(HospitalNo=HospitalNo, test=labTestTFT)
#LB.getIPbillingDetails(HospitalNo=HospitalNo, paymentmode=paymode)
#LB.verifyIPbillingDetails(testrate=labTestTFTrate, canceltest=labTestTFT, paymentmode=paymode)
#LB.preIPbillingDetails()
#LB.preIPbillingDetails()
LB.cancelIPprovisionalBill(HospitalNo, labTestTFT)
#LB.getIPbillingDetails(HospitalNo, paymode)
#LB.verifyIPbillingDetails(labTestTFTrate, labTestTFT, paymode)
#LB.preIPbillingDetails()
#LB.modifyDischargeDate(HospitalNo)
#LB.getIPbillingDetails(HospitalNo, paymode)
#LB.verifyIPbillingDetails(testrate = 0, canceltest = 0, paymentmode=paymode)
#LB.verifyConfirmDischarge(HospitalNo, paymode)
#LB.verifyDischargeInvoice(paymentmode=paymode)
AC.logout()
AC.closeBrowser()



