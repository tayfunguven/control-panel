from import_export import resources
from ProductSystem.models import *

class InventoryCardResource(resources.ModelResource):
    class Meta:
        model = InventoryCard
        import_id_fields = ('card_id',)
        fields = ('card_id', 'product_code', 'product_name', 'product_category', 'image_one')
        
class InventoryResource(resources.ModelResource):
    class Meta:
        model = Inventory
        fields = ('id','product_code', 'product_name', 'recommended_price', 'product_quantity', 'warehouse_info',)
        
