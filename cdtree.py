from collections import OrderedDict
# Binary Search Tree

class Node():
	def __init__(self, value):
		self.value=value
		self.left=None
		self.right=None

	def insert(self, value):
		if value < self.value:
			if self.left == None:
				self.left = Node(value)
			else:
				insert(self.left, value)
		if value > self.value:
			if self.right == None:
				self.right = Node(value)
			else:
				insert(self.right, value)

	def traverse(self,start):
		while start:
			print(start.value)
			traverse(start.left)
			traverse(start.right)



#takes sorted array
def arr_to_bst(arr):
	index=len(arr)//2
	if index == 0:
		return None
	node=Node(arr[index])
	node.left = arr_to_bst(arr[:index])
	node.right = arr_to_bst(arr[index+1:])
	return node

# DFS & BFS
def dfs(graph, start):
	stack=[start]
	visited=set(start)
	while stack:
		node=stack.pop()
		if node is not in visited:
			visited.add(node)
		stack.extend(graph[node]-visited)
	return visited

def dfs_r(graph, start, visited=None):
	if visited is None:
		visited=set()
	for node in graph[start]-visited:
		dfs_r(graph, start)
	return visited


def bfs(graph, start): #including tree levels
	queue=[start]
	visited=set(start)
	levels=[visited]
	while queue:
		node=stack.pop(0)
		if node is not in visited:
			visited.add(node)
		queue.extend(graph[node]-visited)
		levels.extend(graph[node])
	return visited
	
# tree height
def maxheight(root):
	if root==None:
		return 0
	return 1+max(maxheight(root.right),maxheight(root.left))

def minheight(root):
	if root==None:
		return 0
	return 1+min(minheight(root.right),minheight(root.left))

template=OrderedDict()
guess=OrderedDict()
def mind_game():

	for i,j in zip(template,guess):
		if i==j:
			return 'direct hit'
		else:








