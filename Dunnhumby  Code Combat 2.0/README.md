### DunnHumby
* company wants to reward its loyal customers by giving them a heavy discount on the products they buy repeatedly.
* The objective of this project is to allocate the most relevant set of products to each customer by maximizing total relevancy. For More detials visit Output File [Submission File](https://github.com/AI-kartheek/Python-Projects/blob/main/Dunnhumby%20%20Code%20Combat%202.0/Output%20File/Dunnhumby_Submission_file.csv)

* By satysfing all constraints we got Total **Relevancy Score =** `` 1088.9439968840002`` 

### Constraints: 
* 1. Due to budget constraints, there is fixed volume of each product. For instance, product``565051`` cannot be allocated to more than **150** customers. For Referrence check [Product - Volume Dataset](https://github.com/AI-kartheek/Python-Projects/blob/main/Dunnhumby%20%20Code%20Combat%202.0/datasets/Products.csv).
* 2. There are some set of products which cannot be assigned together (e.g. product``5649565`` and ``564964`` cannot be given together to any customer). You can get this list in the [Products Exclusion Dataset](https://github.com/AI-kartheek/Python-Projects/blob/main/Dunnhumby%20%20Code%20Combat%202.0/datasets/Exclusion.csv).
* 3. A customer can get **maximum 8** products and **minimum 3** products. **Drop** all the customers who qualify for less than      ``3 products``.
* 4. All the products allocated to a customer should be ``distinct`` (i.e. the same product cannot be allocated twice to the same customer)


