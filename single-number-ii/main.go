package singlenumberii

/*
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。



示例 1：

输入：nums = [2,2,3,2]
输出：3
示例 2：

输入：nums = [0,1,0,1,0,1,100]
输出：100


提示：

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/WGki4K
进阶：你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

*/
func singleNumber(nums []int) int {
	a := 0
	b := 0

	for _, n := range nums {
		a = (a ^ n) & ^b
		b = (b ^ n) & ^a
	}
	return a
}
