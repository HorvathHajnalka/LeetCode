class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0 for i in range(len(temperatures))]
        helper_stack = []
        for i in range(len(temperatures)):
            while len(helper_stack) != 0 and temperatures[i] > temperatures[helper_stack[-1]]: 
                    stack_pop = helper_stack.pop()
                    answer[stack_pop] = i - stack_pop
            helper_stack.append(i)

        return answer