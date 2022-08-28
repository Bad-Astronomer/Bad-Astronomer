def binary_to_decimal_mag(num):
    decimal = 0
    for i, n in enumerate(num):
        decimal += (2**(len(num)-i-1))*n
    return decimal

def binary_to_decimal(num):
    decimal= 0
    if len(num) == size and num[0] == 1:
        num = twos_complement(num)
        decimal = binary_to_decimal_mag(num)* -1
    else:
        decimal = binary_to_decimal_mag(num)
    return decimal

def decimal_to_binary_mag(num):
    global binary
    binary = []
    if num > 1:
        decimal_to_binary_mag(num//2)
    binary.append(num%2)
    return binary

def decimal_to_binary(num):
    if num < 0:
        num *= -1
        binary = decimal_to_binary_mag(num)
        binary = normalize(binary, size)
        binary = twos_complement(binary)
    else:
        binary = decimal_to_binary_mag(num)
        binary = normalize(binary, size)
    return binary

def normalize(num, size):
    while len(num) < size:
        num.insert(0, 0)
    return num

def twos_complement(num):
    var = num[1:]
    if binary_to_decimal(var) == 0:
        var = [0 for i in range(size)]
        return var
    if num[0] == 1:
        var = binary_to_decimal(invert(var))
        var = decimal_to_binary(var+1)
        del(var[0])
        var.insert(0,0)
    else:
        var = binary_to_decimal(var)
        var = decimal_to_binary(var-1)
        del(var[0])
        var = invert(var)
        var.insert(0,1)
    return var

def invert(num):
    var = []
    for i in num:
        if i == 1:
            i = 0
        else:
            i = 1
        var.append(i)
    return var

def mod(num):
    if num < 0:
        num *= -1
    return num

def binary_add(num1, num2):
    ans, run = [0 for i in range(size)], True
    for i in range(size):
        ans[i] += num1[i] + num2[i]
    while run:
        run = False
        for i, n in enumerate(ans):
            if n > 1:
                ans[i] = 0
                if i > 0:
                    ans[i-1] += 1
                run = True
    return ans


decimal_num = [5,-6]
while True:
        try:
            decimal_num[0] = int(input("Enter an integer number: "))
            decimal_num[1] = int(input("Enter another integer number: "))
            break
        except ValueError:
            print("Invalid Input")

print(f"Decimal Input: {decimal_num}")

binary_num = [0, 0]
complement_num = [0, 0]
size = 0

for j in range(2):
    i = 0
    while mod(decimal_num[j]) >= 2**i:
                i += 1
    size += i
if size < 2:
    size = 2

for i, num in enumerate(decimal_num):
    binary_num[i] = decimal_to_binary(num)
    complement_num[i] = twos_complement(binary_num[i])

print(f"Binary input: {binary_num}\n\n")

global booth_bit
booth_bit = 0
initial = [0 for i in range(size)]

for i in range(size):
    lsd = binary_num[1][-1]
    print(f"Step {i}: {initial} {binary_num[1]} {booth_bit}")

    if lsd + booth_bit != 1:
        print("No Op")
        pass
    if lsd == 0 and booth_bit == 1:
        print("01 : Binary Add")
        initial = binary_add(initial, binary_num[0])
    if lsd == 1 and booth_bit == 0:
        print("10: Binary Subtract")
        initial = binary_add(initial, complement_num[0])

    #right shift start
    booth_bit = lsd
    binary_num[1].insert(0,initial[-1])
    del(initial[-1])
    initial.insert(0,initial[0])
    del(binary_num[1][-1])
    lsd = binary_num[1][-1]
    #right shift end
    print("Right Shift\n"+"-"*100)

binary_ans = []
binary_ans.extend(initial)
binary_ans.extend(binary_num[1])
size = len(binary_ans)
decimal_ans = binary_to_decimal(binary_ans)

print(f"\nBinary Output: {binary_ans}")
print(f"Decimal Output: {decimal_ans}")
