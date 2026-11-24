"""Простое окно: выбрать лабораторную и показать результаты всех её задач."""

import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk


ROOT = Path(__file__).resolve().parent
LABS = [f"lab_{number:02}" for number in range(1, 13)]

# Готовые входные данные для заданий. Они лежат прямо в этом файле,
# поэтому для запуска интерфейса не нужны отдельные demo.py.
EXAMPLES = {
    "lab_01": {
        "task_01.py": ["5", "3"], "task_02.py": ["10"],
        "task_03.py": ["8", "4"], "task_04.py": ["3", "2"],
        "task_05.py": ["-6", "2"], "task_06.py": ["0", "0", "3", "4"],
        "task_07.py": ["1", "5", "3"], "task_08.py": ["1", "5", "3"],
        "task_09.py": ["0", "0", "4", "3"],
        "task_10.py": ["0", "0", "4", "0", "0", "3"],
        "task_11.py": ["2"], "task_12.py": ["4"],
    },
    "lab_02": {
        "task_01.py": ["5", "3"], "task_02.py": ["4", "10", "7"],
        "task_03.py": ["0", "0", "3", "4", "6", "8"],
        "task_04.py": ["-2", "3"], "task_05.py": ["-7"],
        "task_06.py": ["42"], "task_07.py": ["23", "11"],
        "task_08.py": ["21"], "task_09.py": ["256"],
        "task_10.py": ["2024"],
    },
    "lab_03": {
        "task_01.py": ["250"], "task_02.py": ["5"],
        "task_03.py": ["5"], "task_04.py": ["2", "4"],
        "task_05.py": ["2", "4"], "task_06.py": ["1", "4"],
        "task_07.py": ["17", "5"], "task_08.py": ["10"],
        "task_09.py": ["5"], "task_10.py": ["48", "18"],
    },
    "lab_04": {
        "task_01.py": ["5"], "task_02.py": ["8"],
        "task_03.py": ["2", "-3"], "task_04.py": ["топот"],
        "task_05.py": ["1 3 5 7 9", "5"],
        "task_06.py": ["Алгоритмы помогают решать задачи"],
        "task_07.py": ["28"], "task_08.py": ["-12345"],
        "task_09.py": ["3"],
    },
    "lab_05": {
        "task_01.py": ["5"], "task_02.py": ["5", "2", "3"],
        "task_03.py": ["6", "1", "2"],
        "task_04.py": ["1 2 3 4 5"], "task_05.py": ["1 2 3 4 5 6"],
        "task_06.py": ["1 2 3 4 5", "2", "4"],
        "task_07.py": ["2 5 8 11"], "task_08.py": ["9 4 7 2 8"],
        "task_09.py": ["1 3 2 5 4 4"],
        "task_10.py": ["4 1 3 1"],
    },
    "lab_06": {
        "task_01.py": ["3", "1 2 3", "4 5 6", "7 8 9"],
        "task_02.py": ["3 3", "1 2 3", "4 5 6", "7 8 9", "2"],
        "task_03.py": ["3 3", "1 2 3", "4 5 6", "7 8 9"],
        "task_04.py": ["3 3", "1 2 3", "4 5 6", "7 8 9"],
        "task_05.py": ["3 3", "1 2 3", "5 6 7", "9 10 11"],
        "task_06.py": ["3 3", "1 9 3", "8 5 4", "7 2 6"],
        "task_07.py": ["3 3", "1 2 9", "8 5 4", "7 3 6"],
        "task_08.py": ["4 4", "1 2 3 4", "5 6 7 8", "9 10 11 12", "13 14 15 16"],
        "task_09.py": ["3 3", "3 2 1", "1 5 4", "2 8 7"],
        "task_10.py": ["3", "1 2 3", "4 5 6", "7 8 9"],
    },
    "lab_07": {"task_01.py": ["5 2 8 1 3"]},
    # В этих двух программах пустой ввод запускает встроенный пример.
    "lab_08": {"task_01.py": [""]},
    "lab_09": {"task_01.py": [""]},
    "lab_10": {"task_01.py": ["1 3 5 7 9 11", "7"]},
    "lab_11": {"task_01.py": ["8 3 10 1 6 14 4 7 13"]},
    "lab_12": {
        "task_01.py": [
            "1", "альфа", "1", "бета", "1", "гамма", "8", "3", "5",
            "6", "бета", "2", "7", "4", "0",
        ],
    },
}


