# -*- coding: utf-8 -*-
from django import forms
from models import Post, Auction, Photo, Tag
import re

class WritePostForm(forms.Form):

    title = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': u'제목'}
        )
    )

    product_condition = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': u'상품 상태'}
        )
    )

    transaction_place = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': u'거래 장소'}
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': u'상품 설명'}
        )
    )

    tags = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': u'태그'}
        )
    )
    
    original_price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': u'상품 원가'}
        )
    )

    immediate_price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': u'즉시구매가'}
        )
    )
    
    starting_price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': u'경매 시작가'}
        )
    )

    photo = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(WritePostForm, self).__init__(*args, **kwargs)
        self.fields['title'].error_messages = {'required': u"제목을 입력해주세요."}
        self.fields['product_condition'].error_messages = {'required': u"상품 상태를 입력해주세요."}
        self.fields['transaction_place'].error_messages = {'required': u"거래 장소를 입력해주세요."}
        self.fields['description'].error_messages = {'required': u"상품 설명을 입력해주세요."}
        self.fields['original_price'].error_messages = {'required': u"원가를 입력해주세요."}
        self.fields['starting_price'].error_messages = {'required': u"경매시작가를 입력해주세요."}
        self.fields['photo'].error_messages = {'required': u"사진을 등록해주세요."}

    def write(self, request):
        title = self.cleaned_data.get('title')
        product_condition = self.cleaned_data.get('product_condition')
        transaction_place = self.cleaned_data.get('transaction_place')
        description = self.cleaned_data.get('description')
        raw_tags = self.cleaned_data.get('tags')
        # title / product condition / transaction place / description / tags / original price / immediate price / starting price / photo     
        original_price = self.cleaned_data.get('original_price')
        immediate_price = self.cleaned_data.get('immediate_price')
        starting_price = self.cleaned_data.get('starting_price')
        photo = self.cleaned_data.get('photo')

        auction = Auction(
            product_condition=product_condition,
            original_price=original_price,
            immediate_price=immediate_price,
            starting_price=starting_price,
            current_price=starting_price,
            transaction_place=transaction_place)
        auction.save()
        
        post = Post(
            title=title, description=description,
            user=request.user, auction=auction)
        post.save()

        tags = re.compile('[, ]+').split(raw_tags)
        for tag in set(tags):
            tag_model, created = Tag.objects.get_or_create(name=tag)
            post.tags.add(tag_model)

        photo = Photo(post=post, image_file=photo)
        photo.save()

        return post
