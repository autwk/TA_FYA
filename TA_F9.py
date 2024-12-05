def build_grammar(transitions, terminals, final_states):
    productions = set()

    for transition in transitions:
        current_state, terminal, next_state = transition

        # Добавляем продукцию для перехода
        productions.add(f"{current_state}->{terminal}{next_state}")

        # Если следующее состояние конечное, добавляем продукцию для текущего состояния
        if next_state in final_states:
            productions.add(f"{current_state}->{terminal}")

    # Возвращаем упорядоченный список уникальных продукций
    return sorted(productions)


def main():
    print("Введите переходы в формате 'k1, b -> k2'. Оставьте строку пустой, чтобы завершить ввод:")
    transitions = []

    while True:
        line = input().strip()
        if line == "":
            break
        try:
            left, right = line.split("->")
            current_state, terminal = map(str.strip, left.split(","))
            next_state = right.strip()
            transitions.append((current_state, terminal, next_state))
        except ValueError:
            print("Неверный формат. Попробуйте снова.")

    print("Введите множество терминалов через пробел:")
    terminals = set(input().strip().split())

    print("Введите конечные вершины F через пробел:")
    final_states = set(input().strip().split())

    productions = build_grammar(transitions, terminals, final_states)

    # Выводим все продукции в одну строку через пробел
    print("Полученные продукции:")
    print(" ".join(productions))


if __name__ == "__main__":
    main()
