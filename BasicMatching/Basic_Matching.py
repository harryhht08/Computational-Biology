file = open('input', 'r')
lines = file.readlines()
key = lines[0].strip()
text = lines[1:]
for i in range(0, len(text)):
    text[i] = text[i].strip()
text = ''.join(text)
file.close()
pk = 0
output = []
for i in range(len(text) - len(key) + 1):
    if text[i] == key[pk]:
        j = i
        while pk < len(key) and text[j] == key[pk]:
            pk += 1
            j += 1
        if pk == len(key):
            output.append(i)
        pk = 0

# f = open('output', 'w')
# string = ' '.join(str(n) for n in output)
# f.write(string)
# f.close()
