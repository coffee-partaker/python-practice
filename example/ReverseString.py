def reverseString(str):
    reversed = ''
    for char in str[::-1]:
        reversed += char
    return reversed

temp = "it's jojover"
print(reverseString(temp))