#Input : a4k3b2
#Output : aeknbd
#In this program, we need to use the following two functions:

#ord(): To find unicode value for the given character

#Example: print(ord('a'))

#Output: 97

#chr(): To find corresponding character for the given unicode value

#Example: print(chr(97))




s='a4k3b2'
output=''
for i in s:
    if i.isalpha()== True:
            x=i
            output+=i
    else:
        d=int(i)
        new_chr= chr(ord(x)+d)
        output =output + new_chr
print(output)

