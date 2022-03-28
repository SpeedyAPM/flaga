import random
import wikipedia as wiki
wiki.set_lang("pl")

def character( name):
    content = wiki.summary(name, sentences=6)
    return content

# def character(name):
#     page = wiki.search(name)
#     print(page)
#     character_page = wiki.page(page[0])
#     content = character_page.content
#     return content

def character2():
    
    return "kangurzątko"

name = 'Bruce Lee'
