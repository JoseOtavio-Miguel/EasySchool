import os
import django
from datetime import date

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'main.settings'
)

django.setup()

from accounts.models import User

def run():
    User.objects.create_user(
        username='admin01',
        password='123456',
        email='admin@escola.com',
        first_name='João',
        last_name='Silva',
        cpf='111.211.111-11',
        date_of_birth=date(2010, 5, 10),
        gender='M',
        phone='(11) 99999-9999',
        address='Rua A',
        address_number='100',
        neighborhood='Centro',
        city='São Paulo',
        state='SP',
        zip_code='01000-000',
        role='admin'
    )

    print('✅ Usuário criado com sucesso')

if __name__ == '__main__':
    run()
