# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name("AnGEla", "YU"))

def is_leap_year(year):
    # Write your code here.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_leap_year(year):
    """Check a year either it is a leap year or not
    then return boolean"""
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


output = is_leap_year(1989)
print(output)