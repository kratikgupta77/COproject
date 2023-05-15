import sys

opcodeTable={      "add": "00000",
                    "sub": "00001",
                    "mov": ["00010", "00011"], 
                    "ld" : "00100",
                    "st" : "00101",
                    "mul": "00110",
                    "div": "00111",
                    "rs" : "01000",
                    "ls" : "01001",
                    "xor": "01010",
                    "or" : "01011",
                    "and": "01100",
                    "not": "01101",
                    "cmp": "01110",
                    "jmp": "01111",
                    "jlt": "11100",
                    "jgt": "11101",
                    "je" : "11111",
                    "hlt": "11010"
		}

def dec_to_bin(dec):
   
def opcode(instruction):

def instrct_type():

def registerAddress(register):

varLines = 0
assemblyCode = []
for line in sys.stdin:
    assemblyCode.append(line)

convertedBinary = []
encounteredErrors = []
labels = {}
variables = {}
lineNumber = 0
haltEncountered = False

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
            number += 1
            continue
        else:
            number += 1
            continue
    elif line[0] == "var":
        assemblyCode.pop(0)
        number += 1
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
            labels[label] = dec_to_bin(i - 1)
            line = rest_of_line.strip()

    currentLine = line.split()

if currentLine[0] == "mov":
    if len(currentLine) == 3:
        reg1 = registerAddress(currentLine[1])
        reg2 = registerAddress(currentLine[2])
        if reg1 != -1 and reg2 != -1:
            if reg1 == "111":
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Illegal use of FLAGS")
                continue
            convertedBinary.append(opcode(currentLine[0], 1) + "00000" + reg1 + reg2)
            continue
        elif currentLine[2][1:].isdecimal():
            if currentLine[2][0] != "$":
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Syntax Error")
                continue
            if reg1 == -1:
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Invalid Register")
                continue
            if reg1 == "111":
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Illegal use of FLAGS")
                continue
            imm_value = int(currentLine[2][1:])
            if imm_value < 0 or imm_value > 255:
                encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Illegal Immediate Value")
                continue
            convertedBinary.append(opcode(currentLine[0], 0) + reg1 + binary8bit(imm_value))
            continue
    encounteredErrors.append("ERROR at Line " + str(lineNumber + varLines + 1) + ": Wrong Syntax used for instruction")
    continue

