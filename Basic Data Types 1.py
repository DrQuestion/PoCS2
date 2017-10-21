if __name__ == '__main__':
    N = int(raw_input()) #the first integer at the beginning of the input
    l=list() #list initialized
    for i in range(N): #all commands are considered
        cmd = raw_input().split() #the input is taken as string and splitted
        if cmd[0]!='print': #all other cmds are considered
            eval('l.'+cmd[0]+'('+','.join(cmd[1:])+')') #the string is re composed but now written as a true cmd, then the string l.cmd(a,b) is written (a or a and b can be missing), and executed with eval()
        else: print l #list is printed when requested