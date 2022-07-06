coords_1 = list(map(float, input().split(' ')))
coords_2 = list(map(float, input().split(' ')))


def find_intersection(a_coords: list, b_coords: list):
    try:
        if len(a_coords) != 4 or len(b_coords) != 4:
            raise BaseException("the number of coordinates for each object must be 4")

        # Распределяем координаты
        ax1, ay1 = a_coords[0], a_coords[1]
        ax2, ay2 = a_coords[2], a_coords[3]

        bx1, by1 = b_coords[0], b_coords[1]
        bx2, by2 = b_coords[2], b_coords[3]

        # Ищем точки минимума и максимума среди координат
        minax = min(ax1, ax2)
        maxax = max(ax1, ax2)
        minay = min(ay1, ay2)
        maxay = max(ay1, ay2)

        minbx = min(bx1, bx2)
        maxbx = max(bx1, bx2)
        minby = min(by1, by2)
        maxby = max(by1, by2)

        # Определяем координаты стороны
        x1 = max(minax, minbx)
        x2 = min(maxax, maxbx)
        y1 = max(minay, minby)
        y2 = min(maxay, maxby)

        # Если разница координат сторон меньше нуля, то прямоугольники не пересекаются иначе выводим площадь пересечения
        if x2 - x1 < 0 or y2 - y1 < 0:
            return False
        else:
            return abs(x2-x1) * abs(y2-y1)
    except TypeError:
        return "Insert only int or float lists"
    except BaseException as e:
        return e


print(find_intersection(coords_1, coords_2))


if __name__ == '__main__':
    pass