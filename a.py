result = [f"{i} {'짝' * str(i).count('3')}" if '3' in str(i) else str(i) for i in range(100, 0, -1)]

print("\n".join(result))

