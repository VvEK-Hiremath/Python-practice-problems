def timeConversion(s):
    # Write your code here
    if(s[8:] == 'AM'):
        if(s[0:2] == '12'):
            ans = '00'
            return ans + s[2:8]
        return s[0:8]        
    if(s[8:] == 'PM'):
        if(s[0:2] == '12'):
            return s[0:8]
        else:
            a = int(s[0:2])
            a = str(a+12)
            return a + s[2:8]
        
print(timeConversion('01:01:02PM'))