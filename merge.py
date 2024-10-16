
def merg_sort(arr):
    if len(arr) > 1:
        mejtex = len(arr) // 2 
        dzax = arr[:mejtex]        
        aj = arr[mejtex:]
        merg_sort(dzax)  
        merg_sort(aj)  
        i = j = k = 0
        
        while i < len(dzax) and j < len(aj):
            if dzax[i] < aj[j]:
                arr[k] = aj[i]
                i += 1
            else:
                arr[k] = aj[j]
                j += 1
            k += 1
        while i < len(dzax):
            arr[k] = dzax[i]
            i += 1
            k += 1
        while j < len(aj):
            arr[k] = aj[j]
            j += 1
            k += 1
    return arr