def string_splosion(strParam):
    result = ""
    for i in range(len(strParam)):
        result += strParam[:i + 1]
    return result
