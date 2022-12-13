from Library import ApplicationConfiguration as AC
from Library import LibModuleBilling as LB
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
doctor2 = GSV.doctor2
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
#############

#------------Local Veriables-------------------
labitem = GSV.UrineRE
imagingitem = GSV.USG
deposit = 2000
admitCharge = GSV.admitRate
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
LB.counteractivation(EMR)
isDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
LS.checkAutoAddItems(danpheEMR=EMR)
LS.paymentModeOpBillingDisplaySequence(EMR)
LS.addLongSignatureOfEmployee(danpheEMR=EMR, doctor=doctor, doctor2=doctor2)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode="Cash", department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
LB.createlabxrayinvoice(danpheEMR=EMR, HospitalNo=HospitalNo, labtest=labitem, imagingtest=imagingitem)
ADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, transfer=0, deposit=deposit, HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=isDoctorMandatory)
print("Patient admitted successfully")
ADT.admitDisTrans(danpheEMR=EMR, admit=0, discharge=1, transfer=0, deposit=deposit, HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=isDoctorMandatory)
print("Patient Discharged successfully")
ADT.AddSummaryOfDischargedPatient(EMR, HospitalNo=HospitalNo, consultantDr=doctor, inchargeDr=doctor2)
ADT.updateAndViewSummaryOfDischargedPatient(danpheEMR=EMR, HospitalNo=HospitalNo)
ADT.verifyInchargeDoctorAfterUpdate(danpheEMR=EMR, HospitalNo=HospitalNo)
AC.logout()
AC.closeBrowser()