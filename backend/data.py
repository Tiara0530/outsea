"""演示样例数据：甲（需求方）+ 供应商 a,b,c,d,e 及各品类竞品。"""

DEMAND_JIA = {
    "id": "D001",
    "buyerId": "jia",
    "product": "主机",
    "components": {
        "主板": "ATX",
        "显卡": "RTX 4060",
        "CPU": "LGA1700",
        "电源": "750W",
        "内存": "DDR5",
    },
    "quantity": 100,
    "deliveryAddress": "德国柏林",
    "budget": 50000,
    "deadline": "2026-12-20",
}

# 每个品类两条供给，让匹配引擎有真实的取舍。
SUPPLIES = [
    {"id": "S001", "supplierId": "a",  "category": "主板", "specs": "ATX B760",       "origin": "深圳", "price": 150, "moq": 50,  "stock": 300, "leadTime": 10},
    {"id": "S006", "supplierId": "a2", "category": "主板", "specs": "M-ATX B660",     "origin": "东莞", "price": 120, "moq": 50,  "stock": 200, "leadTime": 18},
    {"id": "S002", "supplierId": "b",  "category": "显卡", "specs": "RTX 4060 8G",    "origin": "东莞", "price": 280, "moq": 20,  "stock": 200, "leadTime": 8},
    {"id": "S007", "supplierId": "b2", "category": "显卡", "specs": "RTX 4070 12G",   "origin": "深圳", "price": 420, "moq": 20,  "stock": 100, "leadTime": 9},
    {"id": "S003", "supplierId": "c",  "category": "CPU",  "specs": "i7-13700 LGA1700", "origin": "上海", "price": 320, "moq": 10, "stock": 150, "leadTime": 12},
    {"id": "S008", "supplierId": "c2", "category": "CPU",  "specs": "i9-13900 LGA1700", "origin": "上海", "price": 480, "moq": 10, "stock": 80,  "leadTime": 10},
    {"id": "S004", "supplierId": "d",  "category": "电源", "specs": "750W 金牌",      "origin": "广州", "price": 60,  "moq": 100, "stock": 500, "leadTime": 6},
    {"id": "S009", "supplierId": "d2", "category": "电源", "specs": "650W 铜牌",      "origin": "广州", "price": 45,  "moq": 200, "stock": 600, "leadTime": 20},
    {"id": "S005", "supplierId": "e",  "category": "内存", "specs": "DDR5 32G",       "origin": "深圳", "price": 90,  "moq": 50,  "stock": 400, "leadTime": 7},
    {"id": "S010", "supplierId": "e2", "category": "内存", "specs": "DDR4 32G",       "origin": "深圳", "price": 70,  "moq": 100, "stock": 500, "leadTime": 25},
]
