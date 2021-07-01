from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def main(request):
    return redirect('/admin')


def check_in(request, exhibition_url):
    client_id = request.session.get("client_id", -1)

    exhib = get_object_or_404(Exhibition, code=exhibition_url)
    if client_id == -1:
        client = Client.objects.create(exhibitions_visited=1)
        request.session["client_id"] = client.id
    else:
        client = Client.objects.get(id=client_id)

    client.exhibitions.add(exhib)
    exhib_visited = len(client.exhibitions.all())
    client.exhibitions_visited = exhib_visited
    client.save()
    exhib.clients_visited = len(exhib.clients.all())
    exhib.save()

    if exhib_visited > 3:
        return redirect(exhib.link)
    elif exhib_visited == 3:
        client.is_participant = True
        client.generate_special_code()
        client.save()
        return render(request, "win.html", {"client": client,
                                            "client_id": client_id,
                                            "exhib": exhib
                                            })
    return render(request, "check_in.html", {"client": client,
                                             "client_id": client_id,
                                             "exhib": exhib,
                                             "exhib_visited": exhib_visited
                                             })

# Create your views here.
