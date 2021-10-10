class PrintFile:
    @staticmethod
    def print_file(encrypted_files: list):
        for file in encrypted_files:
            f = open(file, "r")
            lines = f.readlines()
            print(file)
            print("-------------------------------------")
            for line in lines:
                print(line, end="")
            print("\n")
