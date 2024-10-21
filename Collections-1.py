class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
    
    def __repr__(self):
        return self.data.__repr__()
    

class LinkedList:
    def __init__(self):
        self.head_node = None
        self.num_nodes = 0

    def __iter__(self):
        temp_node = self.head_node
        while temp_node is not None:
            yield temp_node.data
            temp_node = temp_node.next_node
    
    def insert_at_start(self, data):
        new_node = Node(data)
        self.num_nodes += 1
        if self.head_node is None:
            self.head_node = new_node
        else:
            new_node.next_node = self.head_node
            self.head_node = new_node

    def append(self, data):
        new_node = Node(data)
        self.num_nodes += 1
        if self.head_node is None:
            self.head_node = new_node
        else:
            temp_node = self.head_node
            while temp_node.next_node is not None:
                temp_node = temp_node.next_node
            temp_node.next_node = new_node

    def insert_after(self, new_data, data):
        new_node = Node(new_data)
        self.num_nodes += 1
        if self.head_node is None:
            self.head_node = new_node
        else:
            temp_node = self.head_node
            while temp_node.next_node is not None and temp_node.data != data:
                temp_node = temp_node.next_node
            new_node.next_node = temp_node.next_node
            temp_node.next_node = new_node

    def remove(self, data):
        if self.head_node is None:
            return
        if self.head_node.data == data:
            del_head = self.head_node
            self.head_node = self.head_node.next_node
            del del_head
        else:
            temp_node = self.head_node
            previous_node = self.head_node
            while temp_node.next_node is not None and temp_node.data != data:
                previous_node = temp_node
                temp_node = temp_node.next_node
            previous_node.next_node = temp_node.next_node
            del temp_node.next_node
            self.num_nodes -= 1

    def __repr__(self):
        temp_node = self.head_node
        output = ""
        while temp_node is not None:
            output += temp_node.__repr__()
            output += "\n"
            temp_node = temp_node.next_node
        return output

class Stack:
    def __init__(self):
        self.top_node = None
        self.num_nodes = 0

    def __iter__(self):
        temp_node = self.top_node
        while temp_node is not None:
            yield temp_node.data
            temp_node = temp_node.next_node

    def push(self, data):
        new_node = Node(data)
        self.num_nodes += 1
        if self.top_node is None:
            self.top_node = new_node
        else:
            new_node.next_node = self.top_node
            self.top_node = new_node

    def pop(self):
        if self.top_node is None:
            return
        else:
            removed = self.top_node
            self.top_node = self.top_node.next_node
            self.num_nodes -= 1
            return removed.data

    def __repr__(self):
        temp_node = self.top_node
        output = ""
        while temp_node is not None:
            output += temp_node.__repr__()
            output += "\n"
            temp_node = temp_node.next_node
        return output

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.num_nodes = 0

    def __iter__(self):
        temp_node = self.front_node
        while temp_node is not None:
            yield temp_node.data
            temp_node = temp_node.next_node

    def push(self, data):
        new_node = Node(data)
        self.num_nodes += 1
        if self.front_node is None:
            self.front_node = new_node
            self.rear_node = new_node
        else:
            self.rear_node.next_node = new_node
            self.rear_node = new_node


    def pop(self):
        if self.front_node is None:
            return
        else:
            removed = self.front_node
            self.front_node = self.front_node.next_node
            self.num_nodes -= 1
            return removed.data

    def __repr__(self):
        temp_node = self.front_node
        output = ""
        while temp_node is not None:
            output += temp_node.__repr__()
            output += "\n"
            temp_node = temp_node.next_node
        return output

