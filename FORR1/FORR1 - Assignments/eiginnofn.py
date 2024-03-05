def create_name_folder():
    resident_folder = {}
    for i in range(int(input())):
        name = input()
        first_name = name.split()[0]
        if more_than_one_name(name):
            last_name = name.split()[1]
            resident_folder[first_name] = last_name
        else:
            resident_folder[first_name] = 0

    return resident_folder

def more_than_one_name(name):
    if len(name.split()) > 1:
        return True
    else:
        return False

def resident_is_home(resident):
    if resident in resident_folder:
        return True
    else:
        return False
    
def check_for_name():
    name = input()
    if not resident_is_home(name):
        print("Neibb")
    else:
        last_name = resident_folder[name]
        if last_name == 0:
            print("Jebb")
        else:
            print(f"Neibb en {name} {last_name} er heima")

resident_folder = create_name_folder()
for i in range(int(input())):
    check_for_name()