from os import system
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login, logout
from datetime import datetime,time, timedelta

from .decorator import *
from .form import *
from .models import *
# Create your views here.

@unauthenticated_user
def userlogin(request):
    if request.POST:
        users = get_user_model()
        usermail = request.POST.get('username')
        if not usermail:
            return redirect('login')
        user, created = users.objects.get_or_create(email = usermail)
        login(request,user)
        if user.is_staff == True:
            return redirect('admin_dash')
        return redirect('home')
    return render(request,'login.html')

def userlogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url="login")
def home(request):
    auctions = auctionItem.objects.all()
    return render(request,'dashboard.html',{'auctions':auctions,'chk':True})

@admin_only
def admin_dash(request):
    bid = bids.objects.all()
    auctions = auctionItem.objects.all()
    User = get_user_model()
    users = User.objects.all()
    total_users = users.count()
    total_bids = bid.count()
    total_auctions = auctions.count()
    bid_value = 0
    for b in bid:
        bid_value+=b.bid_price
    
    active_auction_value=0
    for auction in auctions:
        today = datetime.now()
        end_date = str(auction.end_date)
        date = str(today.strftime("%Y-%m-%d"))
        date = datetime.strptime(date,'%Y-%m-%d')
        end_date = datetime.strptime(end_date,'%Y-%m-%d')
        diff = end_date-date
        if diff.seconds>0 or diff.days>0:
            if auction.max_bid>0:
                active_auction_value+=auction.max_bid
            else:
                active_auction_value+=auction.min_bid

    context = {'users':users,'total_users':total_users,'bids':total_bids,'auctions':auctions,'total_auctions':total_auctions,'bid_val':bid_value,'auc_val':active_auction_value}
    return render(request,'admin_dashboard.html',context)


@login_required(login_url="login")
def userAuctions(request):
    user = request.user
    auctions = auctionItem.objects.filter(user=user)
    return render(request,'dashboard.html',{'auctions':auctions,'chk':False})

@login_required(login_url="login")
def AddAuction(request):
    form = AuctionForm
    if request.method=='POST':
        form = AuctionForm(request.POST, request.FILES)
        if form.is_valid():
            auction = form.save(commit = False)
            auction.user = request.user
            auction.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'add_auction.html',context)

def bid(request,id):
    auction = auctionItem.objects.get(id=id)
    max_bid = auction.max_bid
    all_bids = bids.objects.filter(auction=auction)
    if request.POST:
        bid_price = float(request.POST.get('bid'))
        if bid_price>max_bid:
            auction.max_bid = bid_price
            auction.bid_winner = request.user.email
            max_bid = bid_price
            auction.save()
        new_bid,created = bids.objects.get_or_create(user = request.user, auction=auction)
        new_bid.bid_price = bid_price
        new_bid.save()
    try:
        userbid = bids.objects.get(user=request.user,auction=auction)
        userbid = userbid.bid_price
    except:
        userbid=None
    today = datetime.now()
    today = today-timedelta(days=1)
    end_date = str(auction.end_date)
    date = str(today.strftime("%Y-%m-%d"))
    date = datetime.strptime(date,'%Y-%m-%d')
    end_date = datetime.strptime(end_date,'%Y-%m-%d')
    diff = end_date-date
    print(date)
    print(end_date)
    print(diff)
    if diff.seconds>0 or diff.days>0:
        diff = True
    else:
        diff = False
    return render(request,'bid.html',{'auction':auction,'all_bids':all_bids,'max_bid':max_bid,'diff':diff,'userbid':userbid})
