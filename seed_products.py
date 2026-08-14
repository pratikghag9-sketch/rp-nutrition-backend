from app import app
from models import db
from models.product import Product

products_data = [
    {"name": "RP Whey Gold Isolate", "category": "whey", "price": 2799, "mrp": 3299, "description": "25g protein, low carb, 1kg", "stock": 50},
    {"name": "RP Whey Classic", "category": "whey", "price": 2199, "mrp": 2599, "description": "24g protein blend, 1kg", "stock": 60},
    {"name": "RP Mass Gainer Pro", "category": "gainer", "price": 2499, "mrp": 2899, "description": "1250 kcal per serving, 3kg", "stock": 30},
    {"name": "RP Serious Gainer XL", "category": "gainer", "price": 3199, "mrp": 3699, "description": "High calorie, 5kg pack", "stock": 20},
    {"name": "RP Pre-Ignite", "category": "preworkout", "price": 1699, "mrp": 1999, "description": "Caffeine + beta-alanine, 300g", "stock": 40},
    {"name": "RP Pump Surge", "category": "preworkout", "price": 1899, "mrp": 2199, "description": "Citrulline focused pump, 250g", "stock": 35},
    {"name": "RP Creatine Monohydrate", "category": "creatine", "price": 899, "mrp": 1099, "description": "Micronized, 250g, unflavoured", "stock": 80},
    {"name": "RP Creatine HCL", "category": "creatine", "price": 1299, "mrp": 1499, "description": "Zero bloat formula, 200g", "stock": 45},
    {"name": "RP BCAA 2:1:1", "category": "bcaa", "price": 1199, "mrp": 1399, "description": "Intra-workout recovery, 300g", "stock": 55},
    {"name": "RP EAA Recover", "category": "bcaa", "price": 1599, "mrp": 1899, "description": "Full essential aminos, 400g", "stock": 25},
    {"name": "RP Multivitamin Daily", "category": "vitamins", "price": 699, "mrp": 849, "description": "60 tablets, complete daily dose", "stock": 70},
    {"name": "RP Omega-3 Fish Oil", "category": "vitamins", "price": 799, "mrp": 949, "description": "1000mg, 90 softgels", "stock": 65},
]

with app.app_context():
    for p in products_data:
        product = Product(**p)
        db.session.add(product)
    db.session.commit()
    print(f"Added {len(products_data)} products!")
