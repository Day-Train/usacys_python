from hashlib import sha1

from modules.ex1_2_3_module import useful_function

print(sha1(useful_function(37)).hexdigest())