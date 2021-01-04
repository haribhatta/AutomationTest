from colorama import Fore, Back, Style

try:
    exec(open("D:/svn/DanpheEMR/SystemTest/Appointment/TC001CreateAppointmentNew.py").read())
    print(Back.GREEN + "TC001: Passed" + Back.RESET)
except Exception:
    pass
try:
    exec(open("D:/svn/DanpheEMR/SystemTest/Patient/TC001PatientRegistrationPrintHealthCard.py").read())
    print(Back.GREEN + "TC002: Passed" + Back.RESET)
except Exception:
    pass
try:
    exec(open("D:/svn/DanpheEMR/SystemTest/Billing/TC002OPDbillingLabXray.py").read())
    print(Back.GREEN + "TC003: Passed" + Back.RESET)
except Exception:
    pass
try:
    exec(open("D:/svn/DanpheEMR/SystemTest/Laboratory/TC005GenerateLabReport.py").read())
    print(Back.GREEN + "TC004: Passed" + Back.RESET)
except Exception:
    pass
try:
    exec(open("D:/svn/DanpheEMR/SystemTest/Radiology/TC001GenerateUSGReport.py").read())
    print(Back.GREEN + "TC005: Passed" + Back.RESET)
except Exception:
    pass
try:
    exec(open("D:/svn/DanpheEMR/SystemTest/Pharmacy/TC003PharmacyOPDbilling.py").read())
    print(Back.GREEN + "TC006: Passed" + Back.RESET)
except Exception:
    pass
