{
    'name': 'Mini Sales Order System',
    'description': 'mini sales order system',
    'version': '1.0',
    'depends':['base'],
    'data':[
        "security/ir.model.access.csv",
        "views/order.xml",
        "views/order_line.xml",
        "views/delivery.xml",
        "views/invoice.xml",
        "views/quotation.xml",
        "views/payment.xml",
        "views/product.xml",
    ],
    'application':True,
    'installable':True,
}