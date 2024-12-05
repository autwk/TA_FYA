from string import *

print("Введите продукции P:")
p = [x for x in input().split()]

def generate_language(productions, start_symbol='S', max_depth=4):
    # Словарь для хранения продукций с учётом контекста
    grammar = []
    for production in productions:
        left, right = production.split('->')
        if right == 'Л': right = ''
        grammar.append((left, right))

    # Функция для рекурсивной генерации строк
    def expand(string, depth):
        if depth == 0:
            return []  # Возвращаем пустой список, если достигли максимальной глубины

        generated = set()

        for left, right in grammar:
            # Проверяем, может ли правило быть применено
            pos = string.find(left)
            while pos != -1:
                # Создаём новую строку с применением правила
                new_string = string[:pos] + right + string[pos + len(left):]
                generated.add(new_string)
                pos = string.find(left, pos + 1)

        # Рекурсивно обрабатываем все полученные строки
        results = set(generated)
        for gen in generated:
            results.update(expand(gen, depth - 1))

        return results

    # Генерация языка
    language = {start_symbol}
    for d in range(1, max_depth + 1):  # Увеличиваем глубину
        new_words = set()
        for word in language:
            new_words.update(expand(word, d))
        language.update(new_words)

    # Отфильтруем строки, содержащие нетерминалы (заглавные буквы)
    filtered_language = {word for word in language if not any(c.isupper() for c in word)}

    return filtered_language


# Пример использования
language = list(generate_language(p))
language.sort(key=lambda x: (len(x), x))
print("L(G)={", end='')
for word in language[:20]: #первые 20 слов
    print(word, end = ', ')
print('...}')

#Примеры
'''Введите продукции P:
S->aSb S->bSa S->c
L(G)={c, acb, bca, aacbb, abcab, bacba, bbcaa, 
      aaacbbb, aabcabb, abacbab, abbcaab, baacbba, babcaba, 
      bbacbaa, bbbcaaa, aaaacbbbb, aaabcabbb, aabacbabb, aabbcaabb, abaacbbab, ...}'''

'''Введите продукции P:
S->ASA A->B AS->a B->c
L(G)={ac, cacc, ...}'''

'''Введите продукции P:
S->AB AB->BA A->aA A->a B->bB B->b
L(G)={ab, ba, aab, aba, abb, baa, bba, aaab, aaba, 
      aabb, abaa, abba, abbb, baaa, bbaa, bbba, aaaab, aaaba, aaabb, aabaa, ...}'''