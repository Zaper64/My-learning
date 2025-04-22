import random
arry =[]

for i in range(0,10):
    arry.append(random.randint(1,15))
    print(arry[i], end=' ')
print('')


def mymap(func, arr):
    result = []
    myiter = iter(arr)
    for item in arr:
        new_item = func(next(myiter))
        result.append(new_item)
    return result

new_arr = mymap((lambda x: x**2), arry)
myiter = iter(new_arr)
i=0
for i in range(0, len(new_arr)):
    print(next(myiter), end=' ')
print('')

def qsort(arr):
    length = len(arr)
    if len(arr) < 2:
        return arr
    
    marker = arr[length // 2]
    left, middle, right = [],[],[]
    for i in range(0,length):
        if arr[i] < marker:
            left.append(arr[i])
        elif arr[i] == marker:
            middle.append(arr[i])
        else:
            right.append(arr[i])
    
    return (qsort(left) + middle + qsort(right))

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__():
        return self.data

class linked_list:
    def __init__(self, nodes=None):
        self.head = None

        try:
            data = nodes.pop(0)
        except:
            return  

        node = Node(data)
        self.head = node

        for item in nodes:
            node.next = Node(data=item)
            node = node.next
        else:
            self.end = node
    
    def __repr__(self):
        node = self.head
        nodes =[]
        while node != None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')

        return ' -> '.join(nodes)
    
    def conv_to_aray(self, n=-1):
        node = self.head
        if n == -1:
            while node != None:
                yield node.data
                node = node.next      
        else:
            for i in range(0, n):
                if node == None:
                    break
                else:
                    yield node.data
                    node = node.next

    def find_node(self, target):
        node = self.head
        position = 1
        found = False
        while node.next != None:
            if int(node.data) == target:
                return position
                found = True
            position = position + 1
            node = node.next
        if not(found):
            return (-1)
    
    def add_start(self, new_node):
        if self.head == None:
            self.head, self.end = new_node, new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def add_end(self, new_node):
        if self.head == None:
            self.head = new_node
            self.end = new_node
            return
        node = self.end
        node.next = new_node
        new_node.next = None
        self.end = new_node

    def add_after(self, target, new_node):
        if self.head is None:
            print("List is empty")
            return -1
        
        node = self.head
        position = linked_list.find_node(self, target)
        if (position != -1):
            if position > 1:
                for i in range(0, position-1):
                    node = node.next
            if (node.next == None):
                linked_list.add_end(self, new_node)
            else:
                new_node.next = node.next
                node.next = new_node
        else:
            print('The target value is not present.')
        return
    
    def remove_node(self, target):
        if self.head == None:
            print('List is empty')
            return -1
        
        node = self.head
        found = False

        while (node.next != None) and (found == False):
            if node.next.data == target:
                found = True
            else:
                node = node.next
        if not(found):
            print('This value is not present in the list')
            return -1
        else: 
            node.next = (node.next).next          



new_arr = qsort(new_arr)
list = linked_list(new_arr)
print(list.__repr__())

xyz = Node(23)
list.add_end(Node(23))
list.add_after(144,Node(7))
list.remove_node(64)
print(list.__repr__())

# n = 6
# itterable = (list.__iter__(n))
# for i in range(0, n):
#     print(next(itterable), end=' ')


