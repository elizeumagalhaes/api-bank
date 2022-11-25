from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.UserList.as_view()),
    path('contas/', views.AccountList.as_view()),
    path('cartoes/', views.CardList.as_view()),
    path('faturas/', views.InvoiceList.as_view()),
    path('clientes/', views.ClientList.as_view()),
    path('enderecos/', views.AddressList.as_view()),
    path('transferencias/', views.TransferList.as_view()),
    path('extratos/', views.StatementList.as_view()),
    path('emprestimos/', views.LoanList.as_view()),
    path('pgt_emprestimos/', views.LoanPaymentList.as_view()),
    path('imagens/', views.ImagemList.as_view()),
    path('adicionar-imagens/', views.AddImagemList.as_view()),
]