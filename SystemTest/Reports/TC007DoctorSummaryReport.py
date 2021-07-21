#Tested Scenarios:
#  Same Day
# 1. Admitted Patient
# 2. Transfer Patient
# 3. Discharge Patient
# 4. Repeat above case for different day.
from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

doctorname = GSV.doctor1
opdCharge = GSV.opdRate

pcsr = A()

pcsr.openBrowser()
pcsr.login(foUserId, foUserPwd)
pcsr.counteractivation()
pcsr.getDoctorSummary(doctorname)
pcsr.preSystemDoctorSummary()
pcsr.patientquickentry(0, "Cash")
pcsr.getDoctorSummary(doctorname)
pcsr.verifyDoctorSummary(cash=opdCharge, cashreturn=0, credit=0, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
pcsr.returnBillingInvoice(returnmsg="this is bill return 1")
pcsr.preSystemDoctorSummary()
pcsr.getDoctorSummary(doctorname)
pcsr.verifyDoctorSummary(cash=0, cashreturn=opdCharge, credit=0, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
pcsr.patientquickentry(0, "CREDIT")
pcsr.preSystemDoctorSummary()
pcsr.getDoctorSummary(doctorname)
pcsr.verifyDoctorSummary(cash=0, cashreturn=0, credit=opdCharge, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
pcsr.returnBillingInvoice(returnmsg="this is bill return 2")
pcsr.preSystemDoctorSummary()
pcsr.getDoctorSummary(doctorname)
pcsr.verifyDoctorSummary(cash=0, cashreturn=0, credit=0, creditreturn=opdCharge, discount=0, provisional=0, provisionalcancel=0)
pcsr.patientquickentry(50, 'Cash')
pcsr.preSystemDoctorSummary()
pcsr.getDoctorSummary(doctorname)
pcsr.verifyDoctorSummary(cash=opdCharge, cashreturn=0, credit=0, creditreturn=0, discount=250, provisional=0, provisionalcancel=0)
pcsr.logout()
pcsr.closeBrowser()





