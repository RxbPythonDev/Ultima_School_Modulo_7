from pytest_django.asserts import assertTemplateUsed

import pytest

from base.models import Contato, Reserva

from datetime import date, timedelta

@pytest.fixture
def contato():
    contato = {
        'nome': 'Rafael',
        'email': 'rafael@email.com',
        'mensagem': 'teste',
        'data': '2023-09-05',
    }
    return contato

def test_contato_view_deve_retornar_template(client):
    response = client.get("/contato/")

    assert response.status_code == 200
    assertTemplateUsed(response, 'contato.html')

@pytest.mark.django_db
def test_contato_view_deve_retornar_sucesso(client, contato):
    response = client.post('/contato/', contato)

    assert response.status_code == 200
    assert 'Mensagem enviada com sucesso!' in str(response.content)

def test_inicio_view_deve_retornar_template(client):
    response = client.get('')

    assert response.status_code == 200
    assertTemplateUsed(response, 'inicio.html')

def test_login_usuario_view_deve_retornar_template(client):
    response = client.get('/login/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'login.html')

def test_novo_usuario_view_deve_retornar_template(client):
    response = client.get('/novo-usuario/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'novo_usuario.html')

def test_reserva_view_deve_retornar_template(client):
    response = client.get('/reserva/')

    assert response.status_code == 200
    assertTemplateUsed(response, 'reserva.html')
