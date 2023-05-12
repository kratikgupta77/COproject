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
                    "hlt": "11010",
                    "addf": "10000",
                    "subf": "10001"
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
