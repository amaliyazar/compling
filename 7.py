import pymorphy2
text=''
file_text=open('input.txt', 'r', encoding="utf-8")
text_res = open("output.txt", "w")
for line in file_text:
	text+=line
text_split = text.split(" ")

morph = pymorphy2.MorphAnalyzer()

for a in text_split:
	parse = morph.parse(a)[0]
	result = parse.normalized
	sklon = parse.inflect({"gent"})
	lex = parse.lexeme

	text_res.write("Простой разбор: ")
	text_res.write(str(parse))
	text_res.write("\n")
	text_res.write ("Нормализовано: ")
	text_res.write(str(result))
	text_res.write("\n")
	text_res.write("Склоение в родительном:")
	text_res.write(str(sklon))
	text_res.write("\n")
	text_res.write("Лексемы:")
	text_res.write(str(lex))
	text_res.write("\n")
	text_res.write("\n")

text_res.close()
