import re
pattern=r'^[A-Za-z]+{2}$'
data='%@#'
if re.match(pattern,data):
    print('valid data')
else:
    print("Invalid data.")
    
    
    # OUtput error