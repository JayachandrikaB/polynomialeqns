from function_operation import Function_LinkedList


def multiplication(equation1, equation2):
    ptr1 = equation1.head
    # using inbuilt dictionary to save the power and coeff for internal purpose
    # the job of dictionary is to store the power and coeff for each node in form of key-value pair
    # this will ensure one entry for each node   
    node_content = dict()
    while ptr1 : 
        # Unlike Addition here approach will be different 
        # Two nodes of both equation will always be combined and some operation will be performed
        ptr2 = equation2.head
        while ptr2 : 
            # Adding the powers of two nodes as per the rule
            power = ptr1.power + ptr2.power
            if power not in node_content : 
                node_content[power] = 0
            # creating key-value pair for each node based on power and coeff
            # If there are more terms with the same power their coeff will be added. 
            node_content[power] += ptr1.coeff * ptr2.coeff
            # traversing the ptr1
            ptr2 = ptr2.next
        # traversing the ptr2
        ptr1 = ptr1.next
    # creating new linked list to store result
    equation3 = Function_LinkedList()

    # inserting elements in the newly created equation
    # passing power and coeff as parameter to insert the element
    for power, coeff in node_content.items() : 
        equation3.insert_data(power, coeff)
    # Printing teh content of the newly created linked list with the help of display method
    print('\nMultiplication_equation:', end = ' ')
    # Calling display method of function_operation class
    equation3.display()
    return equation3
    

def addition(equation1, equation2):
    ptr1, ptr2 = equation1.head, equation2.head
    # Need a linked list to store the output data after the operation
    equation3 = Function_LinkedList()
    # Following loop will be executed till the ptr1 or ptr2 will become None 
    while ptr1 or ptr2 :
        # There are multiple cases possible while adding the two equations
        # I. Both powers are same
        # II. ptr1 power is greater than ptr2
        # III. ptr2 power is greater than ptr1
        if ptr1 and ptr2 :
            # I. Powers are same, addition can happen and new node will be inserted in the created equation
            if ptr1.power == ptr2.power : 
                equation3.insert_data(ptr1.power, ptr1.coeff + ptr2.coeff)
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            # II. Power do not match and ptr1 is greater than ptr2
            elif ptr1.power > ptr2.power : 
                equation3.insert_data(ptr1.power, ptr1.coeff)
                ptr1 = ptr1.next

            # III. Power do not match and pyr2 is gtreater than ptr1
            else : 
                equation3.insert_data(ptr2.power, ptr2.coeff)
                ptr2 = ptr2.next
        # if there are unvisited nodes in ptr1 or ptr2, will traverse and insert the node in new equation
        else : 
            if not ptr1 : 
                equation3.insert_data(ptr2.power, ptr2.coeff)
                ptr2 = ptr2.next
            else : 
                equation3.insert_data(ptr1.power, ptr1.coeff)
                ptr1 = ptr1.next
    
    # Printing teh content of the newly created linked list with the help of display method
    print('\nAddition_equation:', end = ' ')
    # Calling display method of function_operation class
    equation3.display()
    return equation3

def sorting_function(equation) :
    # using the sorting method that is actually implemented in the function_operation class. 
    equation.sorting_equation()
    # Printing teh content of the newly created linked list with the help of display method
    print('Sorted_equation:', end = ' ')
    # Calling display method of function_operation class
    equation.display()
    return equation
