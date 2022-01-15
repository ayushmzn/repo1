from datetime import date, timedelta
def fun(y):
    d=date(y,1,1)
    first_sun_date=d+timedelta(days=7-d.isoweekday())
    while first_sun_date.year == y:
        yield first_sun_date
        first_sun_date=first_sun_date+timedelta(days=7)        
y=int(input("enter a year"))
pd=fun(y)
for i in pd:
    print(i)
