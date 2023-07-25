def line(line):
    if line == []:
        print("The line is currently empty.")
    else:
        list =[]
        for person in line:
            list.append(f" {line.index(person) + 1}. {person}")
        print(f"The line is currently:{ ''.join(list)}")
        pass

def take_a_number(customers,name):
    customers.append(name)
    print(f"Welcome, {name}. You are number {customers.index(name) + 1} in line.")
    pass

def now_serving(list):
    if list == []:
        print("There is nobody waiting to be served!")
    elif list != []:
        print(f"Currently serving {list[0]}.")
        del(list[0])
    pass