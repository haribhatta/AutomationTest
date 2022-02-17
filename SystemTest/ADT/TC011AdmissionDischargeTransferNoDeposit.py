#-------------Objective of this script----------
# To verify admission, transfer and discharge of newly registered patient. Patient has to get refund money from deposit left.

from Library import ApplicationConfiguration as AC
from Library import LibModuleBilling as LB
from Library import LibModuleADT as ADT
from Library import LibModuleAppointment as LA
from Library import GlobalShareVariables as GSV
from Library import LibModuleSettings as LS
########
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
#------------Local Veriables-------------------
labitem = GSV.UrineRE
imagingitem = GSV.USG
deposit = 0
admitcharge = GSV.admitRate
doctor = GSV.doctorGyno
department = GSV.departmentGyno
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
#-------------Script Owner: Hari----------------
#Scripted on: 10.05.2077

EMR = AC.openBrowser()
######## Precondition Check: isAdmittingDoctorMandatory?
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGparameter(danpheEMR=EMR)
AC.logout()
########
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode="Cash", department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).HospitalNo
LB.createlabxrayinvoice(danpheEMR=EMR, HospitalNo=HospitalNo, labtest=labitem, imagingtest=imagingitem)
ADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, trasfer=0, deposit=deposit,HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=isDoctorMandatory)
LB.billingIP(danpheEMR=EMR, HospitalNo=HospitalNo, admitCharge=admitcharge, deposit=deposit)
AC.logout()
AC.closeBrowser()
