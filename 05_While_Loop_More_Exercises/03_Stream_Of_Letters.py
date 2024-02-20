command = input()
c_counter = 0
o_counter = 0
n_counter = 0
current_symbol = 0
word = ""
while command != "End":
    is_special = False
    current_symbol = ord(command)
    if 0 <= current_symbol <= 64 or 91 <= current_symbol < 97 or current_symbol > 122:
        command = input()
        continue
    if 97 <= current_symbol <= 122 or 65 <= current_symbol <= 90:
        if current_symbol == 99:
            c_counter += 1
            is_special = True
        elif current_symbol == 110:
            n_counter += 1
            is_special = True
        elif current_symbol == 111:
            o_counter += 1
            is_special = True
    if c_counter == 2:
        c_counter -= 1
        word += str(chr(current_symbol))
    if n_counter == 2:
        n_counter -= 1
        word += str(chr(current_symbol))
    if o_counter == 2:
        o_counter -= 1
        word += str(chr(current_symbol))
    if not is_special:
        word += str(chr(current_symbol))
        # print(f'{chr(current_symbol)}', end="")
    if c_counter > 0 and o_counter > 0 and n_counter > 0:
        print(f'{word}', end=" ")
        c_counter = 0
        o_counter = 0
        n_counter = 0
        word = ""
        command = input()
        continue
    command = input()
