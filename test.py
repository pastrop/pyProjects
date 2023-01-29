class Parking():
  """docstring for Parking"""
  def __init__(self, number_of_spaces=50):
    self.number_of_spaces = number_of_spaces
    self.free_spaces=number_of_spaces
    parked = {}

  def car_in(self, Vehicle):
    if self.free_spaces == 0:
      print('Sorry dude, we are full')
      return 'space is full'
    print('arrived {}'.format(Vehicle.make))
    parked[Vehicle.id]=Vehicle.make
    self.free_spaces =- 1

  def car_out(self, Vehicle):
    print('left {}'.format(Vehicle.make))
    self.free_spaces =+ 1
    parked.pop(Vehicle.id, None)

class Car():
  """docstring for """
  def __init__(self, plate, make):
    self.plate=plate
    self.make=make

class Deck():
  def __init__(self, size=36):
    self.size=size
    self.suit=['spade','club','diamond','heart']
    self.rank=['6','7','8','9','10','jack','queen','king','ace']
    self.card_deck=[]
    if size == 16:
      for i in range(len(self.suit)):
        for j in range(5,len(self.rank)):
          self.card_deck.append(Card(self.suit[i],self.rank[j]))


class Card():
  def __init__(self, typ, value):
    self.typ=typ
    self.value=value

#mydeck=Deck(16)
#for i in range(16):
  #print('suit {} - value {}'.format(mydeck.card_deck[i].typ,mydeck.card_deck[i].value))


def mergeSort(alist):

   print("Splitting ",alist)

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0
       print('lefthalf before while ',lefthalf)
       print('righthalf before while ',righthalf)


       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               print('lefthalf-',lefthalf[i])
               print('righthalf-',righthalf[j])
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1
           print('alist-',alist)

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1
           print('2nd While alist-',alist)

       while j < len(righthalf):
           alist[k]=righthalf[j]
           print('3rd While alist-',alist,k)
           j=j+1
           k=k+1

   print("Merging ",alist)

alist = [5,9]
mergeSort(alist)
print(alist)  