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
import Library.LibModuleSettings as LS
#front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
###
itemprice = GSV.admitRate
doctor = GSV.doctorGyno
department = GSV.departmentGyno
########
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
LB.counteractivation(EMR)
HospitalNo = LPP.patientRegistration(EMR)
LADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, trasfer=0, HospitalNo=HospitalNo, deposit=0, doctor=GSV.doctorGyno, department=GSV.departmentGyno, admittingDoctorMandatory=isDoctorMandatory)
LB.generateDischargeInvoice(danpheEMR=EMR, creditOrganization=GSV.creditOrganization, HospitalNo=HospitalNo, paymentmode='CREDIT')
LB.creditSettlements(danpheEMR=EMR, creditOrganization=GSV.creditOrganization, HospitalNo=HospitalNo, ProvisionalSlip='No', cashdiscount=0)
AC.logout()
AC.closeBrowser()
