# Определение таблиц переходов и выходов
transitions = {
    'z1': {'x1': 'z1', 'x2': 'z2', 'x3': 'z3', 'x4': 'z4'},
    'z2': {'x1': 'z2', 'x2': 'z3', 'x3': 'z4', 'x4': 'z1'},
    'z3': {'x1': 'z3', 'x2': 'z4', 'x3': 'z1', 'x4': 'z2'},
    'z4': {'x1': 'z4', 'x2': 'z1', 'x3': 'z2', 'x4': 'z3'}
}

outputs = {'z1': 'y1', 'z2': 'y2', 'z3': 'y3', 'z4': 'y4'}

# Начальное состояние
current_state = 'z3'

while True:
    # Ввод входного сигнала
    input_signal = input("Введите входной сигнал (x1, x2, x3, x4 или 'exit' для выхода): ")
    if input_signal == 'exit':
        break

    # Обновление состояния и вывод выходного сигнала
    if input_signal in ['x1', 'x2', 'x3', 'x4']:
        current_state = transitions[current_state][input_signal]
        print(f"Текущее состояние: {current_state}")
        print(f"Выходной сигнал: {outputs[current_state]}")
    else:
        print("Неверный входной сигнал. Попробуйте снова.")
