#Tested Scenarios:
#  Same Day
# 1. Admitted Patient
# 2. Transfer Patient
# 3. Discharge Patient
# 4. Repeat above case for different day.
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.foUserPwD

doctorname = GSV.doctorGyno
opdCharge = GSV.opdRate
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
LBR.getDoctorSummary(danpheEMR=EMR, doctor=doctorname)
LBR.preSystemDoctorSummary()
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
LBR.getDoctorSummary(danpheEMR=EMR, doctor=doctorname)
LBR.verifyDoctorSummary(cash=opdCharge, cashreturn=0, credit=0, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo, returnmsg="this is bill return 1")
LBR.preSystemDoctorSummary()
LBR.getDoctorSummary(EMR, doctorname)
LBR.verifyDoctorSummary(cash=0, cashreturn=opdCharge, credit=0, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
HospitalNo, InvoiceNo1, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Credit', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
LBR.preSystemDoctorSummary()
LBR.getDoctorSummary(EMR, doctorname)
LBR.verifyDoctorSummary(cash=0, cashreturn=0, credit=opdCharge, creditreturn=0, discount=0, provisional=0, provisionalcancel=0)
LB.returnBillingInvoice(danpheEMR=EMR, InvoiceNo=InvoiceNo1, returnmsg="this is bill return 2")
LBR.preSystemDoctorSummary()
LBR.getDoctorSummary(EMR, doctorname)
LBR.verifyDoctorSummary(cash=0, cashreturn=0, credit=0, creditreturn=opdCharge, discount=0, provisional=0, provisionalcancel=0)
HospitalNo, InvoiceNo3, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=discountScheme, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
LBR.preSystemDoctorSummary()
LBR.getDoctorSummary(EMR, doctorname)
discount = discountScheme.partition("(")[2]
discount = discount.partition("%)")[0]
discount = int(discount)
print("Discount:", discount)
discountAmount = opdCharge*discount/100
LBR.verifyDoctorSummary(cash=opdCharge, cashreturn=0, credit=0, creditreturn=0, discount=discountAmount, provisional=0, provisionalcancel=0)
AC.logout()
AC.closeBrowser()





