def prettyPrintList(list):
    result = ""
    if len(list) == 1:
        result = list[0]
    elif len(list) == 2:
      result = list[0] + " and " + list[1]
    elif len(list) > 2:
        i = 0
        for item in list:
            if (i < len(list)-1):
                result += list[i] + ", "
                i = i + 1
        result = result + "and " + list[len(list) - 1]

    return result


spam = ['apples', 'bananas']
print prettyPrintList(spam)

