#Tested Scenarios:
#  Same Day
# 1. Admitted Patient
# 2. Transfer Patient
# 3. Discharge Patient
# 4. Repeat above case for different day.
from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

doctorname = "Dr. Doctor Doctor"

pcsr = A()

pcsr.openBrowser()
pcsr.login(foUserId, foUserPwd)
pcsr.counteractivation()
pcsr.getDoctorSummary(doctorname)
pcsr.preSystemDoctorSummary()
pcsr.patientquickentry(0, "Cash")
pcsr.getDoctorSummary(doctorname)
pcsr.verifyDoctorSummary(cash=500, cashreturn=0, credit=0, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
pcsr.returnBillingInvoice(returnmsg="this is bill return 1")
pcsr.preSystemDoctorSummary()
pcsr.getDoctorSummary(doctorname)
pcsr.verifyDoctorSummary(cash=0, cashreturn=500, credit=0, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
pcsr.patientquickentry(0, "CREDIT")
pcsr.preSystemDoctorSummary()
pcsr.getDoctorSummary(doctorname)
pcsr.verifyDoctorSummary(cash=0, cashreturn=0, credit=500, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
pcsr.returnBillingInvoice(returnmsg="this is bill return 2")
pcsr.preSystemDoctorSummary()
pcsr.getDoctorSummary(doctorname)
pcsr.verifyDoctorSummary(cash=0, cashreturn=0, credit=0, creditreturn=500, discount=0, provisional=0, provisionalcancel=0)
pcsr.patientquickentry(50, 'Cash')
pcsr.preSystemDoctorSummary()
pcsr.getDoctorSummary(doctorname)
pcsr.verifyDoctorSummary(cash=500, cashreturn=0, credit=0, creditreturn=0, discount=250, provisional=0, provisionalcancel=0)
pcsr.logout()
pcsr.closeBrowser()





