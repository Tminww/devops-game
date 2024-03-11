import random

# ROW_COUNT = 21
# COLUMN_COUNT = 47

row = 21
column = 47

# 1. Белый
# 2. Ярко-красный
# 3. Зеленый
# 4. Ярко-зеленый
# 5. Синий
# 6. Светло-синий
# 7. Желтый
# 8. Розовый
# 9. Оранжевый
# 0. Черный (стены, цвет не доступен для выбора)


class GameField:
    colors = {
        "1": "Белый",
        "2": "Ярко-красный",
        "3": "Зеленый",
        "4": "Ярко-зеленый",
        "5": "Синий",
        "6": "Светло-синий",
        "7": "Желтый",
        "8": "Розовый",
        "9": "Оранжевый",
        "0": "Черный",
    }

    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column
        self.field = None

        # FIXME user1_color != user2_color
        self.first_user_color = random.randint(1, 9)
        self.second_user_color = random.randint(1, 9)

    def get_field(self):
        self.matrix = [
            [random.randint(0, 9) for _ in range(self.column)] for _ in range(self.row)
        ]
        self.__symmetry()
        self.__set_walls()
        self.__set_users_position()
        return self.matrix

    def __set_users_position(self):
        self.matrix[0][0] = int(
            f"1{self.first_user_color}",
        )

        self.matrix[self.row - 1][self.column - 1] = int(
            f"2{self.second_user_color}",
        )

    def __symmetry(self):
        for i in range(self.row):
            for j in range(self.column):
                self.matrix[self.row - 1 - i][self.column - 1 - j] = self.matrix[i][j]

    def __set_walls(self):
        for i in range(self.row):
            if i % 2 != 0:
                self.matrix[i][self.column - 1] = -1

    def print_field(field):

        for row in field:

            print(*row)
