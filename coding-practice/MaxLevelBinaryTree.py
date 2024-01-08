def maxLevelSum(root):
        levels = [[0,0]]
        curr_level = 1
        if not root:
            return -1
        if not root.left and not root.right:
            return 1
        result = []
        queue = [[root, 0]]
        while queue:
            curr = queue.pop(0)
            node = curr[0]
            curr_level = curr[1]
            result.append(node.val)
            if curr_level == len(levels):
                levels.append([node.val, curr_level])
            else:
                
                levels[curr_level][0] += node.val
            
            if node.left:
                queue.append([node.left, curr_level + 1])
            if node.right:
                queue.append([node.right, curr_level + 1])
        maxl = levels[0][0]
        maxidx = 0
        print(levels)
        for i in range(1, len(levels)):
            if levels[i][0] > maxl:
                maxl = levels[i][0]
                maxidx = i
        return maxidx+1

print(maxLevelSum([1,7,0,7,-8,None,None]))        