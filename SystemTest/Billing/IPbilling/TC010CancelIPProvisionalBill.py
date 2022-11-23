'''
Objective:
To test below scenario:
1. Work flow of cancelling estimation bill (provisional bill) of inpatient.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
import Library.LibModuleADT as LADT
import Library.LibModulePatientPortal as LPP
import Library.LibModuleSettings as LS

########
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
########
admisioncharge = GSV.admitRate
Deposit1 = GSV.deposit
Department1 = GSV.departmentGyno
Doctor1 = GSV.doctorGyno

usgtest = GSV.USG
usgprice = GSV.usgRate

priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName

EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
AC.logout()
AC.login(foUserId, foUserPwd)
# 9. Cancel Provisional Bill
# 8.2 Provisional IP Bill
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
LADT.dischargeRandomPatient(danpheEMR=EMR)
LADT.admitDisTrans(danpheEMR=EMR, HospitalNo=HospitalNo, admit=1, discharge=0, transfer=0, deposit=Deposit1, doctor=Doctor1, department=Department1, admittingDoctorMandatory=isDoctorMandatory)
LB.createIPprovisionalBill(danpheEMR=EMR, HospitalNo=HospitalNo, usgtest=usgtest)
LB.cancelIPprovisionalBill(danpheEMR=EMR, HospitalNo=HospitalNo, canceltest=usgtest)
AC.logout()
AC.closeBrowser()