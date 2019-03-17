# API Docs
## Listing data format
| Name | Type | Required | Example |
| ---- | ---- | -------- | ----------- |
| `area_unit` | enum | true| SqFt|
| `bathrooms` | float | false| 2.0|
| `bedrooms` | float | false| 4|
| `home_size` | float | false| 1372|
| `home_type` | enum | true| SingleFamily|
| `last_sold_date` | date | false| 2018-08-07 |
| `last_sold_price` | string | false| 123 |
| `link` | url string | true| https://www.zillow.com/homedetails/.../|
| `price` | string | false|  $739K|
| `property_size` | float | false| 10611|
| `rent_price` | float | false| 123 |
| `rentzestimate_amount` | float | false| 2850|
| `rentzestimate_last_updated` | date | false| 2018-08-07|
| `tax_value` | float | false| 215083.0|
| `tax_year` | float | false| 2017|
| `year_built` | float | false| 1956|
| `zestimate_amount` | float | false| 709630|
| `zestimate_last_updated` | date | false| 2018-08-07|
| `zillow_id` | string | true| 19866015|
| `address` | string | true| 7417 Quimby Ave|
| `city` | string | true|  West Hills|
| `state` | string | true| CA|
| `zipcode` | string | true| 91307|
### area_unit enum
Availble: `SqFt`
### home_type enum
Available: `SingleFamily`, `VacantResidentialLand`, `MultiFamily2To4`, `Duplex`, `Condominium`, `Apartment`, `Miscellaneous`

---

## Pagination
By default the result is paged at `size=10` and the link to next page is provided in the response.
Example: `/api/v1/listings?page=4` will get you the results on page 4, i.e. the 31-40 rows
## API suffix
The api supports a suffix in the form of `.json|api` or `?format=api|json` and the server will return either a JSON blob or a browsable api.

---

## GET /api/v1/listings
Get the list of listings.

## POST /api/v1/listings
Create a new listing. Body should follow the Listing object format.

---

## GET /api/v1/listings/:id
Get the listing with primary key <:id>.

## PUT /api/v1/listings/:id
## PATCH /api/v1/listings/:id
Update the listing at primary key <:id>. Body should follow the Listing object format.

## DELETE /api/v1/listings/:id
Remove the listing at primary key <:id>.

