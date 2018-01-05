

import check
from myArray import Array

class Event:
    '''
    Fields:
    time (Int); indicates the time of the Event
    event (Str); indicates the name of the Event
    '''
    def __init__(self, time, event):
        self.time = time
        self.event = event

## find_first(disordered) finds the very first event (smallest timestamp) in a
## disordered Array and returns the value; where the time cost of the program
## would be O(log n) hence, we will be using a similar "binary search" algorithm
## find_first: Array -> Int
## Requires disordered to be an disordered Array where the Array was split into
## two Arrays and concatenated in the wrong order.
## Note: Event k.time > Event J.time iff k > j 
## Examples:
## Ex1: Given a disordered Array: 
## A = [(600,'1'),(650,'2'),(900,'3'),(100,'4'),(250,'5'),(300,'6')]
## find_first(A) => 100
## Ex2: Given a disordered Array:
## B = [(900,'1'),(100,'2'),(250,'3'),(300,'4'),(600,'4'),(650,'5')]
## find_first (B) => 100
## Ex3: Given a disordered Array:
## C = [(200,'1'),(300,'2'),(400,'3'),(500,'4'),(50,'5')]
## find_first (C) => 50
        
# using similar to a binary search method, where I discard half of the Array
# from the search continuoutly to achieve O (log n) run time
def find_first(disordered):
    lowestValue = None
    low = 0
    high = disordered.__len__()-1
    
    #initial mid index
    mid = (high+low)//2
    
    #start by using the middle as the lowest value
    lowestValue = disordered.__getitem__(mid).time     
    
    while low <= high:
        mid = (high + low) // 2
        
        #get the temporary mid value
        tmpMid = disordered.__getitem__(mid).time
        
        #replace with the new lowest value, is tmp is lower
        if tmpMid < lowestValue:
            lowestValue = tmpMid
        
        
        #getting the ndx bounds from each of the 2 splits
        firstHalfNdx = low
        firstEndNdx = mid - 1
        secondHalfNdx = mid + 1
        secondEndNdx = high
        
        # case when length Array is <= 2, need to adjust index
        if firstEndNdx < firstHalfNdx:
            firstEndNdx = firstHalfNdx
        if secondHalfNdx > secondEndNdx:
            secondHalfNdx = secondEndNdx
        
        #getting the bounds on the half splits
        firstHalf = disordered.__getitem__(firstHalfNdx).time
        firstEnd = disordered.__getitem__(firstEndNdx).time
        secondHalf = disordered.__getitem__(secondHalfNdx).time
        secondEnd = disordered.__getitem__(secondEndNdx).time
        
        
        #Case 1: smallest value is in the first half
    
        #firstHalf is in order and firsthalf has the lower values
        if firstHalf <= firstEnd and firstHalf <= lowestValue and\
           firstHalf <= secondHalf and firstHalf <= secondEnd:
            high = mid - 1
        #firstHalf in order, but smallest value in second half
        elif firstHalf <= firstEnd and firstHalf >= lowestValue and\
             firstHalf <= secondHalf and firstHalf <= secondEnd:
            low = mid + 1
        #firstHalf is not in order, but has the smallest value
        elif firstHalf >= firstEnd and firstEnd <= lowestValue and\
             firstEnd <= secondEnd:
            high = mid - 1

        
        #Case 2: smallest value is in the second half
        
        #second half is in order and second half has the lower value
        elif secondHalf <= secondEnd and secondHalf <= lowestValue and\
             secondHalf < firstHalf and secondHalf <= firstEnd:
            low = mid + 1
        #second half in order, but smallest value in first half
        elif secondHalf <= secondEnd and secondHalf >= lowestValue and\
             secondHalf < firstHalf and secondHalf <= firstEnd:
            high = mid - 1
        #secondHalf is disordered, but has the smallest value
        elif secondHalf >= secondEnd and secondEnd <= lowestValue and\
             secondEnd <= firstEnd:
            low = mid + 1

        
        #remaining case, we already have the lowest value
        else:
            low = mid + 1
            
    return lowestValue
            
    
## Tests

# Test Set 1 (even)     
E1 = Event(100, 'first')
E2 = Event(250, 'second')
E3 = Event(300, 'third')
E4 = Event(600, 'fourth')
E5 = Event(650, 'fifth')
E6 = Event(900, 'sixth')


#Disordered Array 1 [600,650,900,100,250,300]; perfect half split (even)
A1 = Array (6)
A1[0] = E4
A1[1] = E5
A1[2] = E6
A1[3] = E1
A1[4] = E2
A1[5] = E3
check.expect('Q3T1',find_first(A1),100)

#Disordered Array 2 [900,100,250,300,600,650]; right-tailing split (even)
A2 = Array(6)
A2[0] = E6
A2[1] = E1
A2[2] = E2
A2[3] = E3
A2[4] = E4
A2[5] = E5
check.expect('Q3T2',find_first(A2),100)

#Disordered Array 3 [250,300,600,650,900,100]; left-trailing split (even)
A3 = Array (6)
A3[0] = E2
A3[1] = E3
A3[2] = E4
A3[3] = E5
A3[4] = E6
A3[5] = E1
check.expect('Q3T3',find_first(A3),100)

# Test set 2 (odd)
E1 = Event(150, 'first')
E2 = Event(200, 'second')
E3 = Event(300, 'third')
E4 = Event(400, 'fourth')
E5 = Event(500, 'fifth')
E6 = Event(600, 'sixth')
E7 = Event(700, 'seventh')

#Disordered Array 4 [400,500,600,700,100,200,300]; almost even (odd)
A4 = Array (7)
A4[0] = E4
A4[1] = E5
A4[2] = E6
A4[3] = E7
A4[4] = E1
A4[5] = E2
A4[6] = E3
check.expect('Q3T4',find_first(A4),150)

#Disordered Array 5 [500,600,700,100,200,300,400]; almost even (odd)
A5 = Array (7)
A5[0] = E5
A5[1] = E6
A5[2] = E7
A5[3] = E1
A5[4] = E2
A5[5] = E3
A5[6] = E4
check.expect('Q3T5',find_first(A5),150)

#Disordered Array 6 [700,100,200,300,400,500,600]; right-trailing split (odd)
A6 = Array (7)
A6[0] = E7
A6[1] = E1
A6[2] = E2
A6[3] = E3
A6[4] = E4
A6[5] = E5
A6[6] = E6
check.expect('Q3T6',find_first(A6),150)

#Disordered Array 7 [200,300,400,500,600,700,100]; left-trailing split (odd)
A7 = Array (7)
A7[0] = E2
A7[1] = E3
A7[2] = E4
A7[3] = E5
A7[4] = E6
A7[5] = E7
A7[6] = E1
check.expect('Q3T7',find_first(A7),150)

# Test Set 3 (odd), different numbers

T1 = Event (12345,'answer')
T2 = Event (80000,'test')
T3 = Event (88888, '8')
T4 = Event (98765,'large')
T5 = Event (99999, 'hi')

# Disordered Array 8
A8 = Array (5)
A8[0] = T3
A8[1] = T4
A8[2] = T5
A8[3] = T1
A8[4] = T2
check.expect('Q3T8',find_first(A8),12345)
