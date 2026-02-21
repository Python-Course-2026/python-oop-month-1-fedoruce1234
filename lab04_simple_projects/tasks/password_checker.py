class PasswordChecker:
    """Задача: password_checker"""
    def __init__(self, pwd: str):
        self.pwd = pwd

    def is_strong(self) -> bool:
        """Длина >= 8 и есть цифра"""
        if len(self.pwd) < 8:
            return False


        has_digit = False
        for char in self.pwd:
            if char.isdigit():
                has_digit = True
                break

        return has_digit



