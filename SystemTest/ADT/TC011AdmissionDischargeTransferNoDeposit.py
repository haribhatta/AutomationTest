#-------------Objective of this script----------
# To verify admission, transfer and discharge of newly registered patient. Patient has to get refund money from deposit left.

from Library import ApplicationConfiguration as AC
from Library import LibModuleBilling as LB
from Library import LibModuleADT as ADT
from Library import LibModuleAppointment as LA
from Library import GlobalShareVariables as GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

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
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode="Cash", department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType).HospitalNo
LB.createlabxrayinvoice(danpheEMR=EMR, HospitalNo=HospitalNo, labtest=labitem, imagingtest=imagingitem)
ADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, trasfer=0, deposit=deposit,HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno)
LB.billingIP(danpheEMR=EMR, HospitalNo=HospitalNo, admitCharge=admitcharge, deposit=deposit)
AC.logout()
AC.closeBrowser()
