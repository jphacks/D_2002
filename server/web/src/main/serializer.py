from rest_framework import serializers # Django Rest Frameworkをインポート
from .models import Product # models.py のcouponクラスをインポート

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product # 扱う対象のモデル名を設定する
        fields = '__all__'