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
        NewStockPurchaseObject = StockPurchase(stock_symbol, price_per_share) #creating the stock_purchase
        if not self.contains(stock_symbol):
            NewLEntry = LedgerEntry(stock_symbol) #creating the ledger entry 
            
            # NewLEntry.add_purchase(NewStockPurchaseObject) #putting the stock_purchase into the ledger_entry
            
            counter = 1
            while counter <= shares_bought:
                NewLEntry.add_purchase(NewStockPurchaseObject) #putting the stock_purchase into the ledger_entry
                counter += 1
            # this is where add the loop for muliple shares bought 

            self.List_of_LedgerEntry_Objects.append(NewLEntry) #putting the ledger entry into our stock ledger list
            #TODO add a line to check if an existing of the same stock symbol exist to place it there 
            # make use of the shares bought keyword 
            #print("bought")
        elif self.contains(stock_symbol):
            existingEntry = self.get_entry(stock_symbol)

            counter = 1
            while counter <= shares_bought:
                existingEntry.add_purchase(NewStockPurchaseObject) #putting the stock_purchase into the ledger_entry
                counter += 1

            
        
    def sell(self, stock_symbol, shares_sold, price_per_share): 
        
        index = -1
        for anEntry in self.List_of_LedgerEntry_Objects:
            index += 1
            if   anEntry.equals(stock_symbol):

                # loop this share sold times
                while shares_sold > 0: 
                    self.List_of_LedgerEntry_Objects[index].remove_purchase()
                    shares_sold -= 1

                if self.List_of_LedgerEntry_Objects[index] == None:
                    self.List_of_LedgerEntry_Objects.pop(index)
                return 
        #TODO add checking for the other fields 
            
    # this is what the output needs to be: 
    #             
    # ---- Stock Ledger ----
    # AAPL: 45.0 (20 shares), 75.0 (20 shares) 
    # MSFT: 95.0 (20 shares) 
    def display_ledger(self): 
        my_string = ""

        for anEntry in self.List_of_LedgerEntry_Objects: 
            my_string = my_string + anEntry.stock_symbol + " "

            #shares_counter = 0
            value_counter_list = []
            stock_counter_list = []

            for a_stock_purchase in anEntry.display_entry():

                if len(value_counter_list) == 0:
                    value_counter_list.append(a_stock_purchase.cost_per_share)
                    stock_counter_list.append(1)
                elif a_stock_purchase.cost_per_share == value_counter_list[-1]:
                    stock_counter_list[-1] += 1
                elif a_stock_purchase.cost_per_share != value_counter_list[-1]:
                    value_counter_list.append(a_stock_purchase.cost_per_share)
                    stock_counter_list.append(1)

                # this block of code turns a list of like [22, 22, 22, 12, 12]
                # into these two paralell lists of [22, 12] and [3, 2]

            ## in future use the better string builder
            index = 0
            for a_count_of_stocks in stock_counter_list: 
                my_string = my_string + str(value_counter_list[index]) + " (" + str(a_count_of_stocks) + " shares), "
                index += 1

        return my_string
                


        


    def display_ledger_lists_of_lists(self): 
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
    
