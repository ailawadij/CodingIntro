from Chef import Chef
class ChineseChef(Chef):
# Inheritance allows you to apply credentials from one class to another
# If something is explicitely stated like maing a special dish, it can override the class that it is inheriting from

    def make_special_dish(self):
        print("The chef makes orange chicken")
    def make_fried_rice(self):
        print("The chef makes fried rice")