def task_files(lab):
    return sorted(
        (ROOT / lab).glob("task_*.py"),
        key=lambda path: int(path.stem.split("_")[1]),
    )


def examples_for(lab):
    return EXAMPLES.get(lab, {})


def run_task(path, answers):
    input_text = "\n".join(answers) + "\n"
    try:
        result = subprocess.run(
            [sys.executable, str(path)],
            input=input_text,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=ROOT,
            timeout=15,
        )
        output = result.stdout
        if result.stderr:
            output += "\nОшибка программы:\n" + result.stderr
        return input_text, output, result.returncode == 0
    except subprocess.TimeoutExpired:
        return input_text, "Программа выполнялась дольше 15 секунд и была остановлена.\n", False
    except OSError as error:
        return input_text, f"Не удалось запустить программу: {error}\n", False


class DemoWindow:
    def __init__(self, root):
        self.root = root
        root.title("Демонстрация лабораторных")
        root.geometry("900x680")
        root.minsize(680, 480)

        ttk.Label(
            root,
            text="Показ лабораторных работ",
            font=("Arial", 18, "bold"),
        ).pack(anchor="w", padx=18, pady=(16, 8))
        ttk.Label(
            root,
            text="Выбери лабораторную и нажми «Вычислить». Готовые примеры запустятся для всех задач.",
        ).pack(anchor="w", padx=18, pady=(0, 12))

        controls = ttk.Frame(root)
        controls.pack(fill="x", padx=18, pady=(0, 12))
        ttk.Label(controls, text="Лабораторная:").pack(side="left")
        self.lab = tk.StringVar(value=LABS[0])
        self.lab_box = ttk.Combobox(
            controls, textvariable=self.lab, values=LABS,
            state="readonly", width=12,
        )
        self.lab_box.pack(side="left", padx=8)
        ttk.Button(controls, text="Вычислить", command=self.calculate).pack(side="left", padx=8)

        output_frame = ttk.Frame(root, padding=(18, 0, 18, 18))
        output_frame.pack(fill="both", expand=True)
        self.output = tk.Text(output_frame, wrap="word", font=("Menlo", 10), state="disabled")
        scroll = ttk.Scrollbar(output_frame, command=self.output.yview)
        self.output.configure(yscrollcommand=scroll.set)
        self.output.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self.set_output("Выбери лабораторную и нажми «Вычислить».\n")

    def set_output(self, text):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", text)
        self.output.configure(state="disabled")

    @staticmethod
    def show_input(input_text):
        lines = input_text.splitlines()
        if not lines or lines == [""]:
            return "  (пустая строка — запуск встроенного примера)\n"
        return "".join(f"  {line if line else '(пустая строка)'}\n" for line in lines)

    def calculate(self):
        lab = self.lab.get()
        try:
            examples = examples_for(lab)
        except (OSError, SyntaxError, ValueError) as error:
            self.set_output(f"Не удалось загрузить готовые значения: {error}\n")
            return

        files = task_files(lab)
        parts = [f"Лабораторная {lab[-2:]}\n"]
        for path in files:
            input_text, output, success = run_task(path, examples.get(path.name, []))
            parts.append(
                f"\n{'=' * 48}\n"
                f"Задание {path.stem.split('_')[1]}\n"
                f"Входные данные:\n{self.show_input(input_text)}"
                f"Результат программы:\n{output}"
            )
            if not success:
                parts.append("\nЗадание завершилось с ошибкой.\n")

        self.set_output("".join(parts))


if __name__ == "__main__":
    window = tk.Tk()
    DemoWindow(window)
    window.mainloop()
