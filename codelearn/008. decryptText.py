def decryptText(s):
    st=""
    t=s1=0
    for i in range(len(s)):
        s1=((ord(s[i])-97)-t)%26
        st+=chr(s1+97)
        t += (ord(st[i]) - 97)
        print(s1, st, t)

decryptText('cqtximmdq')