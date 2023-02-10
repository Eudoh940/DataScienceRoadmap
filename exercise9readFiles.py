import re
from collections import Counter
# f = open ("c:\\data\\poem.txt", "r")
# print(f.read())
# f.close()
words = Counter(re.findall("\w+", open('c:\\data\\poem.txt').read().lower()))
print(words.most_common(3))


with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
    header = "Company Name,PE Ratio, PB Ratio\n"
    out.write(header)
    next(f)  # This will skip the first line in the file, which is a header

    for line in f:
        tokens = line.split("\t")
        company_name = tokens[0]
        price = float(tokens[1])
        earnings_per_share = float(tokens[2])
        book_value = float(tokens[3])

        pe_ratio = round(price / earnings_per_share, 2)
        pb_ratio = round(price / book_value, 2)

        output = f"{company_name},{pe_ratio},{pb_ratio}\n"
        out.write(output)