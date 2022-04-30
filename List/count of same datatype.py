def checktype(array):
        for ele in array:
            if isinstance(ele, int):
                print(ele,"is an integer\n")
                # integer = integer + 1
            elif isinstance(ele, str):
                print(ele, "is an string\n")
                # string = string + 1
            elif isinstance(ele, float):
                print(ele, "is an float\n")
                # floating = floating + 1
        # print(
        #     "\nNumber of integer: ", integer,
        #     "\nNumber of string: ", string,
        #     "\nNumber of floating: ", floating)

list = ["a",3,33.66,"hello",22,99]
# list.count(isinstance(list,int))
checktype(list)
