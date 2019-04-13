#sを昇順、tを降順で並び替え
s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)

#1文字目から文字列比較
#sが早い or sが文字無tが文字有の場合終了、判定Yes
#同じ場合次の文字判定へ
#sが遅い or sが文字有tが文字無 or s,t共に文字無の場合終了、判定No
for i in range(100):
    print(s[i:i+1])
    print(t[i:i+1])
    if bool(s[i:i+1]) == False:
        if t[i:i+1]:
            print("Yes")
            break
        else:
            print("No")
            break
    elif bool(t[i:i+1]) == False:
        print("No")
        break
    elif (s[i] < t[i]):
        print("Yes")
        break
    elif (s[i] > t[i]):
        print("No")
        break