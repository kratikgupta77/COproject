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
def dec_to_bin(n):
    i=0
    num=0
    while(n!=0):
        num+=(n%2)(10*i)
        n=n//2
        i+=1
    n_num=str(num).zfill(8)
    return n_num
number = 1

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
labels = {}
encounteredErrors = []

for i, line in enumerate(assemblyCode, 1):
    if not line:
        continue

    if ':' in line:
        label, rest_of_line = line.split(':', maxsplit=1)
        if label in labels:
            encounteredErrors.append(f"ERROR at Line {i + varLines}: Multiple declarations for the same label found")
            continue
        else:
            labels[label] = binary8bit(i-1)
            line = rest_of_line.strip()

    currentLine = line.split()
    # process the rest of the line here
