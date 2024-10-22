class LinkedDeque():

    class DLNode ():
        
        def __init__(self, previous_node=None, data_portion=None, next_node=None):
            self.previous = previous_node
            self.data = data_portion
            self.next = next_node
            
        def get_data(self):
            return self.data
            
        def set_data(self, new_data):
            self.data = new_data
            
        def get_next_node(self):
            return self.next
            
        def set_next_node(self, next_node):
            self.next = next_node

        def get_previous_node(self):
            return self.previous

        def set_previous_node(self, previous_node):
            self.previous = previous_node
            
    ################     
    
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_back(self, new_entry):
        new_node = self.DLNode()
        new_node.set_data(new_entry)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node) #next = new_node
            new_node.set_previous_node(self.tail) #new_node.prev = self.tail
            self.tail = new_node

    def add_to_front(self, new_entry):
        new_node = self.DLNode()
        new_node.set_data(new_entry)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)  #next = self.head
            self.head.set_previous_node(new_node)  #prev = new_node
            self.head = new_node
        
    def get_back(self):
        return self.tail
        
    def get_front(self):
        return self.head
        
    def remove_front(self):
        self.head = self.head.get_next_node()
        
    def remove_back(self):
        self.tail = self.tail.get_previous_node()
        
    def clear(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return self.head == None

    def display(self):
        # Not quite sure what asking for here 
        #print(self)
        alist = []
        #holdHead = self.head
        if self.head != None:
            it = self.head
        else:
            print("empty")
            return ["empty"]
        
        while it != None:
            #print (it.data)
            alist.append(it.data)
            it = it.get_next_node()
        #self.head = holdHead
        return alist
