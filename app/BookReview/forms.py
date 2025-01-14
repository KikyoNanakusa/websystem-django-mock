from django import forms
from .models import Review


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
    """ログイン用フォーム"""
    email = forms.EmailField(
        label="メールアドレス",
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'メールアドレスを入力してください'
        })
    )
    password = forms.CharField(
        label="パスワード",
        max_length=128,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'パスワードを入力してください'
        })
    )
