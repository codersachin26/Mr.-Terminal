
from commands_mapper import commands
from cmd_func import pwd,command_error
import os
import gc



print("\n\n\n\n\n  ***** MR. Terminal *****   ")


print('\n\n')

if __name__ == '__main__':
    while True:
        gc.collect()
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
                print(result.err)
                continue
            if  result.content:
                for line in result.content:
                    print(line)

            continue
        
        except KeyError:
            command_error()


        except ValueError:
            try:
                cmd_func = commands[user_cmd]
                result = cmd_func()
                if result.err:
                    print(result.err)
                    continue
                if result.content:
                    for line in  result.content:
                        print(line)
            except KeyError:
               command_error()
               continue
