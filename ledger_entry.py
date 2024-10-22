from linked_deque import LinkedDeque

class LedgerEntry():
    
    def __init__(self, stock_symbol): 
        self.stock_symbol = stock_symbol
        self.LDofStocks = LinkedDeque()
        #List_of_LedgerEntry_Objects = []
        #pass

    def add_purchase(self, new_purchase): 
        #self.List_of_LedgerEntry_Objects.append(new_purchase)
        self.LDofStocks.add_to_front(new_purchase)
        #pass

    def remove_purchase(self): 
        self.LDofStocks.remove_front()
        #self.List_of_LedgerEntry_Objects.pop()
        #pass

    def equals(self, other): 
        return self.stock_symbol == other
        pass

    def display_entry(self):
        temp = self.LDofStocks.display()
        return temp #list of the linkeddeque data objects
    
    def is_empty(self):
        return self.LDofStocks.get_front() == None 
    
        
