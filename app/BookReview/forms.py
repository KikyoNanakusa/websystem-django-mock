from django import forms
from .models import Review
from .models import User
from django.contrib.auth import authenticate


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'evaluation_point']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'evaluation_point': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }
        labels = {
            'title': 'レビューのタイトル',
            'content': 'レビュー内容',
            'evaluation_point': '評価点 (1〜5)',
        }


class LoginForm(forms.Form):
    email = forms.EmailField(label='メールアドレス', max_length=100)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError("メールアドレスまたはパスワードが正しくありません。")
        cleaned_data['user'] = user  # 認証済みユーザーを保存
        return cleaned_data


class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'パスワード'}),
        label="パスワード"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'パスワード（確認用）'}),
        label="パスワード（確認用）"
    )

    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '名前'}),
            'email': forms.EmailInput(attrs={'placeholder': 'メールアドレス'}),
        }
        labels = {
            'name': '名前',
            'email': 'メールアドレス',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("パスワードが一致しません。")
        return cleaned_data
