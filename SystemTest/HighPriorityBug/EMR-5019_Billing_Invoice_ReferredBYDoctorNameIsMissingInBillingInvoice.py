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
referDoctor = GSV.ReferredBy
priceCategoryType = "Normal"
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
LB.verifyReferDoctorinInvoice(danpheEMR=EMR, HospitalNo=HospitalNo, imagingtest=labTestTFT, labtest=radioTestUSG, ReferDoctor=referDoctor)
AC.logout()
AC.closeBrowser()
# This testcase fails due to EMR-5019