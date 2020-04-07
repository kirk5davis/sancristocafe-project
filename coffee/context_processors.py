from coffee.models import Banner

def banner_info(request):
    try:
        return {'banner': Banner.objects.all().first()}
    except Banner.DoesNotExist:
        {'banner': None}