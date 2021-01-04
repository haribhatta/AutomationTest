from TestActionLibrary import A

pvs = A()

pvs.openBrowser()
pvs.login("admin", "pass123")
pvs.getIncentivePatientVsServiceReport()
pvs.preIncentivePatientVsServiceReport()
pvs.counteractivation()
pvs.patientquickentry(discountpc=0, paymentmode='Cash')
pvs.synchBilingIncentive()
pvs.getIncentivePatientVsServiceReport()
pvs.verifyIncentivePatientVsServiceReport(amount=500)
