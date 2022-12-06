import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA

EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
labTestTFT = GSV.TFT
radioTestUSG = GSV.USG
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=GSV.discountSchemeName, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType="Normal", case="+ve")
print("hospitalNo", HospitalNo)
InvoiceNo1 = LB.multiplebillingclick(danpheEMR=EMR, HospitalNo=HospitalNo, labtest=labTestTFT, imagingtest=radioTestUSG, discountScheme=GSV.discountSchemeName)
AC.logout()
AC.closeBrowser()