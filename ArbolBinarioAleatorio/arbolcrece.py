import random 

class Node: 
	def __init__(self, value): 
		self.value = value 
		self.left = None
		self.right = None

def abrol_binario_random(size): 
	if size == 0: 
		return None

	left_size = random.randint(0, size-1) 
	right_size = size - 1 - left_size 

	left_subtree = abrol_binario_random(left_size) 
	right_subtree = abrol_binario_random(right_size) 
 
	root = Node(random.randint(0, 10)) 
 
	root.left = left_subtree 
	root.right = right_subtree 

	return root 


def print_tree(node, level=0): 
	if node is not None: 
		print_tree(node.right, level + 1) 
		print(" " * 4 * level + "->", node.value) 
		print_tree(node.left, level + 1) 


tree = abrol_binario_random(8) 
print_tree(tree) 
