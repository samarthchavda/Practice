{
    'name': 'Mini Sales Order System',
    'description': 'mini sales order system',
    'version': '1.0',
    'depends':['base'],
    'data':[
        "views/order.xml",
        "views/order_line.xml",
        "views/delivery.xml",
        "views/invoice.xml",
        "views/quotation.xml",
        "security/ir.model.access.csv",
    ],
    'application':True,
    'installable':True,
}