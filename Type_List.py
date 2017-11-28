# test = ["hi",19,'hello',98.98,'world',9]
# sum = 0
# string = ""
# output_type = ""
# for i in test:
#     if isinstance(i, int):
#         sum = sum + i
#         print "The list you entered is of integer type"
#         print "Sum: ", sum
#         if isinstance(i, str):
#             output_type = 'mixed'
#         else:
#             output_type = 'number'
#     elif isinstance(i, str):
#         # print "The list you entered is of string type"
#         string = string + i
#         if isinstance(i, int):
#             output_type = 'mixed'
#         else:
#             output_type = 'str'
# print sum
# print string
# print output_type

mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff", "Moon", "Robot"]
def identify_list_type(lst):
    new_string = ''
    sum = 0

    for value in lst:
        if isinstance(value, int):
            sum += value
        elif isinstance(value, str):
            new_string += value

    if new_string and sum:
        print "The list you entered is of mixed type"
        print "String: ", new_string
        print "Sum: ", sum
    elif new_string:
        print "The list you entered is of string type"
        print "String: ", new_string
    else:
        print "The list you entered is of integer type"
        print "Sum: ", sum
        
print identify_list_type(mixed_list)
print identify_list_type(integer_list)
print identify_list_type(string_list)