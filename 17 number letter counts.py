digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

numstring = ""
for i in range(1, 1000):
    if i // 100:
        numstring += digits[i // 100] + " hundred"
        if i % 100:
            numstring += " and "
    if 10 < i % 100 < 20:
        numstring += teens[i % 100 - 10]
    else:
        numstring += tens[i % 100 // 10] + digits[i % 10]
numstring += "one thousand"

print(len(numstring.replace(" ", "")))