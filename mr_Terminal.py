
from commands_mapper import commands
from cmd_func import pwd
import os



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
            if result.err:
                print(err)
                continue
            for line in result.content:
                print(line)

            continue
        
        except KeyError:
            SRED = '\033[31m'    # Warning color
            CEND = '\033[0m'
            print('%s this command is not recognized %s' % (SRED,CEND))

        except ValueError:
            try:
                cmd_func = commands[user_cmd]
                results = cmd_func()
                for n,line in enumerate(results):
                    print('     '+str(n) + '->  '+ line)
            except KeyError:
                SRED = '\033[31m'    # Warning color
                CEND = '\033[0m'
                print('%s this command is not recognized %s' % (SRED,CEND))
            
                continue
