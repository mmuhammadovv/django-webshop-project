from .models import ProductAttribute
from django.db.models import Min,Max
def get_filters(request):
	minMaxPrice=ProductAttribute.objects.aggregate(Min('price'),Max('price'))
	data={
		'minMaxPrice':minMaxPrice,
	}
	return data