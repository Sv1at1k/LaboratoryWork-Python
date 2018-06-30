from app import ma


class GoodStructure(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'material', 'amount','price')