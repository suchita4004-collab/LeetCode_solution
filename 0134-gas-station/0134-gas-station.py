class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        current_gas = 0
        start = 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                start = i + 1
                current_gas = 0

        if total_gas >= 0:
            return start

        return -1
        