import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR

# front desk user login
foUserId = GSV.itUserID
foUserPwd = GSV.itUserPwD
opdRate = GSV.opdRate
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
LBR.getPatientCensus(EMR)
LBR.preSystemPatientCensus()
LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
LBR.getPatientCensus(EMR)
LBR.verifyPatientCensus(cash=opdRate, cashReturn=0, credit=0, creditReturn=0, provisional=0, provisionalCancel=0)
AC.logout()
AC.closeBrowser()
