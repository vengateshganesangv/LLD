from dto.product_info_query_dto import ProductInfoQuery
from entity.shop_order import ShopOrder
from manager.abstract_order_manager import AbstractOrderManager

class AmountProcessingManager:
    def payAmountInfo(self, amount_added: float, amountToBePaid: float) -> dict[str,int,int,int]:
        if amount_added == amountToBePaid:
            return {"status": "PAID", "amount_to_refund": 0, "total_amount": amountToBePaid, "amount_added": amount_added}
        elif amount_added > amountToBePaid:
            amountToRefund = amount_added - amountToBePaid
            return {"status":"OVER_PAID", "amount_to_refund": amountToRefund, "total_amount": amountToBePaid, "amount_added": amount_added}
        else:
            underPaidAmount = amountToBePaid - amount_added
            return {"status":"UNDER_PAID", "amount_to_refund": underPaidAmount, "total_amount": amountToBePaid, "amount_added": amount_added}
        
    def processPayment(self, paymentInfoObjet: dict[str,int,int,int], transactionId: int, orderManager: AbstractOrderManager) -> ShopOrder:
        order = orderManager.processOrder(paymentInfoObjet, transactionId)
        return order