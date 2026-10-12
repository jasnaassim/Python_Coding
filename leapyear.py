#Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.
def leapyear(year):
    years = []
    cnt = 1
    while cnt <= 15:
        if year % 4 == 0 :
            years.append(year)
            cnt += 1
        year += 1
    return years

print(leapyear(1999))

