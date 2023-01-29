# Stacks & Queues
class Multystack:
	def __init__(self, n=90):
		self.arr=[None]*n
		self.top1=-1
		self.top2=30
		self.top3=60
		self.min1=10**10
		self.min_index=None

	def stack1_add(value):
		if(self.top1>=30):
			raise ValueError('stack1 overflow! A bad thing happened.')
		self.arr[self.top1]=value
		self.top1+=1
		if value < self.min1:
			self.min=value
			self.min_index=top1


		def stack2_add(value):
		if(self.top1>=60):
			raise ValueError('stack2 overflow! A bad thing happened.')
		self.arr[self.top2]=value
		self.top2+=1

		def stack3_add(value):
		if(self.top3>=90):
			raise ValueError('stack3 overflow! A bad thing happened.')
		self.arr[self.top3]=value
		self.top3+=1

		def stack1_pop():
			item=arr[top1]
			arr[top1]=None
			top1 -= 1

		def stack1_min():
