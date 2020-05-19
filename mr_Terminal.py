
from commands_dict import commands
from cmd_func import pwd


print("\n\n\n\n\n  ***** MR. Terminal *****   ")


print('\n\n')

if __name__ == '__main__':
    while True:
        pwd_dir = pwd()
        print()
        user_cmd  =  input(pwd_dir+' ~$ ')
        if user_cmd == 'exit':
            break
        try:
            cmd , agrs = user_cmd.split(' ')
            cmd_func = commands[cmd]
            result = cmd_func(agrs)
            if not result:
                print('   Directory not found')

            continue
        except ValueError:
            cmd_func = commands[user_cmd]
            results = cmd_func()
            for n,line in enumerate(results):
                print('     '+str(n) + '->  '+ line)
