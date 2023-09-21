#!/usr/bin/python3
"""
This module provides various functions for performing calculations.
You can use these functions to add, subtract, multiply, and divide numbers. 
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    text = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
    
    lines = text.splitlines()
    formatted_text = '\n'.join(line.strip() for line in lines if line.strip())
    print(formatted_text)

if __name__ == "__main__":
    text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
