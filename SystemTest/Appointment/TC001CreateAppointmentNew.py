from TestActionLibrary import A

can = A()

can.openBrowser()
can.login("billing1", "pass123")
can.counteractivation()
can.patientquickentry(discountpc=0, paymentmode='Cash')
can.verifyopdinvoice(deposit=0, billamt=500)
can.logout()
can.closeBrowser()
print("Status:Passed - > TC001 CreateAppointmentNew")
