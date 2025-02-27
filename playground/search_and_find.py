import re
oz_text = open(r"C:\Users\exol1\Parsing-w-regex\Compiling-and-matching\Wizard_Of_Oz.txt", encoding='utf-8').read().lower()

found_wizard = re.search("wizard", oz_text)

print(found_wizard)

all_lions = re.findall("lion", oz_text)
#print(all_lions)

number_lions = len(all_lions)

print(number_lions)