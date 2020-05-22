
from commands_mapper import commands
from cmd_func import pwd,command_error
import os
import gc



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
            cmd = user_cmd.split(' ')
            cmd_func = commands[cmd[0]]
            cmd_args= [None,None,None]
            cmd.remove(cmd[0])
            for i ,arg in enumerate(cmd):
                cmd_args[i] = arg


            result = cmd_func(cmd_args)
            if result.err:
                print(result.err)
                continue
            if  result.content:
                for line in result.content:
                    print(line)

            continue
        
        except KeyError:
            command_error()

