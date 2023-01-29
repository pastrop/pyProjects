# binary search recursive
def bin(arr, target):
	mid=len(arr)//2
	high=mid
	low=mid+1
	if arr[mid] == target:
		return True
	if low>mid:
		return None
	bin(arr[:mid],target)
	bin(arr[low:],target)

n = 5
coins = [1,5,10,25]

def change(coins, amount, coins_given):
	if amount == sum(coins_given):
		yield coins_given
	elif amount<sum(coins_given):
		pass
	elif coins == []:
		pass
	else:
		for c in change(coins[:], amount, coins_given+[coins[0]]):
			yield c
		for c in change(coins[1:], amount, coins_given):
			yield c

gen = change(coins,n,[])

def dfs(graph, start):
	stack=[start]
	visited=set()
	while stack:
		node=stack.pop()
		visited.add(node)
		stack.extend(graph[node]-visited)
	return visited

def dfs_path(graph, start, finish):
	stack=[(start, path[start])]
	while stack:
		(node,path)=stack.pop()
		if node == finish:
			return path.append(node)
		for vertex in graph[node]:
			stack.append((graph[vertex],path.append(vertex)))






			

