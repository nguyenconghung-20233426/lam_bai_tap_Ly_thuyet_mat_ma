import unittest
from DES_AES import (
    generate_subkeys,
    des_encrypt_trace,
    des_decrypt,
    gmul,
    AES_S_BOX,
    INV_AES_S_BOX,
    RCON,
    mix_columns,
    inv_mix_columns,
    aes128_encrypt_trace,
    aes128_decrypt,
)

class TestDES(unittest.TestCase):
    def test_sinh_khoa(self):
        khoa_bits = [0] * 64
        cac_khoa = generate_subkeys(khoa_bits)
        self.assertEqual(len(cac_khoa), 16)
        for k in cac_khoa:
            self.assertEqual(len(k), 48)

    def test_vi_du_1(self):
        khoa = "133457799BBCDFF1"
        ban_ro = "0123456789ABCDEF"
        ban_ma_mong_doi = "85E813540F0AB405"

        ban_ma_thuc_te, _ = des_encrypt_trace(ban_ro, khoa)
        self.assertEqual(ban_ma_thuc_te.upper(), ban_ma_mong_doi.upper())

        ban_ro_giai_ma = des_decrypt(ban_ma_thuc_te, khoa)
        self.assertEqual(ban_ro_giai_ma.upper(), ban_ro.upper())

    def test_thuan_nghich(self):
        khoa = "AABBCCDDEEFF0011"
        cac_ban_ro = [
            "0000000000000000",
            "FFFFFFFFFFFFFFFF",
            "123456789ABCDEF0"
        ]
        for p in cac_ban_ro:
            c, _ = des_encrypt_trace(p, khoa)
            p_giai_ma = des_decrypt(c, khoa)
            self.assertEqual(p_giai_ma.upper(), p.upper())


class TestAES128(unittest.TestCase):
    def test_0_nhandathuc_gf(self):
        self.assertEqual(gmul(0x57, 0x83), 0xC1)
        self.assertEqual(gmul(0xA6, 0x3D), 0xC6)

    def test_1_sinh_bang_s_box(self):
        self.assertEqual(AES_S_BOX[0x00], 0x63)
        self.assertEqual(AES_S_BOX[0x01], 0x7c)
        self.assertEqual(AES_S_BOX[0x02], 0x77)
        self.assertEqual(AES_S_BOX[0x53], 0xed)
        self.assertEqual(AES_S_BOX[0xff], 0x16)
        for x in range(256):
            self.assertEqual(INV_AES_S_BOX[AES_S_BOX[x]], x)

    def test_2_hang_so_vong_rcon(self):
        self.assertEqual(RCON[0], 0x01)
        self.assertEqual(RCON[1], 0x02)
        self.assertEqual(RCON[7], 0x80)
        self.assertEqual(RCON[8], 0x1b)
        self.assertEqual(RCON[9], 0x36)

    def test_3_mix_columns(self):
        # Ma trận state lưu theo cột (column-major)
        state = [
            0xd4, 0xbf, 0x5d, 0x30,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0
        ]
        state = mix_columns(state)
        self.assertEqual(state[0], 0x04)
        self.assertEqual(state[1], 0x66)
        self.assertEqual(state[2], 0x81)
        self.assertEqual(state[3], 0xe5)

        state = inv_mix_columns(state)
        self.assertEqual(state[0], 0xd4)
        self.assertEqual(state[1], 0xbf)
        self.assertEqual(state[2], 0x5d)
        self.assertEqual(state[3], 0x30)

    def test_vi_du_1(self):
        khoa = "0f1571c947d9e8590cb7add6af7f6798"
        ban_ro = "0123456789abcdeffedcba9876543210"
        ban_ma_chuan = "ff0b844a0853bf7c6934ab4364148fb9"

        ban_ma, _ = aes128_encrypt_trace(ban_ro, khoa)
        self.assertEqual(ban_ma.lower(), ban_ma_chuan.lower())

        ban_ro_giai_ma = aes128_decrypt(ban_ma, khoa)
        self.assertEqual(ban_ro_giai_ma.lower(), ban_ro.lower())

    def test_vi_du_2(self):
        khoa = "2b7e151628aed2a6abf7158809cf4f3c"
        ban_ro = "3243f6a8885a308d313198a2e0370734"
        ban_ma_chuan = "3925841d02dc09fbdc118597196a0b32"

        ban_ma, _ = aes128_encrypt_trace(ban_ro, khoa)
        self.assertEqual(ban_ma.lower(), ban_ma_chuan.lower())

        ban_ro_giai_ma = aes128_decrypt(ban_ma, khoa)
        self.assertEqual(ban_ro_giai_ma.lower(), ban_ro.lower())

    def test_toan_0(self):
        khoa = "00" * 16
        ban_ro = "00" * 16
        ban_ma_chuan = "66e94bd4ef8a2c3b884cfa59ca342b2e"

        ban_ma, _ = aes128_encrypt_trace(ban_ro, khoa)
        self.assertEqual(ban_ma.lower(), ban_ma_chuan.lower())


def xuat_file_ket_qua():
    # Xuất chi tiết từng trạng thái của các bộ test chính ra file để nộp Git
    logs = []
    
    _, des_log = des_encrypt_trace("0123456789ABCDEF", "133457799BBCDFF1")
    logs.append("*** TEST VECTOR DES - VÍ DỤ 1 ***\n" + des_log)

    _, aes_log1 = aes128_encrypt_trace("0123456789abcdeffedcba9876543210", "0f1571c947d9e8590cb7add6af7f6798")
    logs.append("*** TEST VECTOR AES-128 - VÍ DỤ 1 ***\n" + aes_log1)

    _, aes_log2 = aes128_encrypt_trace("3243f6a8885a308d313198a2e0370734", "2b7e151628aed2a6abf7158809cf4f3c")
    logs.append("*** TEST VECTOR AES-128 - VÍ DỤ 2 ***\n" + aes_log2)

    with open("output_ket_qua.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(logs))
    print("\n>> Đã xuất toàn bộ trạng thái các vòng ra file 'output_ket_qua.txt'!")


if __name__ == "__main__":
    # Xuất báo cáo trước khi chạy unittest
    xuat_file_ket_qua()
    unittest.main(verbosity=2)