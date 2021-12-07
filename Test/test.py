keyid ='rzp_test_7kHkeo0zJIug0H'
keySecret='qYJb59p9O99UfZP9YUTooBJi'

import razorpay
client = razorpay.Client(auth=(keyid, keySecret))

#checkout
data = {
	'amount' : 100*100,
	"currency" : "INR",
	"receipt" : "Feelfreetocode123",
	"notes" : {
	    "name" : "Ritika" ,
	    "Payment_for" : "Python Course"
	}
}

# server orderid
order = client.order.create(data=data)
print(order)




#{'id': 'order_IUdds8E3Edpt4P', 'entity': 'order', 'amount': 10000, 'amount_paid': 0, 'amount_due': 10000, 'currency': 'INR', 'receipt': 'Feelfreetocode123', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': {'name': 'Ritika', 'Payment_for': 'Python Course'}, 'created_at': 1638891768}