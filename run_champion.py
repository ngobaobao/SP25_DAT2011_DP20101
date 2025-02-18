import os, importlib

def dynamic_import(champion_folder, champion_file):
    module_name = champion_folder + '.' + champion_file
    module_name = module_name.replace('.py', '')
    module = importlib.import_module(module_name)

    class_name = champion_file.replace('.py','')
    cls = getattr(module, class_name)

    champion = cls()
    return champion

champion_folder = 'champions'

champion_files = os.listdir(champion_folder)

champion_dict = {}
menu_opt_dict = {}
for idx, champion_file in enumerate(champion_files):
    if not champion_file.endswith('.py'):
        continue
    champion = dynamic_import(champion_folder, champion_file)
    champion_dict[idx + 1] = champion
    menu_opt_dict[idx + 1] = champion.get_name()

def menu(menu_opt_dict):
    print("LOL PROGRAM")
    for key in menu_opt_dict:
        champion_name = menu_opt_dict[key]
        print(key, '-', champion_name)
    print('99 - Quit')

def select_skills(champion):
    opt = input('Please select skill to cast (Q - W - E - R): ')
    opt = opt.upper()
    print(champion)
    if opt == 'Q':
        return champion.cast_skill_q()
    elif opt == 'W':
        return champion.cast_skill_w()
    elif opt == 'E':
        return champion.cast_skill_e()
    elif opt == 'R':
        return champion.cast_skill_r()
    else:
        return 'No cast'

while True:
    menu(menu_opt_dict)
    try:
        opt = int(input('Please select Champion: '))
        if opt == 99:
            break
        champion = champion_dict[opt]
        print('You select:', champion.get_name())
        cast_skill = select_skills(champion)
        print(champion.get_name(), 'cast', cast_skill)

        input('Enter something here to continue...')
        os.system('cls')
    except Exception as e:
        print('Error: ', e)