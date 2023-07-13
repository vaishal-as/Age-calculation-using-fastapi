
def seperate(value):
    lst=[]
    lst1=[]
    for k in value.keys():
        lst=k.split(",")
    for l in value.values():
        lst1=l.split(",")
    values=dict(zip(lst,lst1))

    def group(values):
        groups = {
        'Teen': [],
        'Young Adult': [],
        'Adult': [],
        'Old': []
        }
            
        for k in values.keys():
            a=int(k)
            if a < 18:
                groups['Teen'].append(values[k])
            elif a >= 18 and a <= 25:
                groups['Young Adult'].append(values[k])
            elif a >= 26 and a <= 35:
                groups['Adult'].append(values[k])
            else:
                groups['Old'].append(values[k])
        return groups
    return group(values)
