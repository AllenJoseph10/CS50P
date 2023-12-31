def main():
    convert()

def convert():
    line = input()
    output = line.replace(':)','🙂').replace(':(','🙁')
    print(output)

main()
