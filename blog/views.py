from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from django.template.context_processors import csrf
import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="use_your_merchant_id",
                                  public_key="use_your_public_key",
                                  private_key="use_your_private_key")



def post_list(request):
  posts = Post.objects.all()
  return render(request, 'blog/post_list.html', { 'posts': posts })

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post_detail.html', { 'post': post })

def checkout(request):
    nonce = request.POST["payment_method_nonce"]
    result = braintree.Transaction.sale({
       "amount": "11.00",
       "payment_method_nonce": nonce
    })
    
    return HttpResponse(result.message)

