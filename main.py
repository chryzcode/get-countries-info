import qrcode
import folium
from countryinfo import CountryInfo

print('Welcome, You can get information about any country here!')

try:
    user = input('\nEnter the name of a country:\n')
    name = user

    country = CountryInfo(name)



    country_name = country.alt_spellings()

    print('\nName:')
    for name in country_name:
        print(name, end= ', ')

    country_capital =country.capital()
    print(f'\n\nCapital:\n{country_capital}')

    country_currency = country.currencies()
    print('\nCurrency:')
    for currency in country_currency:
        print(currency, end= ', ')

    country_lang = country.languages()
    print('\n\nLanguages:')
    for languages in country_lang:
        print(languages, end =', ')

    country_timezone = country.timezones()
    print('\n\nTime-Zone:')
    for timezones in country_timezone:
        print(timezones, end = ', ')

    country_area = country.area()
    print(f'\n\nCountry Area:\n{country_area}')

    country_borders = country.borders()
    print('\nBorders:')
    for border in country_borders:
        print(border, end=', ')

    calling_codes= country.calling_codes()
    print('\n\nCall Code:')
    for call_code in calling_codes:
        print(call_code)

    country_region = country.region()
    print(f'\nRegion:\n{country_region}')

    sub_region = country.subregion()
    print(f'\nSub-Region:\n{sub_region}')

    country_population = country.population()
    print(f'\nPopulation:\n{country_population}')

    country_states = country.provinces()
    print('\nStates/Provinces:')
    for states in country_states:
        print(states, end=', ')

    about_country = country.wiki()

    country_map = country.capital_latlng()
    map = folium.Map(location = (country_map))
    print(f'\n\nCheck your qrcode directory for the map of  {user}, named: (mylocation.html)')
    map.save("./qrcode/location.html")

    about_country = country.wiki()

    data = about_country
    qr = qrcode.QRCode( version = 1, box_size = 15, border = 5)
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    print(f'\nCheck your map directory for the qr code containing the information of {user}, named: (about_country.png)')
    img.save('./map/about_country.png')
except:
    print('Please enter a valid country name!')
    exit()
