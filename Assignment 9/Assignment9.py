class user_defined_exception(Exception):
    def __init__(self,arg):
        self.arg = arg

import math_op as c

try:
    raise user_defined_exception("It is a User Defined Exception")
except user_defined_exception as u:
    print(u.arg)
obj = c.math_o(18,41)
obj.power()
obj.trigno()
obj.basic()
obj.rest()