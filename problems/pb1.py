def replace_spaces(string, punctuationChar):
    string = string.replace(" ", punctuationChar)
    return string



# sentence = "Test  This is a test   Testing "
# sentence2 = replace_spaces(sentence, "_")
# print(sentence2) # -> Test__This_is_a_test__Testing_