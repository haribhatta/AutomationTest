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
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
LB.verifyReferDoctorinInvoice(danpheEMR=EMR, imagingtest=labTestTFT, labtest=radioTestUSG, ReferDoctor=referDoctor)
AC.logout()
AC.closeBrowser()
# This testcase fails due to EMR-5019