"""define a function that has 4 parameters, if replaces all (sub-)interface IP addresses
that start with '172.' with IP addresses that start with '192.'"""

import os
def sed(pattern_string,replacment_string,f1,f2):
    f_1 = open(f1)
    f_2 = open(f2,'w')

    for line in f_1:
        if pattern_string in line:
            newline = line.replace(pattern_string,replacement_string)
            f_2.write(newline)
        else:
            f_2.write(line)
    return f_2


f1 = "running-config.cfg"
f2 = "new-running-config.cfg"
pattern_string = "172"
replacement_string = "192"
sed(pattern_string,replacement_string,f1,f2)

