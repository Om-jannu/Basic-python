def checktype(array):
        for ele in array:
            if isinstance(ele, int):
                print(ele,"is an integer\n")
            elif isinstance(ele, str):
                print(ele, "is an string\n")
            elif isinstance(ele, float):
                print(ele, "is an float\n")
list = ["a",3,33.66,"hello",22,99]
checktype(list)
