import json

from django.views import View
from django.http import JsonResponse

from user.utils import LoginConfirm
from .models import Cart
from task.models import Product

class CartAdd(View):
    @LoginConfirm
    def post(self, request):
        print(request.user)
        print(request.user.id, request.user.name)
        data = json.loads(request.body)
        info = Product.objects.all()
        p_id = Product.objects.get(item=data['item']).id
        user_id = User.objects.get(id = request.user.id)
        print(user_id)
        if Cart.objects.filter(item=data['item']).exists():
            return JsonResponse({'message':'이미 담겼어요'})
        else:
            Cart(item=data['item'],
                count = data['count'],
                product_id = p_id,
                user_id = user_id
            ).save()

            return JsonResponse({'message':'Added'})

class Count(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            info = Cart.objects.get(item=data['item'])
            info.count = data['count']
            info.save()
        
            return JsonResponse({'count':info.count})

        except 'DoesNotExist':
            return JsonResponse({'message':'없는데 어케 더해?'})

class CartView(View):
    @LoginConfirm
    def get(self, request):
        print(request.user)
        print(request.user.id, request.user.name)
        cart_in = Cart.objects.filter(user_id=request.user.id)
        img = Product.objects.all()
        data_set=[]
        print(cart_in)
        if not cart_in:
            return JsonResponse({'message':'장바구니에 추가된 제품이 없습니다. 몇가지 건강 설문을 통해 나만을 위한 영양성분을 찾아보세요.'})
        elif request.method == 'GET':
            for i in range(len(cart_in)):
                order = ({'name' :cart_in[i].item,
                          'count':cart_in[i].count,
                          'id'   :cart_in[i].product_id,
                          'image':img[i].image_product,
                          'price':img[i].pricenum,
                          'colors':img[i].colors
                          })
                data_set.append(order)

        return JsonResponse({'order':data_set})



class DeleteItem(View):
    def post(self, request):
        data = json.loads(request.body)
        
        if data['delete'] == 'delete':
            Cart.objects.all().delete()
            return JsonResponse({'message':'텅텅'})




