Closing Balance Calculation Logic:

If Dispatch is Taken:
Closing Balance = Opening+Purchase +StockManageIn(Main+SubStore) -StockManageOut(Main+SubStore)-Dispatch

If Consumption  is Taken:
Closing Balance =  Opening+Purchase +StockManageIn(Main+SubStore) -StockManageOut(Main+SubStore)-Consumption


Note:
1. Cancelled GRs should be excluded altogether from this reports.
    We have separate report to show those data.

2. Return to Vendor Scenario is not handled yet, we'll revise the logic after that feature is completed.

from TestActionLibrary import A

cfy = A()
