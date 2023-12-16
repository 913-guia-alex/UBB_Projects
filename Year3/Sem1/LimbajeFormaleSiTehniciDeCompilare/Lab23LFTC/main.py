from Scanner import Scanner


def main():
    file_names = ["p1.txt", "p2.txt", "p3.txt", "p1err.txt"]

    for file_name in file_names:
        try:
            scanner = Scanner()
            scanner.scan(file_name, "token.in")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
