def incomodam(n):
    if n < 1:
        return ""
    else:
        return "incomodam " + incomodam(n - 1)

def elefantes(n, e = 1):
    if n < 1:
        return ""
    else:
        if n > 1:
            if e == 1:
                return "Um elefante incomoda muita gente\n" + elefantes(n - 1, e + 1)
            else:
                return str(e) + " elefantes " + incomodam(e) + "muito mais\n" + str(e) + " elefantes incomodam muita gente\n"  + elefantes(n - 1, e + 1)
        else:
            return str(e) + " elefantes " + incomodam(e) + "muito mais" + elefantes(n - 1, e + 1)

print(elefantes(8))

    