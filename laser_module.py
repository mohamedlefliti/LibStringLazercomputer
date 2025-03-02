# laser_module.py

class LaserModule:
    def __init__(self, intensity=1.0):
        """
        إنشاء كائن للوحدة الليزرية.

        :param intensity: شدة الليزر (اختياري).
        """
        self.intensity = intensity

    def generate_interference(self, freq1, freq2):
        """
        إنشاء تداخل باستخدام الليزر بين ترددات مختلفة.

        :param freq1: التردد الأول.
        :param freq2: التردد الثاني.
        :return: قيمة التداخل الناتجة.
        """
        interference = abs(freq1 - freq2) * self.intensity
        return interference

    def apply_laser(self, frequencies):
        """
        تطبيق الليزر على قائمة من الترددات لإنشاء جميع التداخلات الممكنة.

        :param frequencies: قائمة تحتوي على الترددات.
        :return: قائمة تحتوي على التداخلات الناتجة.
        """
        results = []
        for i in range(len(frequencies)):
            for j in range(i + 1, len(frequencies)):
                interference = self.generate_interference(frequencies[i], frequencies[j])
                results.append(interference)
        return results