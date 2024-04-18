Users -------> DONE
Category----> 
Product -----> 
Users Company -----> 
Review------> 

store 
    -Category ---> Done
    -Color
    -Size
    -Product
        -user ----> foreign key
        -name
        -slug
        -price
        -size ----> Many
        -color ----> Many
        -description
    -Image Product    
    -Review
        -product
        -user
        -rating
        -comment
    -Offer
        -product
        -discount_precentage
        -start_date    
        -end_date   

-make url for rate_product from product viewset [Done]
-will stop add or update or delete review from review serializer [Done]
- cart Models , serializers and viewsets
-(from product detail)add to cart ---> api/store/product/add_to_cart [Done]
-will add total price in cart [Done]
-Pagination [DONE]
-Order Model and OrderProduct
-Serialize of two models of order
-Added viewsets
-Added Order Completed





