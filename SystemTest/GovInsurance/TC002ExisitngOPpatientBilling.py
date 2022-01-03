import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAppointment as LA
import Library.LibModuleInsurance as LI
import Library.LibModuleBilling as LB
#AC.applicationSelection()
EMR = AC.openBrowser()


# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
radioTestUSG = GSV.USG

#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
# 1. Create an appointment for new patient.
HospitalNo = LA.patientquickentry(EMR, discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).HospitalNo
# 2. Create Insurance Patient for Existing patient
LI.ExistingPatientNewVisit(EMR, HospitalNo, departmentGynae, labtest=)

