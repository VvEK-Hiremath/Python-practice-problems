lt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

dct_s = {}
dct_r = {}

val = 0
val1 = -26
for i in range(0,len(lt)):
    dct_s[lt[i]] = val
    dct_r[lt[i]] = val1
    val1 += 1
    val += 1

print(dct_s,end = "\n\n")
print(dct_r,end = "\n\n")

inp_s = str(input("enter alphabet series: "))
        

def func(s):
    ans = 0
    curr = 'a'
    for i in range(0,len(s)):
        if(dct_s[s[i]] >= dct_s[curr]):
            a_s = dct_s[curr] - dct_r[s[i]]
            a_l = dct_s[s[i]] - dct_s[curr]
        else:
            a_s = dct_s[s[i]] - dct_r[curr]
            a_l = dct_s[curr] - dct_s[s[i]] 
        ans += min(a_s,a_l)
        curr = s[i]
    return ans

def is_valid(inp_s):
    for i in inp_s:
        if(i.isalpha()):
            continue
        else:
            return False
    return True

if(is_valid(inp_s)):
    print(func(inp_s))
else:
    print("invalid character in string input enter only(a to z)")
