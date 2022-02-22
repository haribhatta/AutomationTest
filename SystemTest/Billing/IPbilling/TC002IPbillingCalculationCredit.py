'''
Objective:
To test below scenario:
1. Work flow of normal ip patient (i.e. From patient admission to discharge.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
import Library.LibModuleADT as LADT
import Library.LibModuleSettings as LS
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
AC.logout()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
LADT.dischargeRandomPatient(EMR)  # This action is to free bed to admit new patient (Pre-condition to run test script).
paymode = "CREDIT"
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode=paymode, department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).HospitalNo
LADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, trasfer=0, HospitalNo=HospitalNo, deposit=0, doctor=GSV.doctorGyno, department=GSV.departmentGyno, admittingDoctorMandatory=isDoctorMandatory)
LB.getIPbillingDetails(EMR, HospitalNo, paymode)
LB.preIPbillingDetails(paymentmode="CREDIT")
test1 = GSV.USG
test1rate = GSV.usgRate
### Create IP provisional bill
LB.createIPprovisionalBill(EMR, HospitalNo, test1)
LB.getIPbillingDetails(EMR, HospitalNo, paymode)
LB.verifyIPbillingDetails(testrate=test1rate, canceltest=0, paymentmode=paymode)
LB.preIPbillingDetails(paymentmode="CREDIT")
test2 = GSV.BTCT
test2rate = GSV.btctRate
### Create IP provisional bill
LB.createIPprovisionalBill(EMR, HospitalNo, test2)
LB.getIPbillingDetails(EMR, HospitalNo, paymode)
LB.verifyIPbillingDetails(testrate=test2rate, canceltest=0, paymentmode=paymode)
LB.preIPbillingDetails(paymentmode="CREDIT")
### Cancel IP provisional bill
LB.cancelIPprovisionalBill(EMR, HospitalNo, test2)
LB.getIPbillingDetails(danpheEMR=EMR, HospitalNo=HospitalNo, paymentmode=paymode)
LB.verifyIPbillingDetails(testrate=0, canceltest=test2rate, paymentmode=paymode)
LB.preIPbillingDetails(paymentmode="CREDIT")
LB.modifyDischargeDate(danpheEMR=EMR, HospitalNo=HospitalNo)
LB.getIPbillingDetails(danpheEMR=EMR, HospitalNo=HospitalNo,paymentmode=paymode)
LB.verifyIPbillingDetails(testrate=0, canceltest=0, paymentmode=paymode)
# ''make credit organization non namdatory'''
LB.verifyConfirmDischarge(danpheEMR=EMR, HospitalNo=HospitalNo, paymentmode=paymode)
LB.verifyDischargeInvoice(danpheEMR=EMR, paymentmode=paymode)
AC.logout()
AC.closeBrowser()



