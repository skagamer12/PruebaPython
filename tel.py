
    
base = int(input("base:"))
alt = int(input("altura"))


def cut_rect(wdth,lng):
    cubos = []
    while lng!=0:
        if wdth > lng:
            cubos.append(lng)
            wdth = wdth-lng
            
        else:
            cubos.append(wdth)
            lng = lng - wdth
            
    print(cubos)


print(cut_rect(base,alt))