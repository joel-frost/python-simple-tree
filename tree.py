class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def create_prefix(self):
        spaces = ' ' * self.get_level() * 3
        if self.parent:
            prefix = spaces + '|__'
        else:
            prefix = spaces
        return prefix

    def print_tree(self):
        prefix = self.create_prefix()
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    phone = TreeNode("Phone")
    macbook = TreeNode("Macbook")
    thinkpad = TreeNode("Thinkpad")
    iphone = TreeNode("iPhone")
    pixel = TreeNode("Google Pixel")
    galaxy = TreeNode("Galaxy S20")

    root.add_child(laptop)
    root.add_child(phone)
    laptop.add_child(macbook)
    laptop.add_child(thinkpad)
    phone.add_child(iphone)
    phone.add_child(pixel)
    phone.add_child(galaxy)

    return root


def main():
    root = build_tree()
    root.print_tree()


if __name__ == "__main__":
    main()