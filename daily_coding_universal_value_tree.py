'''
create a class of Node
'''
class Node:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right

'''
create a tree
'''
left_subtree = Node(1, None, None)
right_subtree = Node(1, None, None)
tree = Node(1, left_subtree, right_subtree)
'''
create a in_order function
'''
def in_order(root):
	if root is None:
		return False
	#check the left-most nodes
	if root.left:
		in_order(root.left)

	print(str(root.value) + ', ', end = " ")

	in_order(root.right)

'''
check in_order
'''
in_order(tree)
print("")
'''
is_unival function
'''
def is_unival(root):
	if root is None:
		return True

	if root.left is not None and root.value != root.left.value:
		return False
	if root.right is not None and root.value != root.right.value:
		return False

	#recursive for left and right sub-tree
	if is_unival(root.left) and is_unival(root.right):
		return True

	return False

'''
count the number of univals
'''
def count_univals(root):
	if root is None:
		return 0

	#using recursive for total_count
	total_count = count_univals(root.left) + count_univals(root.right)

	if is_unival(root):
		total_count += 1

	return total_count

print("{}".format(count_univals(tree)))
