# This script is to add Triage of Outpatient and adding note in Overview
import Library.GlobalShareVariables as GSV
import Library.LibModuleAppointment as LA
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleNursing as LN

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
paymode = "Credit"
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode=paymode, department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType="Normal", case="+ve")
LN.addTriage(danpheEMR=EMR, hospitalNumber=HospitalNo, Height=120, Weight=80, Temperature=212, Pulse=83, BPSystolic=120,
             BPDiastolic=80, RespirotaryRate=93, SPO2=80, BodyPart="Head")
LN.outPatientOverview(danpheEMR=EMR, hospitalNumber=HospitalNo, IsTriageDone="yes")
LN.addNotes(danpheEMR=EMR, Template="Emergency Note")
AC.logout()
AC.closeBrowser()
