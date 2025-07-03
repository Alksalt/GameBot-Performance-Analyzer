from collections import deque
class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = deque()
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def delete_node(self, target_node):

        for child in self.children:
            if target_node == child:
                self.children.remove(child)
                return True
            else:
                if child.delete_node(target_node):
                    return True

        return False

    def get_lvl(self):
        lvl = 0
        p = self.parent
        while p:
            lvl += 1
            p = p.parent

        return lvl

    def print_nodes(self, what):
        spaces = ' ' * self.get_lvl() * 4
        prefix = spaces + '|__' if self.parent else ''
        if what == 'name':
            print(prefix + self.name)
        elif what == 'designation':
            print(prefix + self.designation)
        elif what == 'both':
            print(prefix + f'{self.name} ({self.designation})')
        else:
            raise ValueError(f"Invalid argument: '{what}'. Use 'name', 'designation', or 'both'.")
        for child in self.children:
            child.print_nodes(what)

    def print_nodes_by_lvl(self, lvl):
        current_lvl = self.get_lvl()
        if current_lvl > lvl:
            return
        spaces = ' ' * self.get_lvl() * 4
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + f'{self.name} ({self.designation})')

        for child in self.children:
            child.print_nodes_by_lvl(lvl)


def build_company_tree():
    ceo = TreeNode("Nilay", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    dev_manager = TreeNode("Vasya", "Dev Manager")
    developer = TreeNode("Katya", "Developer")
    dev_manager.add_child(developer)
    cto.add_child(dev_manager)

    cfo = TreeNode("Satish", "CFO")
    accountant = TreeNode("Oleksiy", "Accountant")
    cfo.add_child(accountant)

    hr_head = TreeNode("Priya", "HR Head")
    recruiter = TreeNode("Diana", "Recruiter")
    hr_head.add_child(recruiter)

    ceo.add_child(cto)
    ceo.add_child(cfo)
    ceo.add_child(hr_head)

    return ceo


if __name__ == '__main__':
    ceo = build_company_tree()
    #ceo.print_nodes('both')
    ceo.print_nodes_by_lvl(3)