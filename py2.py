n = int(input())
non_exponential = []
exponential = []
exponential1 = []
exponential2 = []
specials = [2,3,5,7]
a = []
b = []
interval = 2
while interval <= n:
    prime = True
    for i in range(2,int(interval**.5)+1):
        if interval % i == 0:
            prime = False
    if prime:
        a.append(interval)
    interval += 1
for d in a:
    if n%d == 0:
        b.append(d)

result = 1
for num in b:
    result *= num
remainder = n // result
if remainder == 1:
    power_ex = False
if remainder > 1:
    power_ex = True

result1 = 1
if power_ex == True:
    for num in b:
        if remainder % num == 0:
            exponential.append(num)
        if remainder % num != 0:
            non_exponential.append(num)
    for num in exponential:
        result1 *= num
    exponent = 0
    h = n
    while h >= result1 and h % result == 0:
        h = h // result1
        exponent += 1

    for num in non_exponential:
        if num in non_exponential:
            for bum in exponential:
                if bum in exponential:
                    if bum >= num:
                        for num in non_exponential:
                            if num in non_exponential:
                                separator = '*'
                                int_values = [str(item) for item in non_exponential if isinstance(item, int)]
                                print(separator.join(int_values) , end = ("*"))
                        for bum in exponential:
                            bum = f"{bum}^{exponent}"
                            exponential1.append(bum)
                        separator = '*'
                        print(separator.join(exponential1))

    for num in non_exponential:
        if num in non_exponential:
            for bum in exponential:
                if bum in exponential:
                    if num > bum and num in non_exponential:
                        for bum in exponential:
                            bum = f"{bum}^{exponent}"
                            exponential1.append(bum)
                        separator = '*'
                        print(separator.join(exponential1) , end = ("*"))
                        for num in non_exponential:
                            if num in non_exponential:
                                separator = '*'
                                int_values = [str(item) for item in non_exponential if isinstance(item, int)]
                                print(separator.join(int_values))

    if len(non_exponential) == 0:
        for num in exponential:
            num = f"{num}^{exponent}"
            exponential2.append(num)
            separator = '*'
        print(separator.join(exponential2))

if power_ex == False:
    separator = '*'
    int_values = [str(item) for item in b if isinstance(item, int)]
    print(separator.join(int_values))