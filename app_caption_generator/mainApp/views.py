from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import ImageData
from datetime import date
from django.conf import settings

# Create your views here.
from mainApp.vit_prediction import vit

# load home.html
@csrf_protect
@csrf_exempt
def home(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']

        # saving the image
        p_file_path = f"static/storage/{image_file.name}"
        with open(p_file_path, 'wb') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        # make prediction
        p_description = vit.predict(p_file_path)

        # Save data to the database
        image_data = ImageData(
            create_time=date.today(),
            description=p_description,
            file_path=p_file_path
        )                
                        
        # save data in table
        image_data.save()

        return JsonResponse({
            'success': True, 
            'file_path': p_file_path,
            'description': p_description
    })

    return render(request, 'home.html')


# load report.html
def report(request):
    # take data from database
    image_data = ImageData.objects.all()

    if request.method == 'POST':
        # take id_image from ajax
        p_id_image = request.POST.get('id_filtered')        
        
        # query the row with corresponding id
        try:
            image_obj = ImageData.objects.get(id_image=p_id_image)
            p_file_path = image_obj.file_path
            p_description = image_obj.description
            print('file: ', p_file_path)
            print('description: ', p_description)

            return JsonResponse({
                'file_path': p_file_path,
                'description': p_description
            })
        
        except ImageData.DoesNotExist:
            print('Image not found for id_image:', p_id_image)
            return JsonResponse({'file_path': None, 'description': None})

    return render(request, 'report.html', {'image_data': image_data})
