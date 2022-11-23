'''
Objective:
To test below scenario:
1. Work flow of inpatient cash invoice return.
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
Deposit = GSV.deposit
Doctor = GSV.doctorGyno
Department = GSV.departmentGyno
########
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
#AC.logout()
#AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LPP.patientRegistration(EMR)
LADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, transfer=0, HospitalNo=HospitalNo, deposit=0, doctor=GSV.doctorGyno, department=GSV.departmentGyno, admittingDoctorMandatory=isDoctorMandatory)
InvoiceNo = LB.generateDischargeInvoice(danpheEMR=EMR, HospitalNo=HospitalNo, paymentmode="Cash")
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo, returnmsg="Discharge bill return")
#LADT.cancelDischarge(danpheEMR=EMR, HospitalNo=HospitalNo) ## Cancel Discharge from ADT feature is no more available, need to return discharge bill.
# Test script is failing due to bug: EMR-2769

