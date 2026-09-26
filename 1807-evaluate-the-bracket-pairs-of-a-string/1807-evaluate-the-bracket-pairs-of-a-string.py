class Solution:
    def evaluate(self, s, knowledge):
        values = {}

        for key, value in knowledge:
            values[key] = value

        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                i += 1
                start = i

                while s[i] != ')':
                    i += 1

                key = s[start:i]

                if key in values:
                    result.append(values[key])
                else:
                    result.append("?")

                i += 1

            else:
                result.append(s[i])
                i += 1

        return "".join(result)