import sys

def dec_to_bin(dec):
   
def opcode(instruction):

def instrct_type():

def registerAddress(register):

assemblyCode = []
for line in sys.stdin:
    assemblyCode.append(line)

convertedBinary = []  
encounteredErrors = [] 
labels = {}
encounteredErrors = []
variables = {}
lineNumber = 0
varLines = 0

for _ in range(varLines):
    if not assemblyCode[0]:
        number += 1
        continue

    line = assemblyCode[0].split()
    number = 1
    if line[0] == "var" and len(line) == 2:
        if line[1] not in variables.keys():
            variables[line[1]] = dec_to_bin()
            assemblyCode.pop(0)
            varLines+= 1
            number += 1
            continue
        else:
            number += 1
            varLines += 1
            continue
    elif line[0] == "var":
        assemblyCode.pop(0)
        number += 1
        varLines += 1
        continue
    else:
        break


for i, line in enumerate(assemblyCode, 1):
    if not line:
        continue

    if ':' in line:
        label, rest_of_line = line.split(':', maxsplit=1)
        if label in labels:
            encounteredErrors.append(f"ERROR at Line {i + varLines}: Multiple declarations for the same label found")
            continue
        else:
            labels[label] = dec_to_bin(i-1)
            line = rest_of_line.strip()

    currentLine = line.split()

if currentLine[0] == "mov":
    if len(currentLine) == 3:
        reg1 = registerAddress(currentLine[1])
        reg2 = registerAddress(currentLine[2])
        if reg1 != -1 and reg2 != -1:
            if reg1 == "111":
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Wrong FLAGS")
               
            convertedBinary.append(opcode(currentLine[0], 1) + "00000" + reg1 + reg2)
           
        elif currentLine[2][1:].isdecimal():
            if currentLine[2][0] != "$":
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Syntax Error")
                
            if reg1 == -1:
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Invalid Reg")
               
            if reg1 == "111":
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Wrong FLAGS")
                
            imm_value = int(currentLine[2][1:])
            if imm_value < 0 or imm_value > 255:
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Illegal Immediate Value")
             
            convertedBinary.append(opcode(currentLine[0], 0) + reg1 + dec_to_bin(imm_value))
          
    encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Wrong Syntax used for instruction")
    


if instrct_type(currentLine[0]) == 'a':
    if len(currentLine) == 4:
        reg1 = registerAddress(currentLine[1])
        reg2 = registerAddress(currentLine[2])
        reg3 = registerAddress(currentLine[3])
        if reg1 == -1 or reg2 == -1 or reg3 == -1:
            encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Invalid Register")
        if reg1 == "111" or reg2 == "111" or reg3 == "111":
            encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Illegal use of FLAGS")
        convertedBinary.append(opcode(currentLine[0]) + "00" + reg1 + reg2 + reg3)
        
    encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Wrong Syntax used for instruction")
    


if instrct_type(currentLine[0]) == 'b':
    if len(currentLine) == 3:
        immediate_value = int(currentLine[2][1:]) if currentLine[2][0] == "$" else None
        if immediate_value is None:
            encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Syntax Error")
            
        if immediate_value not in range(0, 256):
            encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Illegal Immediate Value")
            
        reg = registerAddress(currentLine[1])
        if reg == -1:
            encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Invalid Register")
            
        if reg == "111":
            encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Illegal use of FLAGS")
            
        convertedBinary.append(opcode(currentLine[0]) + reg + dec_to_bin(immediate_value))
        
    encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Wrong Syntax used for instruction")
    


if instrct_type(currentLine[0]) == 'c':
    if len(currentLine) == 3:
        reg1 = registerAddress(currentLine[1])
        reg2 = registerAddress(currentLine[2])
        if all(reg == -1 for reg in (reg1, reg2)):
            encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Invalid Register")
            
        if any(reg == "111" for reg in (reg1, reg2)):
            encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Illegal use of FLAGS")
            
        convertedBinary.append(opcode(currentLine[0]) + "00000" + reg1 + reg2)
        
    encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Wrong Syntax used for instruction")
    

if instrct_type(currentLine[0]) == 'd':
    if len(currentLine) == 3:
        reg = registerAddress(currentLine[1])
        if reg == -1:
            encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Invalid Register")
           
        if reg == "111":
            encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Illegal use of FLAGS")
           
        variable = variables.get(currentLine[2])
        if variable is None:
            if currentLine[2] in labels.keys():
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Misuse of label as variable")
            else:
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Use of undefined variable")
           
        convertedBinary.append(opcode(currentLine[0]) + reg + variable)
       
    encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Wrong Syntax used for instruction")
   


if instrct_type(currentLine[0]) == 'e':
    if len(currentLine) == 2:
        ins = currentLine.pop(0)
        label = currentLine[0]
        if label not in labels.keys():
            if label in variables.keys():
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Misuse of variable as label")
            else:
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Use of undefined labels")
            
        else:
            convertedBinary.append(opcode(ins) + '0' * 3 + labels[label])
            
    encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Wrong Syntax used for instruction")
    


if instrct_type(currentLine[0]) == 'f':
    if len(currentLine) == 1:
        convertedBinary.append(opcode(currentLine[0]) + '0' * 11)
        HltCalled = True
        
    encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Wrong Syntax used for instruction")
    


if not HltCalled:
    encounteredErrors.append("ERROR: No halt (hlt) instruction found")

if len(convertedBinary) > 256:
    print("ERROR: The code length exceeds the maximum capacity (256 lines)")
else:
    if encounteredErrors:
        for error in encounteredErrors:
            print(error)
    else:
        output = '\n'.join(convertedBinary)
        print(output)

