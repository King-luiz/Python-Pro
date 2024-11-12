#pip install CountryInfo

from countryinfo import CountryInfo
country = CountryInfo(input("Enter country Name :\n"))

#various information about country

print("Country Name : ", country.name())
print("Capital Name : ", country.capital())
print("Population : ", country.population())
print("Area (in square meters): ", country.area())
print("Region :", country.region())
print("Subregion : ", country.subregion())
print("Demonym : ", country.demonym())
print("Currency : ", country.currencies())
print("Languages : ", country.languages())
print("Borders : ", country.borders())
#code_with_luiz


