from cryptography.fernet import Fernet


class Cryptography:
    cipher_key = b'RMUKhJk9hOQg47MKxCL1GJfQNzaIwiYQNZfuLm1tsGI='
    cipher = Fernet(cipher_key)

    def encrypt(self, encrypting_files: list):
        for file in encrypting_files:
            f = open(file, "r")
            lines = f.readlines()
            f.close()

            for i in range(len(lines)):
                lines[i] = self.cipher.encrypt(bytes(lines[i], "utf-8"))

            f = open(file, "w")
            for line in lines:
                f.write(str(line).replace('b', '', 1).replace("'", "", 2) + "\n")
            f.close()

    def decrypt(self, encrypting_files: list):
        for file in encrypting_files:
            f = open(file, "rb")
            lines = f.readlines()
            f.close()

            for i in range(len(lines)):
                lines[i] = self.cipher.decrypt(lines[i])

            f = open(file, "wb")
            for line in lines:
                f.write(line)
            f.close()
