from django.shortcuts import render
from ..users.models import User
from django.contrib.postgres.search import SearchVector

# Create your views here.
def search_result(request):
    query = request.GET['q']
    user_result = User.objects.annotate(
        search=SearchVector(
            'email',
            'full_name',
            'tags',
        ).filter(search=query)
    )
    if not user_result:
        message = "Mentor "+ query +" not found."
        return render(request, "./search/search_page.html",{
                "message": message,
            })
    else:
        message = "Mentors found: "
        return render(request, "./search/search_page.html",{
            "message": message,
            "user_result": user_result,
            })
