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

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

Deposit = GSV.deposit
Doctor = GSV.doctorGyno
Department = GSV.departmentGyno

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LPP.patientRegistration()
LADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, trasfer=0, HospitalNo=HospitalNo, deposit=Deposit, doctor=Doctor, department=Department)
paymode = "Cash"
LB.generateDischargeInvoice(danpheEMR=EMR, HospitalNo=HospitalNo, paymentmode=paymode)
LADT.cancelDischarge(danpheEMR=EMR, HospitalNo=HospitalNo)
# Test script is failing due to bug: EMR-2769

