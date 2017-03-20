import hashlib
import os
import pkgutil


packages = pkgutil.iter_modules()
stringy = ""
for x in packages:
    stringy+=str(x).lower()
module_list = ["nmap"]

for module in module_list:
    query = stringy.find(module)
    if query < 0:
        print "\n          {} not found!".format(module)
        exit(0)
    else:
        print(hashlib.sha1('ex1_1_4').hexdigest())