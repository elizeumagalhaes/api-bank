from rest_framework.generics import ListCreateAPIView
from bank.models import Account, Imagem, Invoice, Loan, LoanPayment, Statement, Transfer, User, Client, Address, Card
from bank.serializer import AccountSerializer, AddImageSerializer, AddressSerializer, CardSerializer, ClientSerializer, ImageSerializer, InvoiceSerializer, LoanPaymentSerializer, LoanSerialier, StatementSerializer, TransferSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs): 
        cpfUser = self.request.data['cpf']
        passwordUser = self.request.data['password']

        lista_usuarios = User.objects.all()

        encontrado = False

        if self.request.data['operacao'] == 'logar':
            for u in lista_usuarios:
                print(u.password)
                if u.cpf == cpfUser and u.password == passwordUser:
                    lista_clientes = Client.objects.all()
                    for c in lista_clientes:
                        if str(c) == str(u.id):
                            encontrado = True
                            cliente = {
                                "Nome":c.name + " " + c.last_name,
                                "E-mail":c.email,
                                "Telefone":c.phone_number,
                                "Data de Nascimento":c.birth_date,
                            }
                            break
                    if encontrado:
                        return Response({'cliente':cliente}, status=status.HTTP_200_OK)
                    else:
                        return Response({'cliente':None}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return super().create(request, *args, **kwargs)

class AccountList(ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class CardList(ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class InvoiceList(ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class ClientList(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AddressList(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class TransferList(ListCreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

class StatementList(ListCreateAPIView):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer

class LoanList(ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerialier

class LoanPaymentList(ListCreateAPIView):
    queryset = LoanPayment.objects.all()
    serializer_class = LoanPaymentSerializer

class ImagemList(ListCreateAPIView):
    queryset = Imagem.objects.all()
    serializer_class = ImageSerializer

class AddImagemList(ListCreateAPIView):
    queryset = Imagem.objects.all()
    serializer_class = AddImageSerializer