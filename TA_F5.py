def generate_strings(F, transitions, max_length):
    # Создаем словарь для переходной функции
    transition_dict = {}
    for (state_from, symbol, state_to) in transitions:
        if state_from not in transition_dict:
            transition_dict[state_from] = {}
        transition_dict[state_from][symbol] = state_to

    # Функция для генерации строк
    def explore(state, current_string, length):
        if length > max_length:
            return
        
        # Если текущее состояние финальное, добавляем строку в язык
        if state in F:
            language.add(current_string)

        # Исследуем все возможные переходы из текущего состояния
        if state in transition_dict:
            for symbol, next_state in transition_dict[state].items():
                explore(next_state, current_string + symbol, length + 1)

    language = set()
    # Начинаем с начального состояния (предположим, что это k1)
    start_state = 'k1'
    explore(start_state, '', 0)

    return language

print("Введите мн-во конечных состояний F:")
F = set([x for x in input().split()])
print("Введите количество строк и саму ф-цию t:")
n = int(input())
t = set()
for _ in range(n):
    k, a, tka = input().split()
    t.add((k, a, tka))
max_length = 4  # Максимальная длина строк для генерации
language = generate_strings(F, t, max_length)
language = list(language)
language.sort(key=lambda x:(len(x), x))
print("Сгенерированный язык L:", language)




#Пример
'''Введите мн-во конечных состояний F:
k3
Введите количество строк и саму ф-цию t:
4
k1 1 k2
k2 0 k2
k2 1 k3
k3 1 k3
Сгенерированный язык L: ['11', '101', '111', '1001', '1011', '1111']'''