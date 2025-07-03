class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def __len__(self):
        return self.get_lvl()

    def delete_node(self, target_node):

        for child in self.children:
            if target_node == child:
                self.children.remove(child)
                return True
            else:
                if self.delete_node(target_node):
                    return True

        return False

    def get_lvl(self):
        lvl = 0
        p = self.parent
        while p:
            lvl += 1
            p = p.parent
        return lvl

    def print_tree(self):
        spaces = ' ' * self.get_lvl() * 2
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()
if __name__ == '__main__':
    build_tree()