my_family = {}

def add_family_member(role,name):
    if role == 'bror':
        brødre.append(name)
        my_family[role] = brødre
    elif role == 'mor':
        mødre.append(name)
        my_family[role] = mødre
    elif role == 'far':
        fedre.append(name)
        my_family[role] = fedre
    elif role == 'søster':
        søstre.append(name)
        my_family[role] = søstre

brødre = []
mødre = []
fedre = []
søstre = []

add_family_member('bror','Stian')
add_family_member('bror','Arne')
add_family_member('søster','Heidi')
add_family_member('søster','May')
print(my_family)


