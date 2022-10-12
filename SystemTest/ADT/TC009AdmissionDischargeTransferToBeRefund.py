#-------------Objective of this script----------
# To verify admission, transfer and discharge of newly registered patient. Patient has to get refund money from deposit left.

from Library import ApplicationConfiguration as AC
from Library import LibModuleBilling as LB
from Library import LibModulePatientPortal as LPP
from Library import LibModuleADT as ADT
from Library import LibModuleAppointment as LA
from Library import GlobalShareVariables as GSV
import Library.LibModuleSettings as LS

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# admin  user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
###
doctor = GSV.doctorGyno
department = GSV.departmentGyno

#------------Local Veriables-------------------
labitem = GSV.UrineRE
imagingitem = GSV.USG
deposit = 1000
admitCharge = GSV.admitRate

#-------------Script Owner: Hari----------------
#Scripted on: 10.05.2077

EMR = AC.openBrowser()
#Check application default added items for admitted patient
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
LS.checkAutoAddItems(danpheEMR=EMR)
AC.logout()
AC.login(foUserId, foUserPwd)
HospitalNo = LPP.patientRegistration(danpheEMR=EMR)
LB.counteractivation(danpheEMR=EMR)
LS.paymentModeOpBillingDisplaySequence(EMR)
LB.createlabxrayinvoice(danpheEMR=EMR, HospitalNo=HospitalNo, labtest=labitem, imagingtest=imagingitem)
ADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, trasfer=0, deposit=deposit, HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=isDoctorMandatory)
LB.billingIP(danpheEMR=EMR, HospitalNo=HospitalNo, admitCharge=admitCharge, deposit=deposit)
LB.verifyDuplicateBill(danpheEMR=EMR, HospitalNo=HospitalNo)
AC.logout()
AC.closeBrowser()
print("There is an existing bug for this test case: EMR-2547")
