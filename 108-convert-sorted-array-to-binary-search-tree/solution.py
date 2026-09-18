class Solution:
    def sortedArrayToBST(self, nums):
        def build(left, right):
            if left > right:
                return None

            # Choose the middle element as the root
            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            # Build left and right subtrees
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)
