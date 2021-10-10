import unittest
import get_files
import crypto


class MyTestCase(unittest.TestCase):
    cr = crypto.Cryptography()

    def test_get_files_with_files(self):
        self.assertEqual(get_files.FileGetter().get_files("./text_files"), ["./text_files/a.txt",
                                                                            "./text_files/b.txt", "./text_files/c.txt"])

    def test_get_files_no_files(self):
        self.assertEqual(get_files.FileGetter().get_files("./tee"), [])

    def test_encrypt_and_decrypt_a(self):
        f = open("./text_files/a.txt", "r")
        lines_before = f.readlines()
        f.close()
        self.cr.encrypt(["./text_files/a.txt"])
        self.cr.encrypt(["./text_files/a.txt"])
        self.cr.decrypt(["./text_files/a.txt"])
        self.cr.decrypt(["./text_files/a.txt"])
        f = open("./text_files/a.txt", "r")
        lines_after = f.readlines()
        f.close()
        self.assertEqual(lines_after, lines_before)

    def test_encrypt_and_decrypt_b(self):
        f = open("./text_files/b.txt", "r")
        lines_before = f.readlines()
        f.close()
        self.cr.encrypt(["./text_files/b.txt"])
        self.cr.decrypt(["./text_files/b.txt"])
        f = open("./text_files/b.txt", "r")
        lines_after = f.readlines()
        f.close()
        self.assertEqual(lines_after, lines_before)

    def test_encrypt_and_decrypt_c(self):
        f = open("./text_files/c.txt", "r")
        lines_before = f.readlines()
        f.close()
        self.cr.encrypt(["./text_files/c.txt"])
        self.cr.decrypt(["./text_files/c.txt"])
        f = open("./text_files/c.txt", "r")
        lines_after = f.readlines()
        f.close()
        self.assertEqual(lines_after, lines_before)


if __name__ == '__main__':
    unittest.main()