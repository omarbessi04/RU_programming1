def decimal_to_binary(decimal):
    decimal = int(decimal)
    binary = ""
    if decimal > 0:
        while decimal > 0:
            if decimal % 2 == 0:
                binary += "0"
            else:
                binary += "1"
            decimal = decimal // 2
        return (binary[::-1])
    else:
        return "0"
