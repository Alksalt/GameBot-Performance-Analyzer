class BinarySearchTreeNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


    def add_child(self, data):
        if data == self.data:
            return

        elif data < self.data:

            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data, parent=self)
        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data, parent=self)


    def in_order_traversal(self):
        elements = []
        #visit left side
        if self.left:
            elements += self.left.in_order_traversal()

        #visit root (base)
        elements.append(self.data)

        #visit right side
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if val == self.data:
            return True

        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def advanced_search(self, data, count=1):
        if data == self.data:
            return count
        elif data < self.data:
            if self.left:
                return self.left.advanced_search(data, count + 1)
            else:
                return -1

        else:
            if self.right:
                count += 1
                return self.right.advanced_search(data, count + 1)
            else:
                return -1

    def print_tree(self, lvl=0,prefix='Root__'):
        print(' ' * (lvl * 4) + prefix + str(self.data))
        if self.left:
            self.left.print_tree(lvl + 1,prefix='L__')
        if self.right:
            self.right.print_tree(lvl + 1, prefix ='R__')

    def find_min(self):
        if self.data:
            if self.left:
                return self.left.find_min()
            else:
                return self.data

    def find_max(self):
        if self.data:
            if self.right:
                return self.right.find_min()
            else:
                return self.data

    def calculate_sum(self, result=0):
        if self.data:
            result += self.data
        if self.left:
            result = self.left.calculate_sum(result)
        if self.right:
            result = self.right.calculate_sum(result)

        return result

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def pre_order_traversal_two(self, lvl=0):
        elements = []

        print("  " * lvl + f"Visiting node: {self.data}")
        elements.append(self.data)

        if self.left:
            print("  " * lvl + f"Going LEFT from {self.data}")
            elements += self.left.pre_order_traversal_two(lvl + 1)

        if self.right:
            print("  " * lvl + f"Going RIGHT from {self.data}")
            elements += self.right.pre_order_traversal_two(lvl + 1)

        print("  " * lvl + f"Returning from node {self.data}: {elements}")
        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def get_max_depth(self):
        left_depth = self.left.get_max_depth() if self.left else 0
        right_depth = self.right.get_max_depth() if self.right else 0
        return 1 + max(left_depth, right_depth)


    def get_lvl(self):
        lvl = 0
        p = self.parent
        while p:
            lvl += 1
            p = p.parent
        return lvl

    def lvl_descend_traversal(self, lvl=0, elements=None):
        if elements is None:
            elements = {}

        elements.setdefault(lvl, []).append(self.data)

        if self.left:
             self.left.lvl_descend_traversal(lvl + 1,elements=elements)

        if self.right:
            self.right.lvl_descend_traversal(lvl + 1, elements=elements)

        return elements

    def delete_node_min(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node_min(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_node_min(val)
        else:
            if not self.right and not self.left:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node_min(min_val)
        return self

    def delete_node_max(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node_max(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_node_max(val)
        else:
            if not self.right and not self.left:
                return None
            if not self.left:
                return self.right
            if not self.right:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_node_max(max_val)
        return self

def build_bi_tree(elements):
    tree = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        tree.add_child(elements[i])
    return tree

if __name__ == '__main__':
    numbers = [50,40,30,20,10,35,40,55,70,90,100]
    tree_func = build_bi_tree(numbers)
#    print(tree_func.advanced_search(10) if tree_func.search(10) else -1)
#    print(tree_func.find_min())
#    print(tree_func.calculate_sum())
#    print(tree_func.pre_order_traversal())
#    print(tree_func.post_order_traversal())
#    print(tree_func.lvl_descend_traversal())
#    print(tree_func.pre_order_traversal_two())
    print(tree_func.print_tree())
    print(tree_func.delete_node(70))
    print(tree_func.delete_node(30))
    print(tree_func.delete_node(10))
    print(tree_func.delete_node(90))
    print(tree_func.in_order_traversal())



#print(sum([50,40,30,20,10,35,40,55,70,90,100]))

