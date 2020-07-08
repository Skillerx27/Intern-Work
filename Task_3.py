def fun(s1,s2):
    s = ''
    cnt = int(0)
    s1 += " "
    for idx,i in enumerate(s1,start=0):
        if i == ' ':

            if s == s2:
                cnt += 1
                s = ''
            elif len(s)>len(s2):
                cks = ''
                x = int(0)
                for idx,val in enumerate(s,start=0):
                    if cks == s2 :
                        
                        cnt += 1
                        x = 0
                        cks = ''
                    if s[idx]==s2[x]:
                        cks += s2[x]
                        x += 1
                        if len(s)-1==idx:
                            if cks == s2:
                                cnt += 1
                                continue
                    else:
                        x = 0
                        cks = ''
                s = ''
            else:
                s = ''
        else:
            s += i

    return cnt


x = input()
x1 = input()

print(fun(x,x1))