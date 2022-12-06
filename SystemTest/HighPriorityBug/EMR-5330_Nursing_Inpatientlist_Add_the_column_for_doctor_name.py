# This script is to add Triage of Outpatient and adding note in Overview
import Library.GlobalShareVariables as GSV
import Library.LibModuleAppointment as LA
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleNursing as LN
from Library import LibModuleADT as ADT
from Library import LibModuleSettings as LS
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
wardName = GSV.admitWard
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
paymode = "Credit"
deposit = 1000
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode=paymode, department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType="Normal", case="+ve")
priceCategoryType = "Normal"
admittingDoctorMandatory = LS.checkCoreCFGadmitDocMandatory(danpheEMR=EMR)
ADT.admitDisTrans(danpheEMR=EMR, admit=1, discharge=0, transfer=0, deposit=deposit, HospitalNo=HospitalNo, department=GSV.departmentGyno, doctor=GSV.doctorGyno, admittingDoctorMandatory=admittingDoctorMandatory)
discountScheme = GSV.discountSchemeName
LN.inPatientOverview(danpheEMR=EMR, wardName=wardName, hospitalNumber=HospitalNo)
AC.closeBrowser()
