# laser_string_computer.py

from laser_module import LaserModule
from itertools import permutations

class LaserStringComputer:
    def __init__(self, laser_intensity=1.0):
        """
        إنشاء كائن للحاسوب الوتري الليزري.

        :param laser_intensity: شدة الليزر (اختياري).
        """
        self.laser = LaserModule(intensity=laser_intensity)

    def convert_to_frequencies(self, data):
        """
        تحويل البيانات إلى ترددات اهتزازية.

        :param data: قائمة تحتوي على العناصر المراد تحويلها.
        :return: قائمة تحتوي على الترددات.
        """
        return [item[0] for item in data]

    def calculate_interference_with_laser(self, freq1, freq2):
        """
        حساب التداخل باستخدام الليزر بين ترددات مختلفة.

        :param freq1: التردد الأول.
        :param freq2: التردد الثاني.
        :return: قيمة التداخل الناتجة.
        """
        return self.laser.generate_interference(freq1, freq2)

    def optimize_placement(self, components):
        """
        إيجاد الترتيب الأمثل للمكونات بناءً على المسافة، الطاقة، والحرارة.

        :param components: قائمة تحتوي على العناصر (تردد، استهلاك طاقة، حرارة).
        :return: الترتيب الأمثل والمجموع الإجمالي للتكلفة.
        """
        best_order = None
        best_score = float('inf')

        for order in permutations(components):
            total_distance = 0
            total_power = sum(item[1] for item in order)
            total_heat = sum(item[2] for item in order)

            # حساب المسافة الإجمالية باستخدام الليزر
            for i in range(len(order) - 1):
                distance = self.calculate_interference_with_laser(order[i][0], order[i + 1][0])
                total_distance += distance

            # حساب التكلفة الإجمالية
            score = total_distance + total_power + total_heat

            # تحديث الترتيب الأمثل
            if score < best_score:
                best_score = score
                best_order = order

        return best_order, best_score

    def simulate_physics(self, frequencies):
        """
        محاكاة نظام فيزيائي باستخدام الليزر.

        :param frequencies: قائمة تحتوي على الترددات.
        :return: نتائج المحاكاة.
        """
        return self.laser.apply_laser(frequencies)

    def knapsack_problem(self, items, capacity):
        """
        حل مسألة الحقيبة باستخدام الحاسوب الوتري الليزري.

        :param items: قائمة تحتوي على العناصر (وزن، قيمة).
        :param capacity: السعة القصوى للحقيبة.
        :return: المجموعة الأمثل والقيمة الإجمالية.
        """
        best_value = 0
        best_combination = []

        from itertools import combinations

        for r in range(1, len(items) + 1):
            for combination in combinations(items, r):
                total_weight = sum(item[0] for item in combination)
                total_value = sum(item[1] for item in combination)

                if total_weight <= capacity and total_value > best_value:
                    best_value = total_value
                    best_combination = combination

        return best_combination, best_value