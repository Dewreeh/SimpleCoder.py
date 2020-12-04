def encoderdecoder():
    def encoder():
        print("Enter the string ==>")
        string = list(input())
        print("Enter the code==>    // That code have influence on how your string will be encoded")
        Code = int(input())
        for Symbols in range(0, len(string)):
            string[Symbols] = chr(ord(string[Symbols]) + Code)
        print("That is your string:", "".join(string))
        print("=============================")
        encoderdecoder()

    def decoder():
        print("Enter the string ==>")
        string = list(input())
        print("Enter the code==>    // That code have influence on how your string will be decoded")
        Code = int(input())
        for Symbols in range(0, len(string)):
            string[Symbols] = chr(ord(string[Symbols]) - Code)
        print("That is your string:", "".join(string))
        print("===========================")
        encoderdecoder()

    print("1) Code string")
    print("2) Decode string")
    Choose = int(input())
    if Choose == 1:
        encoder()
    elif Choose == 2:
        decoder()


encoderdecoder()
