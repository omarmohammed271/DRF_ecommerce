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