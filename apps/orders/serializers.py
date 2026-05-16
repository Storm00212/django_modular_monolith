from rest_framework import serializers
from apps.products.models import Product
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('id', 'total_price', 'created_at')

    def validate_product(self, value):
        if not value:
            raise serializers.ValidationError("Product is required.")
        return value

    def validate_quantity(self, value):
        if value is not None and value <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        return value

    def validate_status(self, value):
        valid_statuses = [choice[0] for choice in Order.STATUS_CHOICES]
        if value and value not in valid_statuses:
            raise serializers.ValidationError(
                f"Status must be one of: {', '.join(valid_statuses)}."
            )
        return value
