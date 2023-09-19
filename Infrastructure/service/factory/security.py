from django.contrib.auth.tokens import PasswordResetTokenGenerator



class TokenActiveUserGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_email_verified)


class Security:
    def __init__(self):
        self.token_generator = TokenActiveUserGenerator()

    def generate_token(self, user):
        return self.token_generator.make_token(user)

    def check_token(self, user, token):
        return self.token_generator.check_token(user, token)