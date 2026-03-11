from controller import To_do

def main():
    run = To_do()

    while True:
        run.process()

if __name__ == "__main__":
    main()