import pulp

model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Лимонад (вода - 2, цукор - 1, лимонний сік - 1)
A = pulp.LpVariable('A', lowBound=0, cat='Integer')
# Фруктовий сік (вода - 1, фруктове пюре - 2)
B = pulp.LpVariable('B', lowBound=0, cat='Integer')

model += A + B, "Production"

model += 2 * A + 1 * B <= 50    # Вода
model += 1 * A         <= 100   # Цукор
model += 1 * A         <= 30    # Лимонний сік
model +=         2 * B <= 40    # Фруктове пюре

model.solve()

print("Виробляти лимонаду:", A.varValue)
print("Виробляти фруктового соку:", B.varValue)
