#-------------Objective of this script----------
# To verify admission, transfer and discharge of newly registered patient. Patient has to get refund money from deposit left.

from Library import ApplicationConfiguration as AC
from Library import LibModuleBilling as LB
from Library import LibModuleADT as ADT
from Library import LibModuleAppointment as LA
from Library import GlobalShareVariables as GSV
import Library.LibModuleSettings as LS

# front desk user login

#------------Local Veriables-------------------
labitem = GSV.UrineRE
imagingitem = GSV.USG
admitcharge = GSV.admitRate
deposit = 1000
########
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
#############
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
AC.logout()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode="Cash", department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
#can.verifyopdinvoice(deposit=0, billamt=500)

# LB.createlabxrayinvoice(HospitalNo=HospitalNo, labtest=labitem, imagingtest = imagingitem)
ADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, transfer=0, deposit=deposit, HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=isDoctorMandatory)
print("Patient admitted successfully")
ADT.admitDisTrans(danpheEMR=EMR, admit=0, discharge=0, transfer=1, deposit=deposit, HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=isDoctorMandatory)
print("Patient Transferred successfully")
ADT.admitDisTrans(danpheEMR=EMR, admit=0, discharge=1, transfer=0, deposit=deposit, HospitalNo=HospitalNo, department=GSV.doctorGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=isDoctorMandatory)
print("Patient Discharged successfully")
AC.logout()
AC.closeBrowser()
