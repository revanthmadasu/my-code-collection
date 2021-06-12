# max difference between range of prime numbers
# question in techgig code gladiators
import math
def is_prime(num):
    if num == 2 or num == 3 or num == 5:
        # print(f'{num} is Prime')
        return True
    if num == 4:
        # print(f'{num} is Not Prime')
        return False
    num_sqrt = math.floor(math.sqrt(num))
    num_is_prime = True
    for i in range(2,num_sqrt+1):
        if num%i == 0:
            num_is_prime = False
            break
    # print(f"{num} is {'Prime' if num_is_prime else 'Not Prime'}")    
    return num_is_prime
def max_diff(l,r):
    l_prime = -1
    r_prime = -1
    l_curr = l
    while l_curr<=r:
        if is_prime(l_curr):
            l_prime = l_curr
            break
        l_curr += 1
    r_curr = r
    while r_curr > max(l,l_prime):
        if is_prime(r_curr):
            r_prime = r_curr
            break
        r_curr -= 1
    if r_prime == -1 and l_prime == -1:
        return -1
    elif r_prime == -1 or l_prime == -1:
        return 0
    else:
        return r_prime - l_prime

def main():
    inp_t = input()
    t = int(inp_t)
    # print(f't_input is {inp_t}')
    for t_i in range(t):
        raw_inp_range = input()
        # print(f'raw_inp_range is {raw_inp_range}')
        inp_range = list(
            map(int, raw_inp_range.split(' '))
        )
        l,r = inp_range[0], inp_range[1]
        print(max_diff(l,r))
        



main()

