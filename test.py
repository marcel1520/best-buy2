import product_2_step_2
import promotions


'''product_list = [
    product.Product("Laptop", 100, 5),
    product.Product("Mobile", 50, 2),
    product.Product("TVSamsung", 500, 7)
]

for product in product_list:
    print(product.show())
    print(product.get_quantity())
'''

'''# setup initial stock of inventory
product_list = [product_2.Product("MacBook Air M2", price=1450, quantity=100),
                product_2.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                product_2.Product("Google Pixel 7", price=500, quantity=250),
                product_2.NonStockedProduct("Windows License", price=125),
                product_2.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                ]
best_buy = store.Store(product_list)'''



# setup initial stock of inventory
product_list = [ product_2_step_2.Product("MacBook Air M2", price=1450, quantity=100),
                 product_2_step_2.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 product_2_step_2.Product("Google Pixel 7", price=500, quantity=250),
                 product_2_step_2.NonStockedProduct("Windows License", price=125),
                 product_2_step_2.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)