patient_queue= []

while True:
    from queue import Queue
    print('desk manager')
    print('1.Register Patient')
    print('2.Remove Patient')
    print('3.Display Patient Queue')
    print('4.Exit')
    
    option= int(input("enter your choice(option number):"))

    if option == 1:
        name= input('enter the name of the patient:')
        patient_queue.append(name)
        print(f"patient {name} registered")

    elif option == 2:
        if not patient_queue:
            print("no patient in queue")
        else:
            remove = patient_queue.pop(0)
            print(f'patient {remove} removed after meeting the doctor')

    elif option == 3:
        print("current patients:")
        if not patient_queue:
            print('no patients in queue')
        else:
            queue_length= len(patient_queue)
            for i in range (queue_length):
                index = i + 1
                patient= patient_queue[i]
                print(f'{index}. {patient}')
    
    elif option ==4:
        print('exiting program')
        break

    else:
        print("error!")