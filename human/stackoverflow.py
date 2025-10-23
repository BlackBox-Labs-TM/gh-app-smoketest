class Solution(object):
    def maxArea(self, height):
        ln = len(height)
        max_area = 0
        str_height = list(map(int, height))   #i used map to convert all numbers into a list of int

        for left_index in range(ln):
            left_height = str_height[left_index]

            for right_index in range(left_index + 1, ln):
                right_height = str_height[right_index]
                
                width = right_index - left_index    #we get the with after get both pointers

                height_lvl = min(left_height, right_height) #i change this variable bc was causing confusion
                area = width * height_lvl
                max_area = max(area, max_area)
        
        return max_area
