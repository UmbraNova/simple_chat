user_name = input('Enter your name: ')
while True:
    print('[1] To see chat\n[2] Enter message')
    response = input('Enter 1 or 2: ')
    print('='*30)
    if response == '1':
        try:
            with open('chat.txt', 'r') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('Functional message: nothing so far\n')
    elif response == '2':
        new_message = input('Enter the message: ')
        with open('chat.txt', 'a') as file:
            file.write('{name}: {message}\n'.format(name=user_name, message=new_message))
    else:
        print('Unknown command!')
