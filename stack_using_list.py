# Stack Program (Using List)

stack = []

def push():
    element = input("Enter element to push: ")
    stack.append(element)
    print(element, "pushed into stack")

def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print(stack.pop(), "popped from stack")

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements are:")
        for i in reversed(stack):
            print(i)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")