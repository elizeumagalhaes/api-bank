from rest_framework import serializers
from bank.models import Account, Card, Imagem, Invoice, Loan, LoanPayment, Statement, Transfer, User, Client, Address
from pictures.contrib.rest_framework import PictureField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'cpf', 'password']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'last_name', 'email', 'phone_number', 'birth_date', 'user', 'type']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['client', 'state', 'city', 'district', 'street', 'number', 'cep']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'client', 'agency', 'account', 'balance']

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['id', 'sender', 'recipient', 'value', 'date_time']

class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = ['id', 'account', 'operation', 'value', 'date_time']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'client', 'number', 'cvv', 'validty', 'limit', 'type', 'flag', 'ative', 'due_date']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'card', 'value', 'date']

class LoanSerialier(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id', 'account', 'value', 'date', 'interest_rate', 'approved', 'instalments', 'amount', 'first_installment', 'up_to_date', 'installments_paid', 'amount_paid']

class LoanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPayment
        fields = ['id', 'loan', 'value', 'date']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ['id', 'title', 'photo']
    photo = PictureField()

class AddImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ['id', 'title', 'photo']
