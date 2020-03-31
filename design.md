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
