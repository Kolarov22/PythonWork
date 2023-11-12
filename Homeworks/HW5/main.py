import re
import pandas as pd

with open('HW5Ex1.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

#a)

# link_pattern = r'<a[^>]*\s*href=["\'](https?://[^"\']+)"'
# links = re.findall(link_pattern, html_content)
#
#
# for link in links:
#     print(link)

#b)
#
# label_pattern = r'<label[^>]*>(.*?)<\/label>'
# form_labels = re.findall(label_pattern, html_content)
#
#
# for label in form_labels:
#     print(label.strip())

#c)

# input_type_pattern = r'<input[^>]*\s+type=["\'](.*?)["\']'
#
# input_types = re.findall(input_type_pattern, html_content)
#
# for input_type in input_types:
#     print(input_type)

#d)

# option_value_pattern = r'<option[^>]*>(.*?)<\/option>'
#

# option_values = re.findall(option_value_pattern, html_content, re.DOTALL)
#

# for option_value in option_values:
#     print(option_value.strip())

#e)
# form_pattern = r'<form[^>]*>.*?</form>'
#
# # Find all form elements using the regular expression pattern
# form_elements = re.findall(form_pattern, html_content, re.DOTALL)
#
# # Define a regular expression pattern to match id attributes
# id_attribute_pattern = r'id=["\'](.*?)["\']'
#
# # Iterate through form elements and extract and print the id attributes
# for form_element in form_elements:
#     id_attributes = re.findall(id_attribute_pattern, form_element)
#     for id_attribute in id_attributes:
#         print(id_attribute)

#Ex2


# def ex2(tag):
#     pattern = r'^<([a-z])+(>)\s*\w+\s*(</)([a-z])+(>)'
#     matched = re.match(pattern, tag)
#
#     if matched:
#         print("Valid HTML syntax")
#     else:
#         print("Invalid syntax")
#
#
# htmlCode = "<div> My div </div>"
# htmlNope = "<p,> my paragraph"
#
# ex2(htmlNope)

#Ex3

regex = r'(.*)( , )(.*)( , )(.*)( , )(.\d)'

with open("HW5Ex2.txt", "r") as f:
    my_text = f.readlines()

whole_txt = "".join(my_text)
matches = re.findall(regex, whole_txt)
info = [ [m[0], m[2], m[4], m[6]] for m in matches ]

print(info)

df = pd.DataFrame(data = info)
df.reset_index(inplace = True)
df.columns = ["Id", "LastName", "FirstName", "HiringDate", "Salary"]
df["Id"] += 1
print(df)
#df.to_excel("ex3.xlsx", index=False)

#Ex4

# def ex4(s):
#     if len(s)<3:
#         return "String doesn't match the language"
#     if s[0] == 'a' or s[-1] == 'b':
#         if s[1] == 'b' or s[-2] == 'a':
#             return "String matches language rules"
#
#     return "String doesn't match the language"
#
# print(ex4("aabba"))




