def complete_dfa_to_nfa(V_t, transitions, k_fc):
    # Шаг 1: Создаем полную переходную функцию
    transition_dict = {}
    
    # Заполняем переходную функцию из исходного ДКА
    for (state_from, symbol, state_to) in transitions:
        if state_from not in transition_dict:
            transition_dict[state_from] = {}
        transition_dict[state_from][symbol] = state_to

    # Получаем все состояния
    all_states = set(transition_dict.keys())
    
    # Создаем полную функцию
    for state in all_states:
        for symbol in V_t:
            if symbol not in transition_dict[state]:
                transition_dict[state][symbol] = k_fc  # Переход в k_fc

    # Шаг 2: Преобразуем в НДКА
    nfa_transitions = list()
    for state_from, symbols in transition_dict.items():
        for symbol, state_to in symbols.items():
            nfa_transitions.append((state_from, symbol, {state_to}))

    # Добавляем переходы из k_fc в k_fc для всех символов
    for symbol in V_t:
        nfa_transitions.append((k_fc, symbol, {k_fc}))

    return nfa_transitions

print("Введите множество V_t:")
V_t = set([x for x in input().split()])
print("Введите количество и сами переходы:")
n = int(input())
t = set()
for _ in range(n):
    k, a, tka = input().split()
    t.add((k, a, tka))
k_fc = 'k_fc'

nfa_transitions = complete_dfa_to_nfa(V_t, t, k_fc)
nfa_transitions.sort()

print("НДКА:")
for state_from, symbol, state_to_set in nfa_transitions:
    # Преобразуем множество в строку, обернутую в фигурные скобки
    state_to_str = '{' + ' '.join(state_to_set) + '}'
    print(f"{state_from} {symbol} {state_to_str}")



#Пример
'''Введите множество V_t:
0 1
Введите количество и сами переходы:
4                                                  
k1 1 k2
k2 0 k2
k2 1 k3
k3 1 k3
НДКА:
k1 0 {k_fc}
k1 1 {k2}
k2 0 {k2}
k2 1 {k3}
k3 0 {k_fc}
k3 1 {k3}
k_fc 0 {k_fc}
k_fc 1 {k_fc}'''