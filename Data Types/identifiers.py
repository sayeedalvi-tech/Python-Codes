print("sample".isidentifier())


[D:\QSpiders\Python>python identifiers.py
True]

import keyword
print("True".isidentifier() and not keyword.kwlist)

D:\QSpiders\Python>python identifiers.py
False