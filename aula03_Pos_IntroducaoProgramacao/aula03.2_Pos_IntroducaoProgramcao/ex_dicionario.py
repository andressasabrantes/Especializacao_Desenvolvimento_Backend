palavras_programacao = {
    'C#': 'É uma linguagem de programação de propósito geral, orientada a objetos, desenvolvida pela Microsoft.',
    'Python': 'Python é uma linguagem de programação de alto nível, interpretada e de propósito geral.',
    'Javascript': 'JavaScript é uma linguagem de programação de alto nível, interpretada e voltada para o desenvolvimento web.',
    'Java': 'Java é uma linguagem de programação de propósito geral, orientada a objetos.'
}

for palavra in palavras_programacao:
    print(f'{palavra.upper()}: \n\t{palavras_programacao[palavra]}')