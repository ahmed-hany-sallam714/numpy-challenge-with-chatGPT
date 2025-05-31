# ============================================
# 💡 NumPy Hands-On Practice – Final Review 💡
# تمارين متقدمة باستخدام مكتبة NumPy في Python
# تشمل: Fancy Indexing, Boolean Masking, Broadcasting, Basic Stats
# By: Ilya Akhbaraki
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Boolean Masking – استخراج الدرجات الأكبر من 70
f = np.array([55, 78, 90, 42, 67, 88, 34, 99, 71, 45])
print("🎯 Grades > 70:", f[f > 70])

# ✅ استبدال الدرجات الأقل من 50 بكلمة "fail"
f = np.where(f < 50, "fail", f)
print("📌 Grades After Masking:", f)

# ✅ Fancy Indexing – استخراج درجات طلاب محددين
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("🎯 Selected Students' Scores:", x[[0, 3, 6, 9]])

# ✅ تحليل مصفوفة 2D: أكبر قيمة بكل صف ومجموع كل عمود
arr = np.random.randint(0, 20, 20).reshape((5, 4))
print("🔥 Max of Each Row:", np.max(arr, axis=1))
print("➕ Sum of Each Column:", np.sum(arr, axis=0))

# ✅ Swap بين عنصرين بدون متغير مؤقت
ar = np.array([1, 2, 3, 4])
ar[0], ar[1] = ar[1], ar[0]
print("🔄 After Swap:", ar)

# ✅ Broadcasting – تطبيق عملية جمع على مصفوفتين مختلفتين في البُعد
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([7, 8, 9])
print("🚀 Broadcasting Result:\n", x + y)

# ✅ توليد قيم وتسخين العضلات 💪
v = np.arange(10, 51, 5)
print("🎯 Range with Step 5:", v)

c = np.zeros((3, 3))
print("🧊 Zeros Matrix:\n", c)

# ✅ استخراج القيم الأكبر من 25
arr = np.array([10, 20, 30, 40, 50])
print("🔍 Values > 25:", arr[arr > 25])

# ✅ إحصائيات بسيطة: المتوسط والانحراف المعياري
numbers = np.array([2, 4, 6, 8, 10])
print("📊 Mean:", np.mean(numbers))
print("📉 Std Dev:", np.std(numbers))

# ✅ إعادة تشكيل Array باستخدام reshape
n = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2])
b = n.reshape((4, 3))
print("🔁 Reshaped Array:\n", b)


