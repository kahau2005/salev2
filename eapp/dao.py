from eapp.models import Category, Product

def load_categories():
    return Category.query.all()
def load_products(category_id=None, kw=None):
    query = Product.query
    if kw:
        query = query.filter(Product.name.contains(kw))
    if category_id:
        query = query.filter(Product.category_id.__eq__(category_id))
    return query.all()