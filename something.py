https://masterzoo.ua/ua/catalog/koti/korm-dlya-kotv/
https://masterzoo.ua/ua/catalog/koti/lasoshhi-dlya-kotiv/
https://masterzoo.ua/ua/tualeti-ta-aksesuari-dlya-kotiv/
https://masterzoo.ua/ua/napovnuvachi-dlya-kotiv/
https://masterzoo.ua/ua/catalog/koti/vitamini-ta-dobavki-dlya-kotiv/
https://masterzoo.ua/ua/catalog/koti/vetpreparati-dlya-kotiv/
https://masterzoo.ua/ua/catalog/koti/dryapki/
https://masterzoo.ua/ua/catalog/koti/amunczya-dlya-kotv/
https://masterzoo.ua/ua/catalog/koti/aksesuari-dlya-kotv/
https://masterzoo.ua/ua/catalog/koti/doglyad-ta-gigiena-dlya-kotiv/
https://masterzoo.ua/ua/catalog/koti/myak-msczya-dlya-kotv/
https://masterzoo.ua/ua/catalog/koti/grashki-dlya-kotv/
https://masterzoo.ua/ua/catalog/koti/posud-dlya-kotiv/
https://masterzoo.ua/ua/catalog/koti/obladnannya-dlya-kotv/
https://masterzoo.ua/ua/catalog/koti/sumki-perenoski-dlya-kotv/
https://masterzoo.ua/ua/catalog/koti/speczasobi-dlya-kotiv/
https://masterzoo.ua/ua/catalog/koti/odyag-dlya-kotiv/
https://masterzoo.ua/ua/nabori-dlya-kotiv/

https://masterzoo.ua/ua/catalog/sobaki/korm-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/lasoshhi-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/vitamini-ta-dobavki-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/amunczya-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/vetpreparati-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/aksesuari-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/doglyad-ta-gigiena-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/posud-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/myak-msczya-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/grashki-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/odyag-dlya-sobak/
https://masterzoo.ua/ua/avtoaksessuary/
https://masterzoo.ua/ua/catalog/sobaki/pelyushki-tualeti-ta-aksesuari-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/speczasobi-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/sumki-perenoski-dlya-sobak/
https://masterzoo.ua/ua/catalog/sobaki/obladnannya-dlya-sobak/
https://masterzoo.ua/ua/nabori-dlya-sobak/

https://masterzoo.ua/ua/catalog/ptaxi/klitki-dlya-ptahiv/
https://masterzoo.ua/ua/catalog/ptaxi/korm-dlya-ptahiv/
https://masterzoo.ua/ua/catalog/ptaxi/lasoshhi-dlya-ptahiv/
https://masterzoo.ua/ua/catalog/ptaxi/vitamini-ta-vetpreparati-dlya-ptahiv/
https://masterzoo.ua/ua/catalog/ptaxi/godvnicz-dlya-ptaxv/
https://masterzoo.ua/ua/catalog/ptaxi/grashki-dlya-ptaxv/
https://masterzoo.ua/ua/catalog/ptaxi/obladnannya-dlya-ptaxv/
https://masterzoo.ua/ua/catalog/ptaxi/ggnchn-napovnyuvach-dlya-ptaxv/

https://masterzoo.ua/ua/catalog/grizuni/klitki-dlya-grizuniv/
https://masterzoo.ua/ua/catalog/grizuni/korm-dlya-grizuniv/
https://masterzoo.ua/ua/catalog/grizuni/lasoshhi-dlya-grizuniv/
https://masterzoo.ua/ua/catalog/grizuni/vitamini-ta-vetpreparati-dlya-grizuniv/
https://masterzoo.ua/ua/catalog/grizuni/doglyad-ta-gigiena-dlya-grizuniv/
https://masterzoo.ua/ua/catalog/grizuni/grashki-dlya-grizunv/
https://masterzoo.ua/ua/catalog/grizuni/obladnannya-dlya-grizunv/
https://masterzoo.ua/ua/catalog/grizuni/tualeti-napovnyuvach-ta-aksesuari-dlya-grizunv/
https://masterzoo.ua/ua/catalog/grizuni/godvnicz-dlya-grizunv/
https://masterzoo.ua/ua/catalog/grizuni/amunczya-dlya-grizunv/

https://masterzoo.ua/ua/catalog/akvariumistika/akvariumi/
https://masterzoo.ua/ua/catalog/akvariumistika/korm-dlya-rib/
https://masterzoo.ua/ua/catalog/akvariumistika/zasobi-dlya-doglyadu/
https://masterzoo.ua/ua/catalog/akvariumistika/aksesuari/
https://masterzoo.ua/ua/catalog/akvariumistika/dekoracii-dlya-akvariuma/
https://masterzoo.ua/ua/catalog/akvariumistika/osvitlennya/
https://masterzoo.ua/ua/catalog/akvariumistika/pidstavki-ta-piddoni/
https://masterzoo.ua/ua/catalog/akvariumistika/grunti-ta-substrati-dlya-akvariuma/
https://masterzoo.ua/ua/catalog/akvariumistika/filtri/
https://masterzoo.ua/ua/catalog/akvariumistika/kompresori/
https://masterzoo.ua/ua/catalog/akvariumistika/obigrivachi/
https://masterzoo.ua/ua/catalog/akvariumistika/pompi/

https://masterzoo.ua/ua/catalog/terariumistika/terariumi-ta-faunariumi/
https://masterzoo.ua/ua/catalog/terariumistika/korma-harchovi-dobavki-ta-preparati/
https://masterzoo.ua/ua/catalog/terariumistika/ggnchn-napovnyuvach/
https://masterzoo.ua/ua/catalog/terariumistika/obladnannya-dlya-terariuma/
https://masterzoo.ua/ua/catalog/terariumistika/dekoracii-godivnici-groti-dlya-terariuma/


def __str__(self):
    return f'Корзина для {self.user.email} | Продукт: {self.product.name}'

171.33 x 143




class ContactUsView(FormView):
    template_name = 'contact.html'
    model = Contact
    success_url = '/contact-us/'
    form_class = ContactForm

    def form_valid(self, form):
        contact, _ = Contact.objects.get_or_create(
            email=form.cleaned_data['email'],
            defaults={
                'name': form.cleaned_data['name'],
                'message': form.cleaned_data['message']
            }
        )
        send_email(
            subject='Thank you for your message!',
            to_email=[contact.email],
            message=f'Thank you for your message! {contact.name.title()}'
        )
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'message: ' f"Thank you {form.cleaned_data.get('name').upper()} for your massage"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.add_message(
            self.request,
            messages.WARNING,
            form.errors
        )
        return super().form_invalid(form)
