package org.example;

public class day6 {
    public int[] twoSum(int[] nums, int target) {
        int lengthOfArray = nums.length;
        for (int i = 0; i < lengthOfArray; i++) {
            for (int j = 0; j < lengthOfArray; j++) {
                if (i != j) {
                    if (nums[i] + nums[j] == target) {
                        return new int[] {i, j};
                    }
                }
            }
        }
        return nums;
    }
}
