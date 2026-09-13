'''__init__.py can also be used to effect automatic importing of modules from a package. For example, earlier you saw that the statement import pkg only places the name pkg in the caller's local symbol table and doesn't import any modules. But if __init__.py in the pkg directory contains the following:
'''
import pkg.mod1, pkg.mod2
print(f'Invoking __init__.py for {__name__}')
A = ['quux', 'corge', 'grault']