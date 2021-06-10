#!/usr/bin/env python
# coding=utf-8

import unittest

from PassTrough import Passthrough
from EncrDecr import DebateME


class TestEncodeDecode(unittest.TestCase):

    def test_encode_decode_simple(self):
        root = "./Mount"
        pt = Passthrough(root, "cle")
        path = "alo/papa"
        crypted_path = pt.translation_path_user_machine(path)
        decrypted_path = pt.translation_path_machine_user(crypted_path)
        self.assertEqual(decrypted_path, root+"/"+path)

    def test_encode_decode_simple_with_final_dashroot(self):
        root = "./Mount/"
        pt = Passthrough(root, "cle")
        path = "alo/papa"
        crypted_path = pt.translation_path_user_machine(path)
        decrypted_path = pt.translation_path_machine_user(crypted_path)
        self.assertEqual(decrypted_path, root+path)

    def test_encode_decode_simple_with_complex_root(self):
        root = "./efiuhequf/qefigqiufgef/feqfeqfewqf/wdqqd/"
        pt = Passthrough(root, "cle")
        path = "alo/papa"
        crypted_path = pt.translation_path_user_machine(path)
        decrypted_path = pt.translation_path_machine_user(crypted_path)
        self.assertEqual(decrypted_path, root+path)

    def test_encode_decode_simple_with_complex_path(self):
        root = "./efiuhequf/qefigqiufgef/feqfeqfewqf/wdqqd/"
        pt = Passthrough(root, "cle")
        path = "alo/papa/eqfeqfeqf/qefeqfeqfqef/qefeqffeqfqefqefqfqe/"
        crypted_path = pt.translation_path_user_machine(path)
        decrypted_path = pt.translation_path_machine_user(crypted_path)
        self.assertEqual(decrypted_path, root+path)

    def test_encode_decode_simple_path_and_simple_root(self):
        root = "mountpoint"
        pt = Passthrough(root, "cle")
        path = "alo"
        crypted_path = pt.translation_path_user_machine(path)
        decrypted_path = pt.translation_path_machine_user(crypted_path)
        self.assertEqual(decrypted_path, root+"/"+path)

    def test_encode_decode_no_dot_complex_path(self):
        root = "rot/moi/au/visage/"
        pt = Passthrough(root, "cle")
        path = "alo/papa"
        crypted_path = pt.translation_path_user_machine(path)
        decrypted_path = pt.translation_path_machine_user(crypted_path)
        self.assertEqual(decrypted_path, root+path)

    def test_encode_decode_wrong_passwd(self):
        root = "./alo"
        pt = Passthrough(root, "cle")
        pt2 = Passthrough(root, "clee")
        path = "alo/papa"
        crypted_path = pt.translation_path_user_machine(path)
        crypted_path2 = pt2.translation_path_user_machine(path)
        self.assertNotEqual(crypted_path, crypted_path2)

if __name__ == '__main__':
    unittest.main()
