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
        
class WarehouseResource(resources.ModelResource):
    class Meta:
        model = WarehouseInfo
        import_id_fields = ('warehouse_id',)
        fields = ('warehouse_id', 'warehouse_location', 'shelf_info', 'shelf_no', 'shelf_product_x_axis', 'shelf_product_y_axis')