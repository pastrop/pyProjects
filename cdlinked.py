# Linked List
class Node():
	def __init__(self, value):
		self.value=value
		self.next=None

class Linked():
	def __init__(self, head):
		self.head=head

	def delete(self, value):
		item=self.head
		if item.value == value:
			self.head = self.head.next
			return
		while item:
			if item.next.value == value:
				item.next=item.next.next
			item=item.next

	def to_array(self):
		arr=[]
		item=self.head
		while item:
			arr.append(item.value)
			item=item.next
		return arr

	def detectLoop(self):
		item=fastitem=slow=fast=self.head
		while item:
			if item.next !=None and item.next.next != None:
				slow=item.next
				fast=fastitem.next.next
				if slow.value == fast.value:
					return 'loop was detected'
				item=item.next
				fastitem=fastitem.next.next
		return 'no loop!'









node1=Node("Mon")
node2=Node("Tue")
node3=Node("Wed")
node4=Node("Thu")

node1.next=node2
node2.next=node3
node3.next=node4

week=Linked(node1)

print(week.to_array())


