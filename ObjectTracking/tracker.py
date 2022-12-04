import math


# класс ведет учет объектов, его основная задача - отделять ранее распознанные объекты от новых
class Tracker:
    def __init__(self):
        # Хранит центральные позиции объектов (x, y)
        self.center_points = {}
        # Количество обнаруженных объектов
        self.id_count = 0

    def update(self, objects_rect):
        objects_bbs_ids = []

        for rect in objects_rect:
            x, y, width, height = rect
            center_x = x + width // 2
            center_y = y + height // 2

            # Проверяем, был ли объект обнаружен раннее
            same_object_detected = False
            for id, cpt in self.center_points.items():
                dist = math.hypot(center_x - cpt[0], center_y - cpt[1])

                # Если расстояние между центрами меньше 50п, то обнаружили старый объект
                if dist < 50:
                    self.center_points[id] = (center_x, center_y)
                    objects_bbs_ids.append([x, y, width, height, id])
                    same_object_detected = True
                    break

            # Если объект новый, добавляем его и увеличиваем количество объектов
            if same_object_detected is False:
                self.center_points[self.id_count] = (center_x, center_y)
                objects_bbs_ids.append([x, y, width, height, self.id_count])
                self.id_count += 1

        # Очищаем словарь от объектов, которых уже нет
        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        self.center_points = new_center_points.copy()
        return objects_bbs_ids
