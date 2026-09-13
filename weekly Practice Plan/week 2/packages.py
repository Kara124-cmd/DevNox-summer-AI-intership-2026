
'''Python Packages
Suppose you have developed a very large application that includes many modules. As the number of modules grows, it becomes difficult to keep track of them all if they are dumped into one location. This is particularly so if they have similar names or functionality. You might wish for a means of grouping and organizing them.

Packages allow for a hierarchical structuring of the module namespace using dot notation. In the same way that modules help avoid collisions between global variable names, packages help avoid collisions between module names.

Creating a package is quite straightforward, since it makes use of the operating system's inherent hierarchical file structure. Consider the following arrangement:

'''

# first create a folder name pkg and in it create to module "mod1" and 'mod2' and then import

import pkg.mod1, pkg.mod2
name = pkg.mod1.name()
print(name)

add = pkg.mod2.add(3,5)
print(add)

# also you can write
from pkg import mod1
x = mod1.name()
print(x)
print(mod1)

# you can also write the package like this
from pkg.mod2 import add as d
x = d(2,5)
print(x)





'''Package Initialization
If a file named __init__.py is present in a package directory, it is invoked when the package or a module in the package is imported. This can be used for execution of package initialization code, such as initialization of package-level data.
'''

# For example, consider the following __init__.py file:

# Now when the package is imported, the global list A is initialized:

import pkg                  # Invoking __init__.py for pkg
pkg.A                       # ['quux', 'corge', 'grault']


from pkg import mod1
mod1.name



# then when you execute import pkg, modules mod1 and mod2 are imported automatically:

import pkg
pkg.mod1.name()     # Invoking __init__.py for pkg

add = pkg.mod2.add(2,6)
print(add)


