import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

user = GSV.UserBilling
#
opdRate = GSV.opdRate
AC.applicationSelection()
AC.openBrowser()
AC.login(foUserId ,foUserPwd)
LB.counteractivation()
LBR.getUserCollectionReport()
LA.patientquickentry(0, 'Cash')
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(user)
LBR.verifyUserCollectionReport(cash=opdRate, cashreturn=0, credit=0, creditreturn=0, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
LBR.returnBillingInvoice("This is cash return.")
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(user)
LBR.verifyUserCollectionReport(cash=0, cashreturn=opdRate, credit=0, creditreturn=0, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
LB.patientquickentry(0, 'CREDIT')
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(user)
LBR.verifyUserCollectionReport(cash=0, cashreturn=0, credit=opdRate, creditreturn=0, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
LBR.returnBillingInvoice("This is credit return.")
LBR.preSystemUserCollectionReport()
LBR.getUserCollectionReport(user)
LBR.verifyUserCollectionReport(cash=0, cashreturn=0, credit=0, creditreturn=opdRate, discount=0, deposit=0,
                              depositreturn=0, creditsettlement=0, provisional=0, provisionalcancel=0)
AC.logout()
AC.closeBrowser()
