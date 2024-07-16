import validators

def main():
    address = input('What\'s your email?')
    if validators.email(address):
        print('Valid')
    else:
        print('Invalid')


if __name__ == '__main__':
    main()
