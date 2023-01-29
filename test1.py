class Node:
	def __init__ (self, id, next=None):
		self.id=id
		self.next=next

	def get_next(self):
		return self.next

class Linked:
	def __init__(self, head=None):
		self.head = head

	def return_head(self):
		return self.head


node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)


nodeList=Linked(node1)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node3



def findCycle(linked):
	nodeslow=nodefast=linked.return_head()
	counter=0
	while nodeslow.next and counter < 6:
		print('nodeslow- {} -- nodefast- {}'.format(nodeslow.id,nodefast.id))
		slow=nodeslow.next.id
		fast=nodefast.next.next.id
		print('pointers: slow-{}--fast-{}'.format(slow,fast))
		counter=counter+1
		if slow == fast:
			print('cycle is found!')
			return True
		nodeslow=nodeslow.get_next()
		nodefast=nodefast.get_next().get_next()


findCycle(nodeList)
