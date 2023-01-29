# base conversion
def base_2_r(n):
	if n==0:
		return '0'
	return base_2_r(n//2)+str(n%2)


def base_2(n):
	result=''
	while n>0:
		result=str(n%2)+result
		n=n//2
	return result


class Linked():
	def __init__(self, value, next=None):
		self.value=value
		self._next=next

	def set_next(self, next):
		self._next=next

	def get_next(self):
		return self._next

	def doop_killer(self,other):
		if self.value==other.value:
			if self.next == other:
				self.next=other.next
			if other.next == self:
				other.next=other.next
			else:
				return "these two are not adjucent!"
				

node1=Linked('Mon')
node2=Linked('Tue')
node3=Linked('Wed')
node4=Linked('Thu')
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)



class Linked_lst():
	def __init__(self, root=None):
		self.root=root

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


# Preorder traversal
# Root -> Left ->Right
    def PreorderTraversal(self, root, res=None):
        if res==None:
        	res=[]
        if root:
            res = res+self.PreorderTraversal(root.left)
            res.append(root.data)
            res = res+self.PreorderTraversal(root.right)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

_end = '*'

# takes in a list of words
def make_trie(words):
	dic = {}
	for item in words:
		# create a temporary dict based off our root dict object
		temp_dict = dic.setdefault(item,{})
        
        for letter in item:
            # update our temporary dict and add our current
            # letter and a sub-dictionary
            temp_dict = temp_dict.setdefault(letter, {})
        
        # If our word is finished, add {'*': '*'}  
        # this tells us our word is finished
        temp_dict[_end] = _end
	return dic

class MyMinheap:
	def __init__(self):
		self.arr=[0]
		self.size=len(self.arr)

	def insert(self,item):
		self.arr.append(item)
		sift_up(self.size)

	def sift_up(self, index):
		if index == 1:
			return
		if self.arr(index) < self.arr[index//2]:
			self.arr(index), self.arr(index//2)=self.arr(index//2), self.arr(index)
			index=index//2
			sift_up(index)
		else:
			return

import stdio
import stdarray
import sys
import random

# Accept integers m and n, and float p as command-line arguments.
# Create a m x n minesweeper game where each cell is a bomb with
# probability p. Write the m x n game and the neighboring bomb counts
# to standard output.

m = int(sys.argv[1])
n = int(sys.argv[2])
p = float(sys.argv[3])

# Create bombs as a m+2 * n+2 array.
bombs = stdarray.create2D(m+2, n+2, False)

# bombs is [1..m][1..n]; the border is used to handle boundary cases.
for r in range(1, m+1):
    for c in range(1, n+1):
        bombs[r][c] = (random.random() < p)

# Write the bombs.
for r in range(1, m+1):
    for c in range(1, n+1):
        if bombs[r][c]:
            stdio.write('* ')
        else:
            stdio.write('. ')
    stdio.writeln()

# Create solution as a m+2 x n+2 array.
solution = stdarray.create2D(m+2, n+2, 0)

# solution[i][j] is the number of bombs adjacent to cell (i, j).
for r in range(1, m+1):
    for c in range(1, n+1):
        # (rr, cc) indexes neighboring cells.
        for rr in range(r-1, r+2):
            for cc in range(c-1, c+2):
                if bombs[rr][cc]:
                    solution[r][c] += 1

# Write solution.
stdio.writeln()
for r in range(1, m+1):
    for c in range(1, n+1):
        if bombs[r][c]:
            stdio.write('* ')
        else:
            stdio.write(str(solution[r][c]) + ' ')
    stdio.writeln()

