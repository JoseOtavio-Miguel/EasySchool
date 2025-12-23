import os
import django

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'main.settings'
)

django.setup()

from accounts.models import User


def run():
    if not User.objects.filter(username='admin01').exists():
        User.objects.create_superuser(
            username='admin01',
            email='admin@escola.com',
            password='123456',
            role='admin',
            first_name='João',
            last_name='Silva'
        )

        print('✅ Usuário administrador criado com sucesso')
    else:
        print('⚠️ Usuário admin01 já existe')


if __name__ == '__main__':
    run()
