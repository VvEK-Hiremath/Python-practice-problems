s = input("Enter Navigation(U,D,L,R): ")

s = s.upper()

def is_Origin(s):
    track = [0,0]
    for i in range(0,len(s)):
        if(s[i] == 'U'):
            track[1] += 1 
        elif(s[i] == 'D'):
            track[1] -= 1
        elif(s[i] == 'L'):
            track[0] -= 1
        else:
            track[0] +=1
    if(track.count(0) == 2):
        return True
    else:
        return False

print(is_Origin(s))
    