print ("Test ")
s = input("Input: ")
s = s.strip()
s = s.upper()


num = 0
con = 0
for i in range(len(s)):
    if con == 1:
        con = 0
        continue
    if s[i] == "A":
        if i+1 < len(s):
            if s[i+1] == "B":
                num += 4
                con += 1
            elif s[i+1] == "Z":
                num += 9
                con += 1
            else:
                num += 1
        else:
            num += 1
    elif s[i] == "B":
        num += 5
    elif s[i] == "Z":
        if i+1 < len(s):
            if s[i+1] == "L":
                num += 40
                con += 1
            elif s[i+1] == "C":
                num += 90
                con += 1
            else:
                num += 10
        else:
            num += 10
    elif s[i] == "L":    
        num += 50 
    elif s[i] == "C":
        if i+1 < len(s):
            if s[i+1] == "D":
                num += 400
                con += 1
            elif s[i+1] == "R":
                num += 900
                con += 1
            else:
                num += 100     
        else:
            num += 100
    elif s[i] == "D":
        num += 500     
    elif s[i] == "R":
        num += 1000     


print("Output: ",num)
