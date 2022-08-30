from security import validating
from message import welcome
from app import run

def main():
    run()

if __name__ == "__main__":
    
    print(welcome())
    #comprobar la licencia
    if validating():
        main()
    else:
        print('')
        print('--------------------------------------------------------------------------------------------------------------------------')
        print(" You'll need to get a license, please contact our Services Customer Call Center staff at e-mail: da.torres@redlink.com.ar ")
        print('--------------------------------------------------------------------------------------------------------------------------')
    


