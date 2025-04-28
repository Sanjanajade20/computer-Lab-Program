queue = []

while True:
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Display")
    print("5. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        item = input("Enter item to enqueue: ")
        queue.append(item)
    elif choice == 2:
        if queue:
            print("Dequeued:", queue.pop(0))
        else:
            print("Queue is empty!")
    elif choice == 3:
        if queue:
            print("Front element:", queue[0])
        else:
            print("Queue is empty!")
    elif choice == 4:
        print("Queue:", queue)
    elif choice == 5:
        break
    else:
        print("Invalid choice!")