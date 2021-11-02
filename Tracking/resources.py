from import_export import resources
from Tracking.models import ProductRegistration

class ProductRegistrationResource(resources.ModelResource):

    class Meta:
        model = ProductRegistration # default all files
        fields = ('id','product_id','product_name','product_amount','serial_number',
            'internal_number','product_status','product_category','description','children__additional_serial','children_additional_internal','children_additional_description'
        )