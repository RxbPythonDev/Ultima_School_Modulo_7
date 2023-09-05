from datetime import date

import pytest
from model_bakery import baker

from base.models import Contato, Petshop, Reserva

@pytest.fixture
def contato():
    contato = baker.make(
        Contato,
        nome='Rafael',
        email='rafael@email.com'
    )
    return contato

@pytest.mark.django_db
def test_str_contato_deve_retornar_string_formatada(contato):
    assert str(contato) == "Rafael (rafael@email.com)"
