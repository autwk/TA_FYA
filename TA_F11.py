class Grammar:
    def __init__(self, productions):
        self.productions = {}
        for prod in productions:
            lhs, rhs = prod.split('->')
            if lhs not in self.productions:
                self.productions[lhs] = []
            self.productions[lhs].append(rhs)

    def generate_derivations(self, start_symbol, target, current, derivation, marked_derivation):
        # Если текущая цепочка совпадает с целевой, выводим результат
        if current == target:
            print("Вывод:", " -> ".join(derivation))
            print("Размеченный вывод:", " -> ".join(marked_derivation))
            return
        
        # Ограничение на количество замен, чтобы избежать бесконечной рекурсии
        if len(derivation) > 10:  # Вы можете изменить это значение по необходимости
            return
        
        # Перебираем каждый символ в текущей цепочке
        for i in range(len(current)):
            if current[i] in self.productions:
                for production in self.productions[current[i]]:
                    # Создаем новую цепочку, заменяя текущий символ на продукцию
                    new_current = current[:i] + production + current[i + 1:]
                    new_derivation = derivation + [current[i] + " -> " + production]
                    new_marked_derivation = marked_derivation + [current[:i] + "*" + production + "*" + current[i + 1:]]
                    # Рекурсивно вызываем функцию с новой цепочкой
                    self.generate_derivations(start_symbol, target, new_current, new_derivation, new_marked_derivation)

def main():
    productions = ["S->ASA", "A->B", "AS->a", "B->c"]
    target = "ac"
    grammar = Grammar(productions)
    
    print("Все выводы для цепочки:", target)
    grammar.generate_derivations("S", target, "S", [], [])

if __name__ == "__main__":
    main()
