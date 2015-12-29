import pyperclip
import re

text = pyperclip.paste()

matches = []

emailRegex = re.compile(r'''(
    [a-zA-Z0-9.%+-]+                     # username
    @                                    # @ symbol
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z0-9]{2,4})
    )''', re.VERBOSE)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                   # area code
    ([-\s\.]{,1})                        # separator
    (\d{3})                              # first three digits
    ([-\s\.])?                           # separator
    (\d{4})                              # last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?       # extension
    )''', re.VERBOSE)
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if (groups[8] != ''):
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print '\n'.join(matches)
else:
    print 'No emails or phone numbers found.'
