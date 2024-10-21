from ledger_entry import LedgerEntry
from stock_purchase import StockPurchase

#big stuff here 
class StockLedger():
    
    def __init__(self): 
        self.List_of_LedgerEntry_Objects = []
        
    def buy(self, stock_symbol, shares_bought, price_per_share): 
        NewLEntry = LedgerEntry(stock_symbol)
        NewStockPurchaseObject = StockPurchase(stock_symbol, price_per_share)
        NewLEntry.add_purchase(NewStockPurchaseObject)
        self.List_of_LedgerEntry_Objects.append(NewLEntry)
        
    def sell(self, stock_symbol, shares_sold, price_per_share): 
        
        index = -1
        for anEntry in self.List_of_LedgerEntry_Objects:
            index += 1
            if   anEntry.equals(stock_symbol):
                self.List_of_LedgerEntry_Objects[index].remove_purchase()
                return 
            

    def display_ledger(self): 
        
        for anEntry in self.List_of_LedgerEntry_Objects: 
            anEntry.display_entry()

        
    def contains(self, stock_symbol): 
        
        for anEntry in self.List_of_LedgerEntry_Objects:   
            if   anEntry.equals(stock_symbol):
                return True
            
        return False

    def get_entry(self, stock_symbol):
        index = -1

        for anEntry in self.List_of_LedgerEntry_Objects:
            index += 1
            if   anEntry.equals(stock_symbol):
                return anEntry
            
        return -1
    
