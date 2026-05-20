from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    Order CRUD ViewSet.
    - GET /api/orders/ — list all orders
    - POST /api/orders/ — create a new order
    - GET /api/orders/{id}/ — retrieve an order
    - PUT /api/orders/{id}/ — update an order
    - PATCH /api/orders/{id}/ — partial update an order
    - DELETE /api/orders/{id}/ — delete an order
    - GET /api/orders/by_status/?status=PAID — filter orders by status
    """
    queryset = Order.objects.select_related("product").order_by('-created_at')
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status.upper())
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Order created successfully.", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"data": serializer.data})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Order updated successfully.", "data": serializer.data})

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Order updated successfully.", "data": serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Order deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["get"])
    def by_status(self, request):
        """GET /api/orders/by_status/?status=PAID — filter orders by status."""
        status = request.query_params.get("status")
        if not status:
            return Response(
                {"error": "Query parameter 'status' is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        queryset = self.get_queryset().filter(status=status.upper())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
