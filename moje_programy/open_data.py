def open_data():
    text =  open('data/data.txt').read()
    text_lines = open('/var/www/flaga/data/data.txt', encoding='utf-8').readlines()
    poem_lines = []
    for line in text_lines:
        line = line.strip()
#        line = "<a>href="+line+"</a>"
        poem_lines.append(line)
    
    return poem_lines

# poem = open_poem()
# print(poem)