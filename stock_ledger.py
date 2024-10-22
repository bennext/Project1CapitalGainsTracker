from ledger_entry import LedgerEntry
from stock_purchase import StockPurchase

#big stuff here 

# also test this 

# All stocks of the same type will go into the same Linked Deque. 
# The list will be implemented in StockLedger. 
# You will need to write methods to display your ledger and use an iterator to traverse the Deque. 


class StockLedger():
    
    def __init__(self): 
        self.List_of_LedgerEntry_Objects = []
        
    def buy(self, stock_symbol, shares_bought, price_per_share): 
        #print("buying")
        NewLEntry = LedgerEntry(stock_symbol) #creating the ledger entry 
        NewStockPurchaseObject = StockPurchase(stock_symbol, price_per_share) #creating the stock_purchase
        NewLEntry.add_purchase(NewStockPurchaseObject) #putting the stock_purchase into the ledger_entry
        self.List_of_LedgerEntry_Objects.append(NewLEntry) #putting the ledger entry into our stock ledger list
        #TODO add a line to check if an existing of the same stock symbol exist to place it there 
        #TODO make use of the shares bought keyword 
        #print("bought")
        
    def sell(self, stock_symbol, shares_sold, price_per_share): 
        
        index = -1
        for anEntry in self.List_of_LedgerEntry_Objects:
            index += 1
            if   anEntry.equals(stock_symbol):
                self.List_of_LedgerEntry_Objects[index].remove_purchase()
                self.List_of_LedgerEntry_Objects.pop(index)
                return 
        #TODO add checking for the other fields 
            

    def display_ledger(self): 
        lists_of_lists = []
        for anEntry in self.List_of_LedgerEntry_Objects: 
            lists_of_lists.append(anEntry.display_entry())
        # add a return 
        return lists_of_lists


        
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
    
