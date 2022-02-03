from datetime import datetime, timezone


from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view

from deals.models import Deal
from deals.serializers import DealSerializer
from orders.serializers import OrderSerializer
from orders.models import Order

# Create your views here.


class DealViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Deal.objects.all()
    serializer_class = DealSerializer


@api_view(['POST'])
def claim_deal(request, deal_id):
    """
    List all code snippets, or create a new snippet.
    """
    # handle for concurrency as well
    # check if the deal is active and number of items available in deal
    # decrease item once done

    data = request.data
    user_id = data.get('user_id')
    deal = get_object_or_404(Deal, pk=deal_id)
    import ipdb; ipdb.set_trace()

    if not deal.is_active or not deal.end_time < datetime.now(timezone.utc) or deal.available_items <= 0:
        return Response({
                "message": "Deal expired"
        }, status=status.HTTP_400_BAD_REQUEST)

    if Order.objects.filter(deal=deal, user_id=user_id).exists():
        return Response({
                        "message": "User has already used up this deal"
                        }, status=status.HTTP_400_BAD_REQUEST)

    deal.available -= 1
    if deal.available == 0:
        deal.is_active = False
    deal.save()
    order = Order.objects.create(deal=deal, user_id=user_id)
    return Response({
                    "order_id": "{}".format(order.id),
                    "user_id": user_id
                    }, status=status.HTTP_201_CREATED)
