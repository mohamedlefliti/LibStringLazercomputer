# applications.py

from laser_string_computer import LaserStringComputer

class Applications:
    def __init__(self, laser_intensity=1.0):
        """
        إنشاء كائن لتطبيقات الحاسوب الوتري الليزري.

        :param laser_intensity: شدة الليزر (اختياري).
        """
        self.lsc = LaserStringComputer(laser_intensity=laser_intensity)

    def chip_design(self, components):
        """
        تحسين تخطيط الرقائق الإلكترونية.

        :param components: قائمة تحتوي على العناصر (تردد، استهلاك طاقة، حرارة).
        :return: الترتيب الأمثل والمجموع الإجمالي للتكلفة.
        """
        return self.lsc.optimize_placement(components)

    def knapsack_solution(self, items, capacity):
        """
        حل مسألة الحقيبة.

        :param items: قائمة تحتوي على العناصر (وزن، قيمة).
        :param capacity: السعة القصوى للحقيبة.
        :return: المجموعة الأمثل والقيمة الإجمالية.
        """
        return self.lsc.knapsack_problem(items, capacity)

    def physics_simulation(self, frequencies):
        """
        محاكاة نظام فيزيائي.

        :param frequencies: قائمة تحتوي على الترددات.
        :return: نتائج المحاكاة.
        """
        return self.lsc.simulate_physics(frequencies)