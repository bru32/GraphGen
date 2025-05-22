# QuickSort example
# Source:
#   Quick Sort in 3 Minutes
#   https://www.youtube.com/shorts/MeBYqiehwyQ
# Edited by:
# Bruce Wernick
# 22 May 2025


def QuickSort(arr):

  def QSort(low, high):

    def swap(i, j):
      arr[i], arr[j] = arr[j], arr[i]
    
    def part(low, high):
      piv = arr[high]
      i = low - 1
      for j in range(low, high):
        if arr[j] <= piv:
          i += 1
          swap(i, j)
      swap(i+1, high)
      return i+1

    if low < high:
      p = part(low, high)
      QSort(low, p-1)
      QSort(p+1, high)

  QSort(0, len(arr)-1)


# ---------------------------------------------------------

arr = [20,2,7,12,15,1,6,8]
QuickSort(arr)
print(arr)
