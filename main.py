def name(fname):
    print(f'Name is {fname}')

def surname(sname):
    print(f'Surname is {sname}')

def main():
    fname = 'Joel'
    sname = 'Muturi'
    is_running = True

    while is_running:
        print('1. Firstname')
        print('2. Surname')
        print('3. Exit')
        choice = input("Enter your choice")
        if choice == '1':
          name(fname)
        elif choice == '2':
          surname(sname)
        elif choice == '3':
          is_running = False
        else:
          print('That is not a valid choice')
print('Thank you! have a good day')

if __name__ == '__main__':
    main()

