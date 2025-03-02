from applications import Applications

# تعريف المشكلة
frequencies = [100, 200, 150, 300, 250]

# إنشاء كائن التطبيقات مع شدة ليزر 1.2
app = Applications(laser_intensity=1.2)

# تشغيل المحاكاة
simulation_results = app.physics_simulation(frequencies)

print("نتائج المحاكاة:", simulation_results)