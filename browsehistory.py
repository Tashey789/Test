from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

# visit function
NoOfVisits = int(input("Enter the number of url history: "))
print("Enter URLS to visits: ")
for i in range(NoOfVisits):
    url = input ("URL: ")
    print(f"visiting {url}")
    backward_history.put(current_page)
    current_page = url

    # Display current page
    print("current page: {current_page}")

# go back
    while input("do you want to go back? (yes/no): ").lower() == 'yes':
        if not backward_history.empty():
            forward_history.put(current_page)
            current_page = backward_history.get()
            print(f"going back to {current_page}")
        else:
            print("No previous page available")

# go forward
while input("do you want to go forward? (yes/no): ").lower() == 'yes':
    if not forward_history.empty():
        backward_history.put(current_page)
        current_page = forward_history.get()
        print(f"going forward to {current_page}") 
    else:
        print("no forward page available")
                            