import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
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
LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
LBR.getPatientCensus(EMR)
LBR.verifyPatientCensus(cash=opdRate, cashreturn=0, credit=0, creditreturn=0, provisional=0)
AC.logout()
AC.closeBrowser()
