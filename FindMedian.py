# İki sıralı dizinin medyanını birleştirmeden hesaplar.
def findMedianSortedArrays(nums1, nums2):
    # nums1 her zaman kısa olan dizi olsun ki binary search küçük dizide yapalım
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    imin, imax = 0, m
    half_len = (m + n + 1) // 2
    
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        
        if i < m and nums2[j-1] > nums1[i]:
            # i çok küçük, artır
            imin = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            # i çok büyük, azalt
            imax = i - 1
        else:
            # i doğru, medyanı hesapla
            if i == 0:
                max_of_left = nums2[j-1]
            elif j == 0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums1[i-1], nums2[j-1])
            
            if (m + n) % 2 == 1:
                return max_of_left  # Tek sayıda eleman varsa ortadaki
            
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
            
            return (max_of_left + min_of_right) / 2.0
nums1 = [1,2,3,4]
nums2 = [3]
print(findMedianSortedArrays(nums1, nums2)) 


