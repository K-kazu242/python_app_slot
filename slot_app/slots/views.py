from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Sum
import json

from .models import SlotRecord


# ── 認証 ──────────────────────────────────────

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if not username or not password:
            error = 'ユーザー名とパスワードを入力してください'
        elif password != password2:
            error = 'パスワードが一致しません'
        elif User.objects.filter(username=username).exists():
            error = 'このユーザー名はすでに使われています'
        elif len(password) < 6:
            error = 'パスワードは6文字以上にしてください'
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('index')
    return render(request, 'slots/signup.html', {'error': error})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            error = 'ユーザー名またはパスワードが違います'
    return render(request, 'slots/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


# ── メイン ────────────────────────────────────

@login_required
def index(request):
    today = timezone.localdate()
    return render(request, 'slots/index.html', {'today': today})


@login_required
def save_record(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            amount = int(data.get('amount', 0))
            date = data.get('date', str(timezone.localdate()))
            memo = data.get('memo', '')
            record = SlotRecord.objects.create(
                user=request.user,
                date=date,
                amount=amount,
                memo=memo,
            )
            return JsonResponse({'success': True, 'id': record.id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False}, status=405)


@login_required
def total(request):
    records = SlotRecord.objects.filter(user=request.user)
    total_amount = records.aggregate(total=Sum('amount'))['total'] or 0
    win_count = records.filter(amount__gt=0).count()
    lose_count = records.filter(amount__lt=0).count()
    draw_count = records.filter(amount=0).count()
    total_count = records.count()
    context = {
        'records': records,
        'total_amount': total_amount,
        'win_count': win_count,
        'lose_count': lose_count,
        'draw_count': draw_count,
        'total_count': total_count,
    }
    return render(request, 'slots/total.html', context)


@login_required
def delete_record(request, pk):
    if request.method == 'POST':
        record = get_object_or_404(SlotRecord, pk=pk, user=request.user)
        record.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=405)
