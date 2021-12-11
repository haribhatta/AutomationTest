'''
Objective:
To test below scenario:
1. Work flow of ip patient credit settlement
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
import Library.LibModuleADT as LADT
import Library.LibModulePatientPortal as LPP

#front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD


itemprice = GSV.admitRate
doctor = GSV.doctorGyno
department = GSV.departmentGyno

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LPP.patientRegistration()
LADT.admitDisTrans(danpheEMR=EMR, HospitalNo=HospitalNo, admit=1, discharge=0, trasfer=0, deposit=0,doctor=0,department=0)
paymode = "CREDIT"
LB.generateDischargeInvoice(danpheEMR=EMR, HospitalNo=HospitalNo, paymentmode = paymode)
LB.creditSettlements(danpheEMR=EMR, HospitalNo=HospitalNo)
AC.logout()
AC.closeBrowser()
