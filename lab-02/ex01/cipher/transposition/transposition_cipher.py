class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        num_cols = key
        num_rows = len(text) // key
        if len(text) % key != 0:
            num_rows += 1

        decrypted = [""] * num_cols
        col = 0
        row = 0

        for symbol in text:
            decrypted[col] += symbol
            col += 1

            if col == num_cols or (
                col == num_cols - 1 and row >= len(text) % key
            ):
                col = 0
                row += 1

        return "".join(decrypted)