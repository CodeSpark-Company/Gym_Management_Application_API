from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.response import Response
from accounts.models.visitor import Visitor
from accounts.models.account import Account, Contact
from accounts.serializers.visitor import VisitorSerializer


class VisitorListCreate(generics.ListCreateAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

class VisitorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

    def perform_destroy(self, instance):
        account = Account.objects.get(id=instance.account.id)
        contact = Contact.objects.get(id=account.contact.id)

        contact.delete()
        account.delete()

        return super().perform_destroy(instance)
