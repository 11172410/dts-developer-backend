from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create a simple message for the index of the api
@api_view()
def home_route(request):
    return Response(
        {"message": "This is the homepage of the DTS developer challenge API."}
    )
