regs = {
     'R0':'000',
     'R1':'001',
     'R2':'010',
     'R3':'011',
     'R4':'100',
     'R5':'101',
     'R6':'110',
     'FLAGS':'111'
     }
     
opcodeTable={   "var": "",
                "add": "0000000",
                "sub": "0000100",
                "mov": ["000100", "0001100000"], 
                "ld" : "001000",
                "st" : "001010",
                "mul": "0011000",
                "div": "0011100000",
                "rs" : "010000",
                "ls" : "010010",
                "xor": "0101000",
                "or" : "0101100",
                "and": "0110000",
                "not": "0110100000",
                "cmp": "0111000000",
                "jmp": "011110000",
                "jlt": "111000000",
                "jgt": "111010000",
                "je" : "111110000",
                "hlt": "1101000000000000"
}

def dec_to_bin(n):
    i = 0
    num = 0
    while n != 0:
        num += (n % 2) * (10 ** i)
        n = n // 2
        i += 1
    n_num = str(num).zfill(8)
    return n_num


Out = []
out_index = 0
Var_count = 0
Errors = 0
Source = []
for line in sys.stdin:
    Source.append(line)

for i in range(len(Source)):
    linenum = i+1
    labels = []
    
    curr = Source[i].split()
    if curr[0][::-1] == ":":
        label , rest = curr.split(:)
        labels.append(label)
        
        newcurr = rest.split()
        
        
        if newcurr[0] in opcodeTable.keys() :
            if newcurr[0] in ["add", "sub", "mul", "xor", "or", "and"]:
                if length(newcurr) != 3:
                    Errors += 1
                elif newcurr[1] not in regs.keys() or newcurr[2] not in regs.keys() or newcurr[3] not in regs.keys():
                    Errors += 1
                else : 
                    Out.append(opcodeTable[newcurr[0]]+regs[newcurr[1]]+regs[newcurr[2]]+regs[newcurr[2]])
                out_index += 1
                i += 1
            
            elif newcurr[0] == "mov":
                tempval = 0
                if newcurr[2][0] == "$":
                    opcodeTable[newcur[0][0]] = tempval
                    if len(newcurr) != 2:
                        Errors += 1
                    else:
                        Out.append(tempval + regs[newcurr[1]] + dec_to_bin(int(newcurr[2][1:])))
                    out_index+=1
                    i += 1
                else :
                    opcodeTable[newcur[0][1]] = tempval
                    if len(newcurr) != 2:
                        Errors += 1
                    else:
                        Out.append(tempval + regs[newcurr[1]] + regs[newcurr[2]])
                    out_index+=1
                    i += 1
            
            elif newcurr[0] in ["rs", "ls"]:
                if len(newcurr) != 3:
                    Errors += 1
                else :
                    Out.append(opcodeTable[newcurr[0]] + regs[newcurr[1]] + regs[newcurr[2]])
                out_index += 1
                i += 1
            
            elif newcurr[0] in ["div", "not", "cmp"]:
                if len(newcurr) != 3 :
                    Errors += 1 
                else :
                    Out.append(opcodeTable[newcurr[0]] + regs[newcurr[1]] + regs[newcurr[2]])
                out_index += 1 
                i += 1
                    
            elif newcurr[0] in ["ld", "st"]:
                if len(newcurr) != 3 :
                    Errors += 1
                elif newcurr[2][0] != "$" :
                    Errors += 1
                else :
                    Out.append(opcodeTable[newcurr[0]] + regs[newcurr[1]] + dec_to_bin(int(newcurr[2][1:])))
                out_index += 1
                i += 1
            
            elif newcurr[0] in ["jmp", "jlt", "jgt", "je"]:
                if len(newcurr) != 2:
                    Error += 1
                elif newcurr[1][0] != "$":
                    Error += 1
                else :
                   Out.append(opcodeTable[newcurr[0]] + dec_to_bin(int(newcurr[1][1:])))
                out_index += 1
                i += 1
        
    elif curr[0] in opcodeTable.keys():
        if curr[0] in ["add", "sub", "mul", "xor", "or", "and"]:
            if len(curr) != 3:
                Errors += 1
            elif curr[1] not in regs.keys() or curr[2] not in regs.keys():
                Errors += 1
            else:
                Out.append(opcodeTable[curr[0]] + regs[curr[1]] + regs[curr[2]] + regs[curr[2]])
            out_index += 1
            i += 1

        elif curr[0] == "mov":
            tempval = 0
            if curr[2][0] == "$":
                opcodeTable[curr[0][0]] = tempval
                if len(curr) != 3:
                    Errors += 1
                else:
                    Out.append(tempval + regs[curr[1]] + dec_to_bin(int(curr[2][1:])))
                out_index += 1
                i += 1
            else:
                opcodeTable[curr[0][1]] = tempval
                if len(curr) != 3:
                    Errors += 1
                else:
                    Out.append(tempval + regs[curr[1]] + regs[curr[2]])
                out_index += 1
                i += 1

        elif curr[0] in ["rs", "ls"]:
            if len(curr) != 3:
                Errors += 1
            else:
                Out.append(opcodeTable[curr[0]] + regs[curr[1]] + regs[curr[2]])
            out_index += 1
            i += 1

        elif curr[0] in ["div", "not", "cmp"]:
            if len(curr) != 3:
                Errors += 1
            else:
                Out.append(opcodeTable[curr[0]] + regs[curr[1]] + regs[curr[2]])
            out_index += 1
            i += 1
                
        elif curr[0] in ["ld", "st"]:
            if len(curr) != 3:
                Errors += 1
            elif curr[2][0] != "$":
                Errors += 1
            else:
                Out.append(opcodeTable[curr[0]] + regs[curr[1]] + dec_to_bin(int(curr[2][1:])))
            out_index += 1
            i += 1

        elif curr[0] in ["jmp", "jlt", "jgt", "je"]:
            if len(curr) != 2:
                Errors += 1
            elif curr[1][0] != "$":
                Errors += 1
            else:
                Out.append(opcodeTable[curr[0]] + dec_to_bin(int(curr[1][1:])))
            out_index += 1
            i += 1

        elif curr[0] == "var":
            Var_count += 1
            out_index += 1
            i += 1

        elif curr[0] == "hlt":
            if len(curr) != 1:
                Errors += 1
            else:
                Out.append(opcodeTable[curr[0]])
            break


        

   
   
   
   
   
   
        

        

   
   
   
   
   
   
        
