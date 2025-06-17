def devolver_distintos(int1, int2, int3):
   total = int1 + int2 + int3
   if total > 15:
        return max(int1, int2, int3)
   elif total < 10:
        return min(int1, int2, int3)
   elif total >= 10 and total <= 15:
        if int1 !=  max(int1, int2, int3) and int1 != min(int1, int2, int3):
            return int1
        elif int2 !=  max(int1, int2, int3) and int2 != min(int1, int2, int3):
            return int2
        elif int3 !=  max(int1, int2, int3) and int3 != min(int1, int2, int3):
            return int3
        

print(devolver_distintos(10, 1, 3))