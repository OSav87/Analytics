scanning = False

data = 'path_to_file'

for i in data:
    
    if i.startswith('x'):
        scanning = False
        continue
        
    if scanning:
        print(i)
    
    if 'y' in i:
        scanning = True
        continue