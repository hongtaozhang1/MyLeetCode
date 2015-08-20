__author__ = 'hongtao'

class QuickSort:
    def qs(self, num, l, r):
        i = l
        j = r
        x = num[(i+j)/2]

        while i <= j:
            while num[i] < x:
                i += 1
            while num[j] > x:
                j -= 1

            if i<=j:
                t = num[i]
                num[i] = num[j]
                num[j] = t
                i += 1
                j -= 1

        if i < r:
            self.qs(num, i, r)
        if j > l:
            self.qs(num, l, j)

        return num


num = [4, 1, 5, 1, 6, 7, 134, 723, 45]
quicksort = QuickSort()
print quicksort.qs(num, 0, len(num)-1)