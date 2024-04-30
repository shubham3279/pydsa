class Node:
    def __init__(self, value):
        self.nodedata = value
        self.nextnode = None


class LinkedList:
    def __init__(self):
        # creates empty linked list : head = None
        self.headnode = None  # linked list's head node
        self.nodecount = 0  # node count

    # length of linked list = number of nodes in linked list
    def __len__(self):
        return self.nodecount

    # Insertion a new item in Linked List from Head
    def insert_head(self, nodedata):
        new_node = Node(nodedata)  # creating a new node
        new_node.nextnode = self.headnode  # create reference
        # reassigning Head
        self.headnode = new_node
        # incrementing node count
        self.nodecount += 1

    # Inserting a new item in Linked List from Tail : Append
    def append(self, value):
        # traverse to the Tail
        new_node = Node(value)
        if self.headnode == None:  # empty linked list
            self.headnode = new_node
            self.nodecount += 1
            return
        current_node = self.headnode
        while current_node.nextnode != None:
            current_node = current_node.nextnode
            self.nodecount += 1
        # we are at last node now
        # set the pointer of tail to new node
        current_node.nextnode = new_node

    # Inserting a new node in Linked List in between after some value
    def insert_after(self, nodedata, value):
        new_node = Node(value)
        # traverse to after_value as current node
        current_node = self.headnode
        while current_node != None:
            if current_node.nodedata == nodedata:
                break
            current_node = current_node.nextnode
        # case1: break happens : prevnode  found
        # case2: break doesn't happens : loop runs upto last node : nodedata not found
        if current_node != None:
            new_node.nextnode = current_node.nextnode
            current_node.nextnode = new_node
            self.nodecount += 1
        else:
            return f'{nodedata} not found in the linked list.'

    # Clearing the linked List
    def empty(self):
        self.headnode = None
        self.nodecount = 0

    # Deleting nodes from headnode
    def rmvhead(self):
        # logic for empty linked list
        if self.headnode == None:
            return f'Empty Linked List'
        # logic for removing head node
        return f' Removed headnode: {self.headnode}'
        self.headnode = self.headnode.nextnode
        self.nodecount -= 1

    # Deleting nodes from tail (Pop)
    def rmvtail(self):
        # logic for empty linked list
        if self.headnode == None:
            return f'Empty Linked List'
        # logic for linked list with single node
        current_node = self.headnode
        if current_node.nextnode == None:
            return f'Single Node Exists, removed it: {self.headnode}'
            self.rmvhead()
        # logic for linked list with more than one node
        while current_node.nextnode.nextnode != None:  # traverse upto second last node
            current_node = current_node.nextnode
        current_node = None
        self.nodecount -= 1

    # Deleting nodes by node's data.
    def rmvnode(self, nodedata):
        # logic for empty linked list
        if self.headnode == None:
            return f'Empty Linked List'
        # logic when nodedata is the headnode
        if nodedata == self.headnode.nodedata:
            return f'Deleted node with node data: {nodedata} for its first occurence in the linked list.'
            self.rmvhead()
            self.nodecount -= 1
        current_node = self.headnode
        while current_node.nextnode != None:
            if current_node.nextnode.nodedata == nodedata:
                break
            current_node = current_node.nextnode
        # case1: node with specified node data not found even just after tail node
        if current_node.nextnode == None:
            return f'Node with the specified node data: {nodedata} not found in the linked list.'
        # case2: node with specified node data  found upto tail node
        else:
            current_node.nextnode = current_node.nextnode.nextnode
            self.nodecount -= 1

    # Searching the index of a node in the linked List by node's data
    def nodeindex(self, nodedata):
        current_node = self.headnode
        index = 0
        while current_node != None:
            if current_node.nodedata == nodedata:
                return index
            current_node = current_node.nextnode
            index += 1
        return f'Node with given node data: {nodedata} not found in the linked list. '

    # Fetching node's data at a given index
    def __getitem__(self, nodeindex):
        current_node = self.headnode
        index = 0
        while current_node != None:
            if index == nodeindex:
                return current_node.nodedata
            current_node = current_node.nextnode
            index += 1
        return 'IndexError'

    # Traversing the Linked List and printing it.
    def __str__(self):
        if self.headnode == None:
            return f'Empty Linked List'
        current_node = self.headnode
        result = ''
        while current_node != None:
            result += str(current_node.nodedata) + '--->'
            current_node = current_node.nextnode
        return result[:-2]
    
    # replacing node with maximum 
    def replace_max_nodedata(self, new_nodedata):
        current_node = self.headnode
        node_with_max_nodedata = current_node

        while current_node != None:
            if current_node.nodedata > node_with_max_nodedata.nodedata:
                node_with_max_nodedata = current_node
            current_node = current_node.nextnode

        node_with_max_nodedata.nodedata = new_nodedata 

    # sum of node data of nodes at odd positions
    def sum_nodedata_odd_index(self):
        current_node = self.headnode
        counter = 0
        sum = 0

        while current_node != None:
            if counter % 2 != 0:
                sum += current_node.nodedata
            
            counter += 1
            current_node = current_node.nextnode

    # In place reversal : reversing the linked list without making a new linked list
    def inplace_reversal(self):
        previous_node = None
        current_node = self.headnode
        while current_node != None:
            next_node = current_node.nextnode
            current_node.nextnode = previous_node
            previous_node = current_node
            current_node = next_node

        self.headnode = previous_node










