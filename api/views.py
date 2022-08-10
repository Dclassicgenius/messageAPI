from rest_framework import viewsets, status, filters
from .serializers import MessageSerializer
from .models import Message
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'message', 'id']
    search_fields = ['name', 'message']
    ordering_fields = ['id', 'name', 'message']

    @swagger_auto_schema(operation_summary="Создать сообщение")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({serializer.data} , status=status.HTTP_201_CREATED, headers=headers)

    
    @swagger_auto_schema(operation_summary="Получить сообщение по идентификатору")
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({f"Hello {serializer.data['name']}! {serializer.data['message']}"})
    
    @swagger_auto_schema(operation_summary="Осписок сообщений")
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        for item in serializer.data:
            item['message'] = f"Hello {item['name']}! {item['message']}"
        return Response(item['message'])
    
    @swagger_auto_schema(operation_summary="Обновить сообщений")
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    @swagger_auto_schema(operation_summary="Удалить сообщение")
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


    