from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .helpers import return_context


@login_required
def search_view_entry(request):
    """
    react detail view for tearsheet matching id
    """

    if request.method == "GET":

        context = return_context(request)
        asset_path = '/app/react_views/r_search/templates/r_search/search/dist/assets/'

        return render(request, "r_search/search/dist/index.html", {"context": context, 'asset_path': asset_path})
