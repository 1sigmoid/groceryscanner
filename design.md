# Design Essentials

### data structure for scraped prices

Assuming for a commodity, we need a quantity:

rice --> rice 5kg, rice 25kg etc


we use a json / bson / dictionary format

{
    rice 5kg: 
    {
        bigbasket: [day1, day2, day3],
        grofers: [day1, day2, day3]
        pantry: [day1, day2, day3
    }, 

    wheat 25kg:
    {
        ...
        ...
        ...
    }
}



Else, if we decide to go the csv route, maybe simpler, the columns would be

(this is a highly impractical route)

we make a file for each commodity that we search for, and in that we


in rice_5kg.csv

date    bb_price    grofers_price   pantry_price



