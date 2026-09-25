class Solution:
    def braceExpansionII(self, expression):
        def parse(index):
            result = {""}

            while index < len(expression) and expression[index] != '}':
                if expression[index] == '{':
                    group, index = parse(index + 1)

                    new_result = set()

                    for a in result:
                        for b in group:
                            new_result.add(a + b)

                    result = new_result

                elif expression[index] == ',':
                    index += 1
                    continue

                else:
                    new_result = set()

                    for word in result:
                        new_result.add(word + expression[index])

                    result = new_result
                    index += 1

            return result, index + 1

        # Handle top-level union correctly
        def solve(index):
            parts = []
            current = {""}

            while index < len(expression) and expression[index] != '}':
                if expression[index] == ',':
                    parts.append(current)
                    current = {""}
                    index += 1

                elif expression[index] == '{':
                    group, index = solve(index + 1)

                    current = {
                        a + b
                        for a in current
                        for b in group
                    }

                else:
                    current = {
                        word + expression[index]
                        for word in current
                    }
                    index += 1

            parts.append(current)

            result = set()
            for part in parts:
                result.update(part)

            return result, index + 1

        result, _ = solve(0)

        return sorted(result)
        