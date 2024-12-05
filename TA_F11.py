print("Введите продукции P:")
p = [x for x in input().split()]


def generate_language_with_derivations(productions, start_symbol='S', max_depth=6):
    # Словарь для хранения продукций
    grammar = {}
    for production in productions:
        left, right = production.split('->')
        if right == 'Л': right = ''
        if left in grammar:
            grammar[left].append(right)
        else:
            grammar[left] = [right]

    # Функция для рекурсивной генерации строк с размеченными выводами
    def expand_with_derivation(current, derivation, depth):
        if depth == 0:
            return []  # Если достигли глубины, возвращаем пустой список

        # Если в текущей цепочке нет нетерминалов, возвращаем её
        if all(c not in grammar for c in current):
            return [(current, derivation + [current])]  # Добавляем конечную цепочку

        derivations = []
        for i, symbol in enumerate(current):
            if symbol in grammar:  # Если символ является нетерминалом
                for production in grammar[symbol]:
                    # Заменяем символ на продукцию
                    new_string = current[:i] + production + current[i + 1:]
                    # Добавляем текущую цепочку с разметкой в вывод
                    marked_string = (
                        current[:i] + f"*{symbol}*" + current[i + 1:]
                    )
                    derivations.extend(
                        expand_with_derivation(new_string, derivation + [marked_string], depth - 1)
                    )

        return derivations

    # Генерация строк с максимальной глубиной
    language_derivations = []
    for d in range(1, max_depth + 1):  # Начинаем с глубины 1
        if d == 1:
            # Для первой итерации добавляем только начальный символ с разметкой
            language_derivations.extend(
                expand_with_derivation(start_symbol, [f"*{start_symbol}*"], d)
            )
        else:
            language_derivations.extend(
                expand_with_derivation(start_symbol, [], d)
            )

    return language_derivations


# Пример использования
language_with_derivations = generate_language_with_derivations(p)
language_with_derivations.sort(key=lambda x: (len(x[0]), x[0]))  # Сортировка по длине и строке

print("Введите цепочку минимальной длины:")
min_length_word = input()

print("Различные размеченные выводы для цепочки минимальной длины:")
unique_derivations = set()
for word, derivations in language_with_derivations:
    if word == min_length_word:
        unique_derivations.add(" -> ".join(derivations))

for derivation in sorted(unique_derivations):
    print(derivation)
