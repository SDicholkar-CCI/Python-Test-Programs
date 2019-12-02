import language_check
tool = language_check.LanguageTool('en-US')

file = open("D:/Swapnil Data/spellAndGrammerCheck.txt", "r")
sentence = file.read()
str1 = sentence.split('\n')
str2 = ''.join([i if i.endswith('.') else i+'. ' for i in str1])
matches = tool.check(str2)
for m in matches:
    print(m)
print(len(matches))
data = language_check.correct(str2, matches)
print(data)

