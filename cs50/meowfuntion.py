def main():
    number = get_number()
    meow(number)
    
    
    
def meaow(n):
        while True:
            n = int(input("whats n?: "))
            if n > 0:
                break
            
        return n



def meow(n):
    for _ in range(n):
        for _ in range(3):
            print("meow")