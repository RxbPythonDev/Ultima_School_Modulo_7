import pytest
import datetime
from rest_framework.test import APIClient
from model_bakery import baker
from reserva.models import Petshop, Reserva
from rest_api.serializers import PetshopModelSerializer

@pytest.fixture
def dados_agendamento():
    hoje = datetime.date.today()
    petshop = baker.make(Petshop)
    return {
        'nome': 'nome teste', 'email': 'email@email.com',
        'nome_pet': 'pet teste', 'data': hoje, 'turno': 'manhã',
        'tamanho': 0, 'observacoes': '', 'petshop': petshop.pk,
    }

@pytest.fixture
def usuario():
    return baker.make('auth.User')

@pytest.mark.django_db
def test_criar_agendamento(usuario, dados_agendamento):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.post('/api/agendamento', dados_agendamento)
    assert resposta.status_code == 201

@pytest.fixture
def agendamento():
    return baker.make(Reserva)

@pytest.mark.django_db
def test_todos_agendamentos(agendamento):
    cliente = APIClient()
    resposta = cliente.get('/api/agendamento')
    assert len(resposta.data['results']) == 1

@pytest.fixture
def petshops():
    return baker.make(Petshop, _quantity=3)

@pytest.mark.django_db
def test_todos_petshops(petshops):
    cliente = APIClient()
    resposta = cliente.get('/api/petshop')
    assert len(petshops) == 3
    serializer = PetshopModelSerializer(Petshop.objects.all(), many=True)
    assert resposta.data['results'] == serializer.data
