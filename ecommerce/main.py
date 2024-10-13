# Initialize ProductSearcher and SearchProductAPI
from apis.search_product_api import SearchProductAPI
from data.filter_details import FilterDetails
from data.rating import Rating
from searcher.product_searcher import ProductSearcher


product_searcher = ProductSearcher()
search_api = SearchProductAPI(product_searcher)

filter_details = FilterDetails(price_filter=1000.0, rating_filter=Rating.FOUR, pay_on_del_filter=True)

result = search_api.search("Product", filter_details)

# Display the result
print("Filtered Search Results:")
for product in result:
    print(f"ID: {product.id}, Name: {product.name}, Description: {product.description}, "
          f"Price: {product.price_in_inr}, Rating: {product.rating.get_val()}, "
          f"Pay on Delivery: {'Yes' if product.is_pay_on_delivery else 'No'}")
