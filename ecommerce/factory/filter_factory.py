from data.filter_details import FilterDetails
from filter.idle_filter import IdleFilter
from filter.pay_on_del_filter import PayOnDelFilter
from filter.price_based_filter import PriceBasedFilter
from filter.rating_based_filter import RatingBasedFilter

class FilterFactory:
    @staticmethod
    def get_product_filter(filter_details: FilterDetails):
        filter_instance = IdleFilter()
        if filter_details.rating_filter is not None:
            filter_instance = RatingBasedFilter(filter_details.rating_filter, filter_instance)
        if filter_details.pay_on_del_filter is not None:
            filter_instance = PayOnDelFilter(filter_details.pay_on_del_filter, filter_instance)
        if filter_details.price_filter is not None:
            filter_instance = PriceBasedFilter(filter_details.price_filter, filter_instance)
        return filter_instance
#Iterator Design Pattern -> PriceBasedFilter(filter_details.price_filter, PayOnDelFilter(filter_details.pay_on_del_filter, RatingBasedFilter(filter_details.rating_filter, IdleFilter())))