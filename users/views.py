# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth import login 
from django.contrib.auth.views import PasswordChangeView, PasswordResetView

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserUpdateView(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'update.html'

    # This keeps users from accessing the profile of other users.
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(id=user.id)

class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('home')
    template_name = 'change_password.html'

class UserPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('login')
    template_name = 'reset_password.html'

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})