class BSTNode:
    def __init__(self, data, parent = None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent

    def __repr__(self):
        return self.data.__repr__()
    

class BinarySearchTree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        #create a new node with the data entered
        new_node = BSTNode(data)
        #if there's nothing in the tree, insert the node at the root
        if self.root_node is None:
            self.root_node = new_node
        #otherwise, call a recursive method on the root node
        else:
            self.insert_node(data, self.root_node)

    def insert_node(self, data, node):
        #if the inserted node's name is less than the one it's comparing to (starts with root node)
        if data.name < node.data.name:
            #call this method on each node until it is in the right place
            if node.left_node is not None:
                self.insert_node(data,node.left_node)
            else:
                #when you get to the right place, create a new node there
                node.left_node = BSTNode(data, node)
        #if it's to the right of the one it's comparing to
        else:
            #call this method on each node until it is in the right place
            if node.right_node is not None:
                self.insert_node(data,node.right_node)
            else:
                #when you get to the right place, create a new node there
                node.right_node = BSTNode(data, node)

    def print_tree(self):
        # if the tree is not empty
        if self.root_node is not None:
            #call the recursive method print_in_order on the root node
            self.print_in_order(self.root_node)

    def print_in_order(self, node):
        #call this method on each node going left until the left node is none
        if node.left_node is not None:
            self.print_in_order(node.left_node)
        #print the node
        print(node)
        #call this method on each node going right until the right node is none
        if node.right_node is not None:
            self.print_in_order(node.right_node)

    #an alternative print tree method that prints the names of birds
    def print_name(self):
        if self.root_node is not None:
            self.print_names_in_order(self.root_node)

    def print_names_in_order(self, node):
        if node.left_node is not None:
            self.print_names_in_order(node.left_node)
        print(node.data.name)
        if node.right_node is not None:
            self.print_names_in_order(node.right_node)


    def get_min(self):
        temp_node = self.root_node
        while temp_node.left_node is not None:
            temp_node = temp_node.left_node
        return temp_node.data

    def get_max(self):
        temp_node = self.root_node
        while temp_node.right_node is not None:
            temp_node = temp_node.right_node
        return temp_node.data

    def get(self, title):
        if self.root_node is None:
            return None
        else:
            return self.get_book(title, self.root_node)

    def get_book(self, title, node):
        if title == node.data.title:
            return node
        elif title < node.data.title:
            if node.left_node is not None:
                return self.get_book(title,node.left_node)
            else:
                return None
        else:
            if node.right_node is not None:
                return self.get_book(title,node.right_node)
            else:
                return None

    def get_bird(self, name):
        if self.root_node is None:
            return None
        else:
            return self.get_bird_from_name(name, self.root_node)

    def get_bird_from_name(self, name, node):
        if name == node.data.name:
            return node
        elif name < node.data.name:
            if node.left_node is not None:
                return self.get_bird_from_name(name,node.left_node)
            else:
                return None
        else:
            if node.right_node is not None:
                return self.get_bird_from_name(name,node.right_node)
            else:
                return None


    def get_num_pred(self, node):
        temp_node = node.left_node
        while temp_node.right_node is not None:
            temp_node = temp_node.right_node
        return temp_node

    def remove(self, data):
        if self.root_node is not None:
            return self.remove_node(data, self.root_node)
    
    def remove_node(self, title, node):
        if node is None:
            return
        #find the node that we want to remove
        if self.get(title).data.title < node.data.title:
            return self.remove_node(self.get(title).data.title, node.left_node)
        elif self.get(title).data.title > node.data.title:
            return self.remove_node(self.get(title).data.title, node.right_node)
        else:
            #OPTION 1: IT IS A LEAF NODE
            if node.right_node is None and node.left_node is None:
                parent = node.parent
                #is it a left child
                if parent is not None and parent.left_node == node:
                    #set its parents left node to None (removing it from the tree)
                    parent.left_node = None
                #is it a right child
                elif parent is not None and parent.right_node == node:
                    #set its parents right node to None (removing it from the tree)
                    parent.right_node = None
                else:
                    self.root_node = None
                return node.data
            #OPTION 2: IT HAS A SINGLE CHILD
            #if it has a right child
            elif node.left_node is None and node.right_node is not None:
                parent = node.parent
                #is NODE a left child
                if parent is not None and parent.left_node == node:
                    #move the child up to where node used to be
                    parent.left_node = node.right_node
                #is NODE a right child
                elif parent is not None and parent.right_node == node:
                    #move the child up to where node used to be
                    parent.right_node = node.right_node
                #if NODE is the root node
                elif parent is None:
                    #set the root node to NODE's right node
                    self.root_node = node.right_node
                return node.data
            #if it has a left child
            elif node.left_node is not None and node.right_node is None:
                parent = node.parent
                #is NODE a left child
                if parent is not None and parent.left_node == node:
                    #move the child up to where node used to be
                    parent.left_node = node.left_node
                #is NODE a right child
                elif parent is not None and parent.right_node == node:
                    #move the child up to where node used to be
                    parent.right_node = node.left_node
                elif parent is None:
                    #set the root node to NODE's left node
                    self.root_node = node.left_node
                return node.data
            #OPTION 3: IT HAS TWO CHILDREN
            else:
                predecessor = self.get_num_pred(node)
                #swap the data of predecessor and NODE
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                #remove it as if it is a leaf node
                self.remove_node(self.get(title).data.title, predecessor)

if __name__ == '__main__':
    my_list = LinkedList()
    my_list.append(6)
    my_list.insert_at_start("hiii")
    my_list.insert_after(80,"hiii")
    my_list.remove(80)
    # print(my_list)
    my_tree = BinarySearchTree()
    # my_tree.insert(Book("Mary Shelley","Frankenstein"))
    # my_tree.insert(Book("Bram Stoker", "Dracula"))
    # my_tree.insert(Book("Anne Bronte", "Agnes Grey"))
    # my_tree.insert(Book("George ELiot", "Middlemarch"))
    
    # my_tree.print_tree()
    # # print(my_tree.get_min())
    # # print(my_tree.get_max())
    # print(my_tree.get_book("Frankenstein"))

    test_tree = BinarySearchTree()
    test_tree.insert(53)
    test_tree.insert(42)
    test_tree.insert(61)
    test_tree.insert(40)
    test_tree.insert(55)
    test_tree.insert(68)
    test_tree.print_tree()
    print()
    # print(test_tree.get(42))
    test_tree.remove(61)
    test_tree.print_tree()
    