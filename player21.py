pts1=input().split()
pts2=input().split()
pts3=input().split()
if(pts1[0]==pts2[0]==pts3[0] or pts1[1]==pts2[1]==pts3[1] or (pts1[0]==pts1[1] and pts2[0]==pts2[1] and pts3[0]==pts3[1])):
    print('yes')
else:
    print('no')
