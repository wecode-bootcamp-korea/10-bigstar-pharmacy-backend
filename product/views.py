import json

from django.views import View
from django.http import JsonResponse
from django.core import serializers

from .models import Product, Product_detail
#from cart.models import Cart

class ProductMainView(View):
    def get(self, request):
        info = Product.objects.all()
        data_set=[]

        if request.method == 'GET':
            for i in range(len(info)):
#                n = i+1
#                if Cart.objects.filter(product_id=n).exists():
#                   cart_info = Cart.objects.get(product_id=n)
#                   cart = cart_info.product_id
#                else:
#                   cart=0

                main_data = ({'item':info[i].item,
                              'deco':info[i].deco,
                              'icon1':info[i].icon1,
                              'icon2':info[i].icon2,
                              'desc1':info[i].desc1,
                              'desc2':info[i].desc2,
                              'desc3':info[i].desc3,
                              'period':info[i].period,
                              'price':info[i].price,
                              'image':info[i].image_product,
                              'colors':info[i].colors,
                             # 'cart':carat
                             })
                data_set.append(main_data)

        return JsonResponse({'main_data':data_set})


class ProductDetailView(View):
    def get(self, request, id):
        info = Product_detail.objects.all()
        product = Product.objects.all()
        if Cart.objects.filter(product_id=id).exists():
            cart_info = Cart.objects.get(product_id=id)
            cart = cart_info.product_id
        else:
            cart = 0
        num = id-1
        
        item = product[num].item
        deco = product[num].deco
        icon1= info[num].icon1
        icon2= info[num].icon2
        explan= info[num].explanation
        period = info[num].period
        price = info[num].price
        product_id = info[num].product_id
        img_url = info[num].image_detail
        rest  = info[num].rest
        
        return JsonResponse({'item':item,
                             'deco':deco,
                             'icon1':icon1,
                             'icon2':icon2,
                             'explanation':explan,
                             'period':period,
                             'price':price,
                             'product_id':product_id,
                             'img_url':img_url,
                             'rest':rest,
                             'cart':cart})


