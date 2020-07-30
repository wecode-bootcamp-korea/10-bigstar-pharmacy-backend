import json

from django.views import View
from django.http import JsonResponse

from user.utils import LoginConfirm
from .models import Cart
from task.models import Product
from user.models import User

class CartAdd(View):
    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        info = Product.objects.all()
        try:
            p_id = Product.objects.get(item=data['item']).id
            user = User.objects.get(id = request.user.id)
            if Cart.objects.filter(item=data['item'], user_id=request.user.id).exists():
                return JsonResponse({'message':'이미 담겼어요'})
            else:
                Cart(item      = data['item'],
                    count      = data['count'],
                    product_id = p_id,
                    user_id    = user.id
                ).save()

                return JsonResponse({'message':'Added'})
        
        except:
            return JsonResponse({'message':'품목이 잘못되었어요'})

class Count(View):
    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        try:
            info       = Cart.objects.get(item=data['item'], user_id=request.user.id)
            info.count = data['count']
            info.save()
        
            return JsonResponse({'count':info.count})

        except:
            return JsonResponse({'message':'없는데 어케 더해?'})

class CartView(View):
    @LoginConfirm
    def get(self, request):
        cart_in  = Cart.objects.filter(user_id=request.user.id)
        data_set = []
        if not cart_in:
            return JsonResponse({'message':'장바구니에 추가된 제품이 없습니다. 몇가지 건강 설문을 통해 나만을 위한 영양성분을 찾아보세요.'})
        elif request.method == 'GET':
            for i in range(len(cart_in)):
                imgs  = cart_in[i].product_id
                img   = Product.objects.get(id=imgs)
                order = ({'name' :cart_in[i].item,
                          'count':cart_in[i].count,
                          'id'   :cart_in[i].product_id,
                          'image':img.image_product,
                          'price':img.pricenum,
                          'colors':img.colors
                          })
                data_set.append(order)

        return JsonResponse({'order':data_set})

class DeleteItem(View):
    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        
        if data['delete'] == 'delete':
            Cart.objects.filter(user_id=request.user.id).delete()
            return JsonResponse({'message':'텅텅'})




