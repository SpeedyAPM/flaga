def open_poem():
    text =  open('dane/poem.txt').read()
    text_lines = open('/var/www/flaga/dane/poem.txt', encoding='utf-8').readlines()
    poem_lines = []
    for line in text_lines:
        line = line.strip()
        poem_lines.append(line)
    
    return poem_lines

poem = open_poem()
#print(poem)