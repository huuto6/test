s = input()
s_rev = s[::-1]
while s_rev[0:1]:
    if s_rev.startswith("maerd"):
        s_rev = s_rev[5::1]
    elif s_rev.startswith("remaerd"):
        s_rev = s_rev[7::1]
    elif s_rev.startswith("esare"):
        s_rev = s_rev[5::1]
    elif s_rev.startswith("resare"):
        s_rev = s_rev[6::1]
    else:
        print("NO")
        break
if bool(s_rev[0:1]) == False:
    print("YES")
