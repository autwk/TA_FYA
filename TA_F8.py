from collections import defaultdict


def format_state(state_set):
    """
    Форматирует множество состояний в строку для вывода.
    :param state_set: множество состояний (frozenset).
    :return: строка, представляющая состояния.
    """
    return "{" + ", ".join(sorted(state_set)) + "}"


def parse_states(states_str):
    """
    Преобразует строку вида "k1, k2" в множество состояний.
    :param states_str: строка состояний, разделённых запятыми.
    :return: множество состояний.
    """
    return set(states_str.split(", ")) if states_str else set()


def input_nfa_table():
    """
    Ввод таблицы переходов НКА.
    :return: таблица переходов НКА, начальное состояние, алфавит.
    """
    nfa_table = {}
    print("Введите таблицу переходов НКА (по одной строке в формате `k, a -> k1, k2`):")
    print("Для завершения ввода оставьте строку пустой.")
    while True:
        line = input("> ").strip()
        if not line:
            break
        try:
            left, right = line.split("->")
            state, symbol = map(str.strip, left.split(","))
            target_states = parse_states(right.strip())
            nfa_table[(state, symbol)] = target_states
        except ValueError:
            print("Ошибка ввода. Убедитесь, что строка соответствует формату `k, a -> k1, k2`.")

    start_state = input("Введите начальное состояние (например, k1): ").strip()
    alphabet = input("Введите алфавит (например, a, b): ").strip().split(", ")
    return nfa_table, start_state, set(alphabet)


def convert_to_dfa(nfa_table, start_state, alphabet):
    """
    Преобразует НКА в ДКА.
    :param nfa_table: таблица переходов НКА. Формат: {(state, symbol): set(states)}.
    :param start_state: начальное состояние НКА.
    :param alphabet: алфавит НКА (множество символов).
    :return: таблица переходов ДКА.
    """
    dfa_table = {}
    visited = set()
    queue = [frozenset([start_state])]

    while queue:
        current_set = queue.pop(0)
        if current_set in visited:
            continue

        visited.add(current_set)
        dfa_table[current_set] = {}

        for symbol in alphabet:
            next_set = set()
            for state in current_set:
                next_set.update(nfa_table.get((state, symbol), set()))

            if next_set:
                next_set = frozenset(next_set)
                dfa_table[current_set][symbol] = next_set

                if next_set not in visited:
                    queue.append(next_set)

    return dfa_table


# Ввод данных
nfa_table, start_state, alphabet = input_nfa_table()

# Преобразование
dfa_table = convert_to_dfa(nfa_table, start_state, alphabet)

# Вывод результата
print("\nТаблица переходов ДКА:")
for state, transitions in dfa_table.items():
    formatted_state = format_state(state)
    for symbol, target_state in transitions.items():
        formatted_target = format_state(target_state)
        print(f"T({formatted_state}, {symbol}) -> {formatted_target}")