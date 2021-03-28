#пункт А
lineNumeral='1 2 3 4 5 6'
print(lineNumeral[:4:1])
#пункт B
print(lineNumeral[::-1])
#пункт C
print(lineNumeral.replace(' ',','))
#пункт D
lineLetter='a b c d e f'
for i,j in zip(lineNumeral.replace(' ',''),lineLetter.replace(' ','')):
    print(i,j)

