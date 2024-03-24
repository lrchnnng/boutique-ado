from decimal import Decimal
from django.conf import settings
# Handles the bag items variable 

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        # Use decimal when working with money = more accurate
        
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        # lets user know how much left they need to spend to qualify for free delivery

    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context