import json

from django.views import View
from django.http import JsonResponse

from .models import Review

class ReviewToPage(View):
    def get(self, request):
        reviews = Review.objects.all()
        data_set=[]

        if request.method == "GET":
            for i in  range(len(reviews)):
                main_data = ({'id':reviews[i].id,
                              'name':reviews[i].name,
                              'purchased_item':reviews[i].purchased_item,
                              'purchased_date':reviews[i].purchased_date,
                              'photo':reviews[i].photo,
                              'comment':reviews[i].comment
                             })
                data_set.append(main_data)
        return JsonResponse({'main_data':data_set})





