import argparse
import csv

# parser = argparse.ArgumentParser()
# parser.add_argument('--a', type=int, required=True)
# parser.add_argument('--b', type=int, required=True)
# parser.add_argument('--op', type=str)
# args = parser.parse_args()

# 1

# sum = args.a + args.b
# diff = args.a - args.b
# mult = args.a * args.b
# div = args.a / args.b
# mean = (args.a + args.b)/2
#
# print(f'Sum: {sum} \n'
#       f'Difference: {diff} \n'
#       f'Multiplication: {mult} \n'
#       f'Division: {div} \n'
#       f'Mean: {mean} \n')

# 2

# if args.op == '+':
#       print(f'The result of your operation: {sum}')
# elif args.op == '-':
#       print(f'The result of your operation: {diff}')
# elif args.op == '*':
#       print(f'The result of your operation: {mult}')
# elif args.op == '/':
#       print(f'The result of your operation: {div}')
# elif args.op == 'avg':
#       print(f'The result of your operation: {mean}')
# else:
#       print("Input a proper operation")

# 3

html = ''
html += '<html>\n<body>\n'
names = []
emails = []
ages = []
with open('Lab7.csv', 'r') as data:
    dataCSV = csv.DictReader(data)

    for line in dataCSV:
      names.append(f"{line['FirstName']} {line['LastName']}")
      emails.append(f"{line['Email']}")
      ages.append(f"{line['Age']}")

html += '<ul>\n'

for n in names:
      html += f"<li>{n}</li>\n"
html += '</ul>\n'

html += '<ol>\n'

for e in emails:
      html += f"<li>{e}</li>\n"

html += '</ol>\n'

html += '<table>\n<tr>\n<th>Name</th>\n<th>Age</th>\n</tr>\n'

for i in range(len(names)):
    html+= f"<tr>\n<td>{names[i]}</td>\n<td>{ages[i]}</tr>\n"

html += '</table>\n'



html += '<style>\nul{\nbackground-color: green;\ncolor: blue;\n}\nol{\nbackground-color:red;\ncolor: blue;\n}\n</style>\n'
html += '</body>\n</html>'

f = open('HW7.html', 'w')
for line in html:
      f.write(line)
