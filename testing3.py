print ("e")
from ledger_entry import LedgerEntry

testA = LedgerEntry("AAA")

stringA = "A"

testA.add_purchase(stringA)

qwere= testA.display_entry()

print ("qwere is", qwere) 

testA.add_purchase("B")

ewretg = testA.display_entry()

print("ewretg is", ewretg)

for asdf in ewretg:
    print ("asdf is", asdf)



testA.add_purchase("G")
testA.add_purchase("U")
testA.add_purchase("Q")
print("added 3 ")

for asdf in ewretg:
    print ("asdf is", asdf)

print ("don test")

print("test 2")

from stock_purchase import StockPurchase

sto = StockPurchase("BBB", 567)

print("sto is" , sto.stock_symbol, sto.cost_per_share)

hjk = LedgerEntry("BBB")

hjk.add_purchase(sto)

qaz = hjk.display_entry()

print (qaz , " is qaz")
egw = StockPurchase("dsg", 3435)
hjk.add_purchase(egw)
hjk.add_purchase(StockPurchase("sdf", 35))
hjk.add_purchase(StockPurchase("rth", 5464))
hjk.add_purchase(StockPurchase("fhd", 437))
print (qaz , " is qaz")
for az in qaz:
    print (az.stock_symbol, az.cost_per_share)

print("test done")
