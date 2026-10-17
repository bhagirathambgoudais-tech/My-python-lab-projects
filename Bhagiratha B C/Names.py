colours=["Red","Green","Maroon"]
colours[1]="pink"
print(colours)

Mixed_list=["Red",10,"Green",20,"Blue"]
print("Mixed_one=",Mixed_list[1::2])
print("Mixed two=",Mixed_list[2::2])

Mixed_one=[]
Mixed_two=[]
for item in Mixed_list:
    if isinstance(item,(int,float)):
        Mixed_one.append(item)
    else:
        Mixed_two.append(item)
        
Mixed_list.clear()
        



