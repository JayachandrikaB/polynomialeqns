class Node:
    def __init__(self, power = 0, coeff = 0):    
        self.power = power
        self.coeff = coeff
        self.next = None

class Function_LinkedList: 


    def __init__(self):
        self.head = None
        self.power = 0
        self.coeff = 1    

    def insert_data(self, power, coeff):
        # Assigning variable for new node creation
        self.power = power
        self.coeff = coeff
        new_node = Node(self.power, self.coeff)
        # Inserting node at the temporary variable
        if self.head == None:
            self.head = new_node

        # Inserting node at the beginning of teh linked list
        else:
            tmp = self.head
            while(tmp.next):
                tmp = tmp.next
            tmp.next = new_node

        return self.head

        
    def display(self):
        # print the content of the list
        # Initializing the temp variable for traversal
        temp = self.head
        # checking the condition if there are some elements are there in the linked list
        if self.head is not None:
            # running the loop till temp is traversed once completely
            # To print the equation without any confusion, we are iterating till the second last node of the list
            while(temp.next):
                # printing the data
                if temp.coeff == 0:
                    pass
                elif temp.power != 0:
                    if temp.coeff == 1: 
                        print("x", "^", temp.power, end = " + ")
                    else: 
                        print(temp.coeff, "*", "x", "^", temp.power, end = " + ")
                else:
                    if temp.coeff == 1: 
                        print(1, end = " + ")
                    else: 
                        print(temp.coeff, "*", "x", "^", temp.power, end = " + ")

                temp = temp.next
            if(temp.power != 0):
                if temp.coeff == 1:
                    print("x", "^", temp.power)
                else:
                    print(temp.coeff, "*", "x", "^", temp.power)
            else:
                print(temp.coeff)

    def sorting_equation(self) :
        # Using sorting techinqiue with the help of fast and slow pointer technique to sort based on the 
        # power of the each node, Traversal will happen for all the nodes 
        fast_pointer = self.head
        while fast_pointer : 
            slow_pointer = fast_pointer.next
            # Here we are running the loop from fast_poitnter.next to the end 
            while slow_pointer : 
                # Comparing the pwoer of two nodes and switching their values 
                # coeff and power, both will be swapped for the nodes if the following condition is true
                if fast_pointer.power < slow_pointer.power : 
                    temp_power = fast_pointer.power
                    fast_pointer.power= slow_pointer.power
                    slow_pointer.power = temp_power 
                    temp_coeff = fast_pointer.coeff  
                    fast_pointer.coeff = slow_pointer.coeff
                    slow_pointer.coeff = temp_coeff
                slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next 