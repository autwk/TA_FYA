def generate_nfa_strings(F, transitions, max_length):
    # Создаем словарь для переходной функции
    transition_dict = {}
    for (state_from, symbol, state_to) in transitions:
        if state_from not in transition_dict:
            transition_dict[state_from] = {}
        if symbol not in transition_dict[state_from]:
            transition_dict[state_from][symbol] = set()
        transition_dict[state_from][symbol].add(state_to)

    # Функция для генерации строк
    def explore(states, current_string, length):
        if length > max_length:
            return
        
        # Если одно из текущих состояний финальное, добавляем строку в язык
        if any(state in F for state in states):
            language.add(current_string)

        # Исследуем все возможные переходы из текущих состояний
        for state in states:
            if state in transition_dict:
                for symbol, next_states in transition_dict[state].items():
                    for next_state in next_states:
                        explore([next_state], current_string + symbol, length + 1)

    language = set()
    # Начинаем с начального состояния (предположим, что это k1)
    start_state = 'k1'
    explore([start_state], '', 0)

    return language

print("Введите мн-во конечных состояний F:")
F = set([x for x in input().split()])
print("Введите количество и сами переходы:")
n = int(input())
t = set()
for _ in range(n):
    k, a, tka = input().split()
    t.add((k, a, tka))

max_length = 4  # Максимальная длина строк для генерации
language = generate_nfa_strings(F, t, max_length)

print("Сгенерированный язык L:", language)


#Пример
'''Введите мн-во конечных состояний F:
k3 k4
Введите количество и сами переходы:
5
k1 * k2
k1 * k4
k2 | k3
k3 | k3
k4 * k4
Сгенерированный язык L: {'*|', '***', '*|||', '*', '****', '**', '*||'}'''