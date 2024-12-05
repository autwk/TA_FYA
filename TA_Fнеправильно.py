from string import *

print("Введите продукции P:")
p = [x for x in input().split()]

def generate_language(productions, start_symbol='S', max_depth=5):
    # Словарь для хранения продукций
    grammar = {}
    for production in productions:
        left, right = production.split('->')
        if right == 'Л': right = ''
        if left in grammar:
            grammar[left].append(right)
        else:
            grammar[left] = [right]

    # Функция для рекурсивной генерации строк
    def expand(symbol, depth):
        if depth == 0:
            return []  # Возвращаем пустой список, если достигли максимальной глубины
        
        if symbol not in grammar:
            return [symbol]  # Если символ не имеет продукции, возвращаем его

        strings = []
        for production in grammar[symbol]:
            # Рекурсивно обрабатываем продукцию
            parts = list(production)  # Превращаем продукцию в список символов
            expanded_parts = ['']  # Начинаем с пустой строки для комбинирования

            for part in parts:
                new_expanded = []
                for prefix in expanded_parts:
                    for result in expand(part, depth - 1):
                        new_expanded.append(prefix + result)
                expanded_parts = new_expanded

            strings.extend(expanded_parts)

        return strings

    # Генерация строк с максимальной глубиной
    language = set()
    for d in range(1, max_depth + 1):  # Начинаем с глубины 1
        language.update(expand(start_symbol, d))

    return language

# Пример использования
language = list(generate_language(p))
language.sort(key=lambda x:(len(x), x))
print("L(G)=:")
for word in language:
    print(word, end = ' ')