class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return "Stack is empty"

        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        if value == self.max_stack[-1]:
            self.max_stack.pop()

        return f"Popped: {value}"

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else "Empty"

    def get_max(self):
        return self.max_stack[-1] if self.max_stack else "Empty"


def main():
    s = MinMaxStack()

    while True:
        print("\n--- MinMax Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Get Min")
        print("4. Get Max")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            val = int(input("Enter value: "))
            s.push(val)

        elif choice == '2':
            print(s.pop())

        elif choice == '3':
            print("Min:", s.get_min())

        elif choice == '4':
            print("Max:", s.get_max())

        elif choice == '5':
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()