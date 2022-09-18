class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Sort the lists, on the base of their length
        list1, list2 = sorted((list1, list2), key=len)
        # Get length of each list
        length1, length2 = len(list1), len(list2)
        # Calculate the half length of their resultant list
        halfLength = (length1 + length2 - 1) // 2
        # High and low variable for the binary search
        low, high = 0, length1
        # While lower doesn't go higher than the high
        while low < high:
            # Get the middle index
            mid = (low + high) // 2
            # Check if our distance from half length to the mid is 0, or middle value of first list is greater
            # than the halflength-mid-1, then change the high to mid
            if ((halfLength - mid - 1) < 0) or (list1[mid] >= list2[halfLength - mid - 1]):
                high = mid
            else:
                # Else take the lower to the mid
                low = mid + 1
        # Get the middle at the low, for indexing
        mid = low
        # Create a sorted list from list one, that goes from mid to the next two indexed
        # and append another sublist from the second list that goes from halflength-mid to the next two elements
        next = sorted(list1[mid: mid+2] +
                    list2[halfLength - mid: halfLength - mid + 2])
        # Return the median from the resultant list
        return (next[0] + next[1 - (length1 + length2) % 2]) / 2.0
