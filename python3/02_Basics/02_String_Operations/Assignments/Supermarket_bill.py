#!python -u
# printing store receipt
print(" ".center(60))
print("=" * 60)
print(("-" * 12).center(60))
print("SUPER MARKET".center(60))
print(("-" * 12).center(60))
print("1000 Castro Street, #111,".center(60))
print("MTV, CA, 94000".center(60))
print(" ".center(60))
print("Name of the customer:Ram")
print(" ".center(60))
print(("-" * 60).center(60))
print("S.No    Name of Item      Unit Price     Qty    Total Price")
print(
    "%d       %s              %d            %d      $%f/-" % (1, "Apple", 10, 12, 120)
)
print(
    "%d       %s              %d            %d      $%f/-" % (2, "Mangoes", 3, 10, 30)
)
print(" ".center(60))
print(" ".center(60))
print(("-" * 60).center(60))
print(" ".center(60))
print(("Total cost before discount: Rs %d/-" % (150)).rjust(57))
print(("(PAY)After discount: Rs %d/-" % (80)).rjust(57))
print(("YOU SAVED: Rs %d/-" % (30)).rjust(57))
print(" ".center(60))
print(" ".center(60))
print(("-" * 60).center(60))
print("Name of the cashier:Alex")
print("Date: 10/28/2017 10:14:43")
print(" ".center(60))
print(" ".center(60))
print("Thanks for visiting!!!".center(60))
print(" ".center(60))
print(" ".center(60))
print(("=" * 60).center(60))

"""
============================================================
                        ------------
                        SUPER MARKET
                        ------------
                 1000 Castro Street, #111,
                       MTV, CA, 94000

Name of the customer:Ram

------------------------------------------------------------
S.No    Name of Item      Unit Price     Qty    Total Price
1       Apple              10            12      $120.000000/-
2       Mangoes              3            10      $30.000000/-


------------------------------------------------------------

                     Total cost before discount: Rs 150/-
                             (PAY)After discount: Rs 80/-
                                       YOU SAVED: Rs 30/-


------------------------------------------------------------
Name of the cashier:Alex
Date: 10/28/2017 10:14:43


                   Thanks for visiting!!!


============================================================
"""
