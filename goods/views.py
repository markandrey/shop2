from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Каталог",
        "goods": [
            {
                "name": "Классические шторы",
                "description": "Элегантные шторы из плотного хлопка с традиционным дизайном. Подходят для гостиных и спален.",
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "price": 3499.99,
            },
            {
                "name": "Римские шторы",
                "description": "Практичные и стильные шторы с механизмом подъёма. Идеальны для кухонь и офисов.",
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "price": 4299.50,
            },
            {
                "name": "Японские шторы",
                "description": "Минималистичные панельные шторы с ровными складками. Создают уютную атмосферу.",
                "image": "deps/images/goods/double bed.jpg",
                "price": 5999.00,
            },
            {
                "name": "Рулонные шторы",
                "description": "Удобные шторы с компактным механизмом скручивания. Защищают от солнца.",
                "image": "deps/images/goods/kitchen table.jpg",
                "price": 2899.99,
            },
            {
                "name": "Шторы блэкаут",
                "description": "Полностью блокируют солнечный свет. Отлично подходят для спален.",
                "image": "deps/images/goods/kitchen table 2.jpg",
                "price": 4599.50,
            },
            {
                "name": "Тюлевые шторы",
                "description": "Лёгкие и воздушные шторы, пропускающие мягкий свет. Украшают окна.",
                "image": "deps/images/goods/corner sofa.jpg",
                "price": 1999.99,
            },
            {
                "name": "Деревянные жалюзи",
                "description": "Стильные жалюзи из натурального дерева. Регулируют уровень освещённости.",
                "image": "deps/images/goods/bedside table.jpg",
                "price": 6799.00,
            },
            {
                "name": "Алюминиевые жалюзи",
                "description": "Лёгкие и прочные жалюзи для офисов и квартир. Устойчивы к влаге.",
                "image": "deps/images/goods/corner sofa.jpg",
                "price": 3499.50,
            },
            {
                "name": "Вертикальные жалюзи",
                "description": "Жалюзи с вертикальными ламелями. Удобны для панорамных окон.",
                "image": "deps/images/goods/sofa.jpg",
                "price": 5199.99,
            },
            {
                "name": "Карниз круглый",
                "description": "Прочный металлический карниз с кольцами. Подходит для тяжёлых штор.",
                "image": "deps/images/goods/office chair.jpg",
                "price": 1499.00,
            },
            {
                "name": "Карниз профильный",
                "description": "Современный карниз с незаметным креплением. Идеален для рулонных штор.",
                "image": "deps/images/goods/plants.jpg",
                "price": 2299.50,
            },
            {
                "name": "Карниз струнный",
                "description": "Лёгкий и почти невидимый карниз. Используется для тюлевых штор.",
                "image": "deps/images/goods/flower.jpg",
                "price": 899.99,
            },
            {
                "name": "Подушки декоративные",
                "description": "Мягкие подушки с яркими принтами. Украшают диваны и кровати.",
                "image": "deps/images/goods/strange table.jpg",
                "price": 1299.00,
            },
            {
                "name": "Покрывало стёганое",
                "description": "Тёплое и уютное покрывало для спальни. Доступно в разных размерах.",
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "price": 3499.99,
            },
            {
                "name": "Плед вязаный",
                "description": "Ручная работа из натуральной шерсти. Согревает зимними вечерами.",
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "price": 2799.50,
            },
            {
                "name": "Скатерть льняная",
                "description": "Экологичная скатерть с натуральной фактурой. Подходит для праздничного стола.",
                "image": "deps/images/goods/double bed.jpg",
                "price": 1899.00,
            },
            {
                "name": "Гобелен настенный",
                "description": "Декоративное панно с узорами. Создаёт акцент в интерьере.",
                "image": "deps/images/goods/double bed.jpg",
                "price": 4599.99,
            },
            {
                "name": "Полотенца кухонные",
                "description": "Хлопковые полотенца с высокой впитываемостью. Практичны и долговечны.",
                "image": "deps/images/goods/kitchen table 2.jpg",
                "price": 799.50,
            },
            {
                "name": "Чехлы для мебели",
                "description": "Защищают диваны и кресла от загрязнений. Легко снимаются и стираются.",
                "image": "deps/images/goods/corner sofa.jpg",
                "price": 4999.00,
            },
            {
                "name": "Балдахин для кровати",
                "description": "Романтичный балдахин из лёгкой ткани. Создаёт уют в спальне.",
                "image": "deps/images/goods/kitchen table.jpg",
                "price": 3599.99,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
