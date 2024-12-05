# Функция для ввода продукций
def input_productions():
    productions = []
    print("Введите продукции в формате 'A -> aB'. Для завершения ввода оставьте строку пустой и нажмите Enter.")
    while True:
        production = input("Введите продукцию: ")
        if production == '':  # Если строка пустая, завершаем ввод
            break
        # Разделяем продукцию на левую и правую части
        parts = production.split('->')
        if len(parts) == 2:
            left = parts[0].strip()  # Левый нетерминал
            right = parts[1].strip()  # Правая часть
            productions.append((left, right))
        else:
            print("Неверный формат продукции. Попробуйте снова.")
    return productions

# Множество состояний (нетерминалов) и терминалов
states = set()  # Множество состояний
terminals = set()  # Множество терминалов
transitions = {}  # Таблица переходов

# Функция для добавления переходов в таблицу
def add_transition(from_state, symbol, to_state):
    # Убедимся, что состояние существует в таблице переходов
    if from_state not in transitions:
        transitions[from_state] = {}  # Инициализируем пустой словарь для состояния
    if symbol not in transitions[from_state]:
        transitions[from_state][symbol] = set()  # Инициализируем пустое множество для символа
    if to_state is not None:
        transitions[from_state][symbol].add(to_state)  # Добавляем состояние в множество

# Функция для построения НКА из продукций
def build_nfa(productions):
    # Строим переходы и собираем терминалы и состояния
    for production in productions:
        left, right = production
        states.add(left)  # Добавляем левую часть как состояние

        if len(right) == 1 and right.islower():  # Продукция вида A -> a (где a - терминал)
            terminals.add(right)
            add_transition(left, right, '@')  # Переход в конечное состояние
        else:  # Продукция с цепочкой символов
            for i, symbol in enumerate(right):
                if symbol.islower():  # Терминал (например, 'a', 'b', 'c')
                    terminals.add(symbol)
                    if i == len(right) - 1:  # Если это последний символ, переход в конечное состояние
                        add_transition(left, symbol, '@')
                    else:  # Переход к следующему символу
                        next_state = right[i + 1]  # Следующий символ (может быть терминалом или нетерминалом)
                        add_transition(left, symbol, next_state)
                        left = next_state  # Обновляем текущее состояние для следующей итерации

    # Добавляем пустые переходы для конечного состояния '@'
    for terminal in terminals:
        add_transition('@', terminal, None)  # Переход из конечного состояния, обозначаем как пустое множество

# Функция для вывода переходов
def print_transitions():
    print("Переходы НКА:")
    # Вывод существующих переходов
    for from_state, trans in transitions.items():
        for symbol, to_states in trans.items():
            if not to_states:  # Если множество пустое, выводим 0
                print(f"t({from_state}, {symbol}) -> 0")
            else:
                print(f"t({from_state}, {symbol}) -> {to_states}")

    # Вывод оставшихся переходов, ведущих в пустое множество
    all_states = states.union({'@'})  # Включаем конечное состояние '@'
    for state in all_states:
        for terminal in terminals:
            if state not in transitions or terminal not in transitions[state]:
                print(f"t({state}, {terminal}) -> 0")

# Вводим продукции и строим НКА
productions = input_productions()
build_nfa(productions)

# Выводим таблицу переходов
print_transitions()
