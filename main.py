import get_files
import crypto
import printer


class Main:
    path = ""
    action = ""
    encrypted_files = []

    def fill_action(self):
        while True:
            self.action = input("Выберите действие: зашифровать/расшифровать ------- e/d: ")
            if self.action != "e" and self.action != "d":
                print("Вы ввели недопустимое значение")
            else:
                break

    def fill_path(self):
        while True:
            self.path = input("Введите относительный путь до рабочей папки: ")
            self.encrypted_files = get_files.FileGetter.get_files(self.path)
            if len(self.encrypted_files) == 0:
                print("Такая папка не существует или пустая")
            else:
                break

    def act(self):
        cr = crypto.Cryptography()
        if self.action == "e":
            cr.encrypt(self.encrypted_files)
            printer.PrintFile.print_file(self.encrypted_files)
        else:
            cr.decrypt(self.encrypted_files)
            printer.PrintFile.print_file(self.encrypted_files)

    def first(self):
        self.fill_action()
        self.fill_path()
        self.act()


obj = Main()
obj.first()
