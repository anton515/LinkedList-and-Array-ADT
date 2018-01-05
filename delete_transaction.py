import check

class Record:
    ''' 
    Fields:
    merchandise (Str); indicates the merchandise of this transaction
    time (Int); represented using Unix timestamp (which is the number of seconds
    that have elapsed since Jan 1, 1970 at midnight UTC/GMT)
    prev_trans (Record); reference to the previous transaction
    '''
    def __init__(self, merchandise, time, prev):
        self.merchandise = merchandise
        self.time = time
        self.prev_trans = prev
    
    def tranverse (head):
        curNode = head
        while curNode != None:
            print (curNode.merchandise)
            curNode = curNode.prev_trans

    def __eq__(self, other):
        if type(self) != type(other) :
            return False
        if self.merchandise == other.merchandise and \
            self.time == other.time :
            return self.prev_trans == other.prev_trans
        return False

    def __ne__(self, other):
        return not self == other

    #Converts record list into a string, where the head of the list is on the left
    #(merch, time)(merch, time)....
    def __str__(self):
        rest_of_list = ""
        if self.prev_trans != None:
            rest_of_list = str(self.prev_trans)
        return "({},{})".format(self.merchandise, self.time) + rest_of_list


## delete_transaction (head_trans,m) deletes the m-th transaction happened in
## this month given the head reference of the leger, and returns the 
## merchandise field value of the deleted transaction record.
## Effect: deletes the m-th transaciton that happened in this month of the leger
## given the head reference.
## delete_transaction: Record Int -> Str
## Requires: m to be a valid index ( 1 <= m < n), where n is the index of the
## most recent transaction. Hence would require head_trans to contain 
## at least 2 or more elements (links to previous transactions) in the linked
## list
## Examples:
## Given linked list:
    #tx1 = Record ('apple',1580,None)
    #tx2 = Record ('banana',2390,tx1)
    #tx3 = Record ('carrot',3452,tx2)
    #tx4 = Record ('doll',3789,tx3)
## Ex1:
## delete_transaction(tx4,3) => 'carrot'
## and will delete the tx3 link from the linked list with tx4 head.
## Ex2: continuation after last delete
## delete _transaction(tx4,2) => 'banana'
## and will delete the tx2 link from the linked list with tx4 as head.
## Ex3: continuation after last delete
## delete_transaction(tx4,1) => 'apple'
## and will delete the tx1 link from the linked lsit with tx4 as head.

def delete_transaction(head_trans , m):
    #get the node that we want to delete, call it prevNode
    prevNodeCount = 1
    prevNode = None
    tmp = head_trans
    curNode = head_trans
    while curNode != None:
        #loop until the node we want to delete is 'm-1' infront of the head node
        if prevNodeCount != m:
            prevNode = None
            curNode = curNode.prev_trans
            prevNodeCount += 1
        else:
            prevPrevNode = prevNode
            prevNode = tmp
            tmp = tmp.prev_trans
            curNode = curNode.prev_trans
    #relink the nodes to delete the prevNode
    prevPrevNode.prev_trans = prevNode.prev_trans
    return prevNode.merchandise
    
       
## Tests
tx1 = Record ('apple',1580,None)
tx2 = Record ('banana',2390,tx1)
tx3 = Record ('carrot',3452,tx2)
tx4 = Record ('doll',3789,tx3)

## Test1 delete transaction before head
check.expect('Q1T1',delete_transaction(tx4,3),'carrot')        
## Test2, continuation...delete transaction in middle
check.expect('Q1T2',delete_transaction(tx4,2),'banana')
## Test3, continuation... delete first transaction
check.expect('Q1T3',delete_transaction(tx4,1),'apple')

ls1 = Record('soap',1000,None)
ls2 = Record('toothbrush',1500,ls1)
ls3 = Record('string',2500,ls2)
ls4 = Record('broom',3000,ls3)
ls5 = Record('hat',4000,ls4)
ls6 = Record('pant',5000,ls5)
ls7 = Record('shirt',6000,ls6)

## Test4, delete transaction in the middle (4)
check.expect('Q1T4',delete_transaction(ls7,4),'broom')
## Test5, continuation, delete the least-recent (first) transaction (1)
check.expect('Q1T5',delete_transaction(ls7,1),'soap')
## Test6, continuation, delete the 2nd most-recent transaction (4)
check.expect('Q1T6',delete_transaction(ls7,4),'pant')
## Test7, continuation, delete the 2nd transaction (2)
check.expect('Q1T7',delete_transaction(ls7,2),'string')