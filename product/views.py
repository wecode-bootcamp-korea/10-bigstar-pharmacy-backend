import json, jwt

from django.views import View
from django.http import JsonResponse

from proj1.settings import SECRET_KEY, ALGORITHM

from .models import Product, Product_detail
from cart.models import Cart
from user.models import User

class ProductMainView(View):
    def get(self, request):
        info = Product.objects.all()
        data_set=[]
        try:
            token   = request.headers.get('Authorization', None)
            payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
            user    = User.objects.get(id = payload['user'])
            if request.method == 'GET':
                for i in range(len(info)):
                    n = i+1
                    print(user)
                
                    if Cart.objects.filter(product_id=n, user_id=user.id).exists():
                        cart_info = Cart.objects.get(product_id=n, user_id=user.id)
                        print(cart_info.item, cart_info.product_id)
                        cart = cart_info.product_id
                    else:
                        cart = 0

                    main_data = ({'item':info[i].item,
                              'decoration':info[i].decoration,
                              'icon1':info[i].icon1,
                              'icon2':info[i].icon2,
                              'description1':info[i].description1,
                              'description2':info[i].description2,
                              'description3':info[i].description3,
                              'period':info[i].period,
                              'price':info[i].price,
                              'image':info[i].image_product,
                              'colors':info[i].colors,
                              'cart':cart})
                    data_set.append(main_data)
            
            return JsonResponse({'main_data':data_set})
        
        except:
            #if request == "GET":
            for i in range(len(info)):
                main_data = ({'item':info[i].item,
                              'decoration':info[i].decoration,
                              'icon1':info[i].icon1,
                              'icon2':info[i].icon2,
                              'description1':info[i].description1,
                              'description2':info[i].description2,
                              'description3':info[i].description3,
                              'period':info[i].period,
                              'price':info[i].price,
                              'image':info[i].image_product,
                              'colors':info[i].colors,
                              'cart':0})
                data_set.append(main_data)

            return JsonResponse({'main_data':data_set})


class ProductDetailView(View):
    def get(self, request, id):
        info    = Product_detail.objects.all()
        product = Product.objects.all()
        try:
            token   = request.headers.get('Authorization', None)
            payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
            user    = User.objects.get(id = payload['user'])
            if Cart.objects.filter(product_id=id, user_id=user.id ).exists():
                cart_info = Cart.objects.get(product_id=id, user_id=user.id)
                cart      = cart_info.product_id
             else:
                cart = 0
            num        = id-1
        
            item       = product[num].item
            deco       = product[num].decoration
            icon1      = info[num].icon1
            icon2      = info[num].icon2
            explan     = info[num].explanation
            period     = info[num].period
            price      = info[num].price
            product_id = info[num].product_id
            img_url    = info[num].image_detail
            rest       = info[num].rest
        
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
        except:
            num        = id-1
        
            item       = product[num].item
            deco       = product[num].decoration
            icon1      = info[num].icon1
            icon2      = info[num].icon2
            explan     = info[num].explanation
            period     = info[num].period
            price      = info[num].price
            product_id = info[num].product_id
            img_url    = info[num].image_detail
            rest       = info[num].rest
        
            return JsonResponse({'item' :item,
                                 'deco' :deco,
                                 'icon1':icon1,
                                 'icon2':icon2,
                                 'explanation':explan,
                                 'period':period,
                                 'price' :price,
                                 'product_id':product_id,
                                 'img_url':img_url,
                                 'rest':rest,
                                 'cart':0})

