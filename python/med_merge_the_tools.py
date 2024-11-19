def merge_the_tools(string, k):
    #k is substrings
    #split string in k substrings
    
    for i in range(0, len(string), k):
        string_breakdown = string[i:i+k]

        final_string = ""
        for i in range(0, len(string_breakdown)):
            if string_breakdown[i] not in final_string:
                final_string += string_breakdown[i]
        print(final_string)



