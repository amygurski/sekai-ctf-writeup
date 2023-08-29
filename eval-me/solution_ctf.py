import json
from pwn import *

conn = remote('chals.sekai.team',9000)

i = 0

while i < 100:

    input = str(conn.recv())
    print(i)
    print(input)

    # regex to extract equation from input, e.g. 10 / 10 or 1 * 4
    equation = re.findall('[\d]+ [\/\+\-\*] [\d]+', input)[0]

    split_num_sym = re.findall('(\d+|[^ 0-9])', equation)

    operator = split_num_sym[1]
    first_operand = int(split_num_sym[0])
    second_operand = int(split_num_sym[2])

    if operator == '+':
        result = first_operand + second_operand
    elif operator == '-':
        result = first_operand - second_operand
    elif operator == '*':
        result = first_operand * second_operand
    else:
        result = first_operand / second_operand

    conn.sendline(str(result).encode())

    i+=1


response = conn.recv()
print(response)

conn.close()
