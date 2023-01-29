# coin chonge
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

# power set recursive
def p(arr):
	s=arr
	if s:
		rest = p(s[1:])
		return rest + [[s[0]] + x for x in rest]
 	return [[]]

#powerset dynamic programming:

def get_subsets(fullset):
  listrep = list(fullset)
  subsets = [[]]
  for i in range(1,2**len(listrep)):
    subset = []
    for k in range(len(listrep)):      
      if i & 1<<k:
        subset.append(listrep[k])
    subsets.append(subset)    
  return subsets

def common_seq_helper(i,j):
	if i>len(str1) or j>len(str2):
		return 0
	if str1[i] == str2[j]:
		return 1+ common_seq_helper(i+1,j+1)
	else:
		return max(common_seq_helper(i+1,j),common_seq_helper(i,j+1))

# robot in the grid 
grid = [ [0,0,1,0],
		 [0,1,0,1],
		 [0,0,0,0],
		 [0,1,1,0]
]
	width=len(grid[0])
	depth=len(grid)


path=[ [ 0 for j in range(4) ] for i in range(4) ] 
def is_safe(row,column):
	if column<=width and row<=depth and grid[row][column] == 0:
		return True
	return False
def maze_runner(grid,start_r,start_c,f_r=n,f_c=n):
	if start_r == f_r and start_c == f_c:
		return path
	if is_safe(star_r, start_c):
		path[statr_r][start_c]='*'
	if maze_runner(grid,statr_r+1,start_c):
		return True
	if maze_runner(grid,statr_r,start_c+1):
		return True	
	else:
		path[statr_r][start_c]=0
		return False

#rod cutting:

def max_cat(prices, num_cats, length, profit=None):
	if profit==None:
		profit = -sys.max
	if length <=0:
		return profit
	for i in range(num_cats):
		profit = max([profit, prices[i]+max_cat(prices, length-i)])

# diving board design

def board_length(short_l, long_l, k, length=0):
	for short_n in range(k):
		length=short_l+short_n+long_l*(k-short_)
		legnths.append(length)
	return lengths


		









