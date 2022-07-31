from dataclasses import dataclass
import enum

@dataclass
class Category:
    name: str
    id: str

@enum.unique
class Categories(enum.Enum):
    ELECTRONICS = Category(
        name = 'Electronics',
        id = '01'
    )
    COMPUTERS_MOBILE = Category(
        name = 'Computers-Mobile',
        id = '02'
    )
    APPLIANCES = Category(
        name = 'Appliances',
        id = '03'
    )
    HOME_FURNISHING = Category(
        name = 'Home-Furnishing',
        id = '04'
    )
    KITCHEN_DINING = Category(
        name = 'Kitchen-Dining',
        id = '05'
    )
    SPORTS_OUTDOOR = Category(
        name = 'Sports-Outdoor',
        id = '06'
    )
    GARDEN_FLORAL_PATIO = Category(
        name = 'Garden-Floral-Patio',
        id = '07'
    )
    DIY_HOME_IMPROVEMENT = Category(
        name = 'DIY-Home-Improvement',
        id = '08'
    )
    Health_Beauty = Category(
        name = 'Health-Beauty',
        id = '09'
    )
    BABY_KIDS_TOYS = Category(
        name = 'Baby-Kids-Toys',
        id = '10'
    )
    TIRES_AUTOMOTIVE = Category(
        name = 'Tires-Automotive',
        id = '11'
    )
    CLEANING_LAUNDRY_PET_SUPPLIES_HOUSEHOLD_ESSENTIALS = Category(
        name = 'Cleaning-Laundry-Pet-supplies-Household-Essentials',
        id = '12'
    )
    FOOD_BEVERAGE = Category(
        name = 'Food-Beverage',
        id = '13'
    )
    WINES_LIQUORS = Category(
        name = 'Wines-Liquors',
        id = '14'
    )
    CLOTHING_SHOES_BAGS = Category(
        name = 'Clothing-Shoes-Bags',
        id = '15'
    )
    JEWELRY_WATCHES = Category(
        name = 'Jewelry-Watches',
        id = '16'
    )
    SUNGLASSES_GLASSES_CONTACTS = Category(
        name = 'Sunglasses-Glasses-Contacts',
        id = '17'
    )
    BOOKS_GIFTS_ENTERTAINMENT = Category(
        name = 'Books-Gifts-Entertainment',
        id = '18'
    )
    BUSINESS_OFFICE_SUPPLIES = Category(
        name = 'Business-Office-Supplies',
        id = '19'
    )
    FOR_BUSINESS = Category(
        name = 'For-Business',
        id = '20'
    )
    DROPSHIP_FROZEN_CHILLED_ITEMS = Category(
        name = 'Dropship-Frozen-Chilled-Items',
        id = '21'
    )
    FLORAL = Category(
        name = 'Floral',
        id = '22'
    )
    ORGANIC = Category(
        name = 'Organic',
        id = '23'
    )
    MADE_IN_JAPAN = Category(
        name = 'Made-in-Japan',
        id = '24'
    )

@enum.unique
class Sub_Categories(enum.Enum):
    TV_ACCESSORIES = Category( 
        name = 'TV-Accessories',
        id = '001'
    )
    AUDIO_VIDEO = Category( 
        name = 'Audio-Video',
        id = '002'
    )
    SECURITY_SURVEILLANCE_SYSTEMS = Category( 
        name = 'Security-Surveillance-Systems',
        id = '003'
    )
    CAMERA_VIDEO_CAMERAS_DRONES = Category(
        name = 'Camera-Video-Cameras-Drones',
        id = '004'
    )
    INSTRUMENTS = Category(
        name = 'Instruments',
        id = '005'
    )
    SMART_HOME = Category(
        name = 'Smart-Home',
        id = '006'
    )
    COMPUTERS = Category( 
        name = 'Computers',
        id = '007'
    )
    TABLET = Category(
        name = 'Tablet',
        id = '008'
    )
    PC_ACCESSORIES = Category(
        name = 'PC-Accessories',
        id = '009'
    )
    HARD_DRIVES_MEMORY_CARDS = Category( 
        name = 'Hard-Drives-Memory-Cards',
        id = '010'
    )
    SMARTPHONES_MOBILE_ACCESSORIES = Category(
        name = 'Smartphones-Mobile-Accessories',
        id = '011'
    )
    HEADPHONES_EARPHONES = Category( 
        name = 'Headphones-Earphones',
        id = '012'
    )
    REFRIGERATORS_FREEZERS = Category(
        name = 'Refrigerators-Freezers',
        id = '013'
    )
    WASHERS_CLOTHING_APPLIANCES = Category(
        name = 'Washers-Clothing-Appliances',
        id = '014'
    )
    WINE_CELLAR_COOLERS = Category(
        name = 'Wine-Cellar-Coolers',
        id = '015'
    )
    DISHWASHERS = Category(
        name = 'Dishwashers',
        id = '016'
    )
    COOLING_AIR_TREATMENT_HEATING = Category( 
        name = 'Cooling-Air-Treatment-Heating',
        id = '017'
    )
    COMMERCIAL_APPLIANCES = Category( 
        name = 'Commercial-Appliances',
        id = '018'
    )
    SODA_MAKERS = Category( 
        name = 'Soda-Makers',
        id = '019'
    )
    OVENS_TOASTERS = Category( 
        name = 'Ovens-Toasters',
        id = '020'
    )
    GRILLS_HOT_PLATES = Category( 
        name = 'Grills-Hot-Plates',
        id = '021'
    )
    RICE_PRESSURE_COOKERS = Category( 
        name = 'Rice-Pressure-Cookers',
        id = '022'
    )
    ELECTRIC_KETTLES = Category( 
        name = 'Electric-Kettles',
        id = '023'
    )
    COFFEE_ESPRESSO_MACHINES = Category( 
        name = 'Coffee-Espresso-Machines',
        id = '024'
    )
    BREAD_MACHINES = Category( 
        name = 'Bread-Machines',
        id = '025'
    )
    SPECIALTY_APPLIANCES = Category( 
        name = 'Specialty-Appliances',
        id = '026'
    )
    FOOD_PROCESSORS_MIXERS = Category( 
        name = 'Food-Processors-Mixers',
        id = '027'
    )
    BLENDER_JUICERS = Category( 
        name = 'Blender-Juicers',
        id = '028'
    )
    COFFEE_GRINDERS = Category( 
        name = 'Coffee-Grinders',
        id = '029'
    )
    VACCUM_SEALERS = Category( 
        name = 'Vaccum-Sealers',
        id = '030'
    )
    VACUUMS_FLOOR_CARE = Category( 
        name = 'Vacuums-Floor-Care',
        id = '031'
    )
    SEWING_GARMENT_CARE = Category( 
        name = 'Sewing-Garment-Care',
        id = '032'
    )
    BED_BATH = Category( 
        name = 'Bed-Bath',
        id = '033'
    )
    MATTRESS_BEDROOM_FURNISHING = Category( 
        name = 'Mattress-Bedroom-Furnishing',
        id = '034'
    )
    FURNITURE = Category( 
        name = 'Furniture',
        id = '035'
    )
    HOME_DECOR = Category( 
        name = 'Home-Decor',
        id = '036'
    )
    STORAGE_LAUNDRY = Category(
        name = 'Storage-Laundry',
        id = '037'
    )
    CURTAINS_BLINDS = Category( 
        name = 'Curtains-Blinds',
        id = '038'
    )
    INDOOR_LIGHTING = Category( 
        name = 'Indoor-Lighting',
        id = '039'
    )
    RELIGIOUS_DECOR = Category(
        name = 'Religious-Decor',
        id = '040'
    )
    DINING = Category( 
        name = 'Dining',
        id = '041'
    )
    KITCHEN = Category( 
        name = 'Kitchen',
        id = '042'
    )
    FITNESS_EXERCISE = Category( 
        name = 'Fitness-Exercise',
        id = '043'
    )
    CAMPING = Category( 
        name = 'Camping',
        id = '044'
    )
    BICYCLES_SCOOTERS = Category( 
        name = 'Bicycles-Scooters',
        id = '045'
    )
    SPORTS_OUTDOOR = Category( 
        name = 'Sports-Outdoor',
        id = '046'
    )
    GAME_ROOM = Category(
        name = 'Game-Room',
        id = '047'
    )
    WATER_SPORTS = Category(
        name = 'Water-Sports',
        id = '048'
    )
    BINOCULARS = Category(
        name = 'Binoculars',
        id = '049'
    )
    SPA_SAUNA = Category(
        name = 'Spa-Sauna',
        id = '050'
    )
    WINTER_SPORTS = Category( 
        name = 'Winter-Sports',
        id = '051'
    )
    BBQ = Category( 
        name = 'BBQ',
        id = '052'
    )
    PATIO_FURNITURE = Category(
        name = 'Patio-Furniture',
        id = '053'
    )
    SHEDS_BARNS = Category(
        name = 'Sheds-Barns',
        id = '054'
    )
    OUTDOOR_LIGHTING = Category(
        name = 'Outdoor-Lighting',
        id = '055'
    )
    GARDEN_STRUCTURES = Category(
        name = 'Garden-Structures',
        id = '056'
    )
    GARDEN_ACCESSORIES = Category(
        name = 'Garden-Accessories',
        id = '057'
    )
    OUTDOOR_POWER_EQUIPMENT = Category( 
        name = 'Outdoor-Power-Equipment',
        id = '058'
    )
    FLORAL = Category( 
        name = 'Floral',
        id = '059'
    )
    DECKS_FENCING = Category( 
        name = 'Decks-Fencing',
        id = '060'
    )
    LIGHTING = Category(
        name = 'Lighting',
        id = '061'
    )
    DISASTER_PREPAREDNESS = Category( 
        name = 'Disaster-Preparedness',
        id = '062'
    )
    SECURITY_CRIME_PREVENTION = Category( 
        name = 'Security-Crime-Prevention',
        id = '063'
    )
    BATHROOM_HARDWARE = Category( 
        name = 'Bathroom-Hardware',
        id = '064'
    )
    TOOLS_HARDWARE = Category( 
        name = 'Tools-Hardware',
        id = '065'
    )
    PORTABLE_BATTERIES_STORAGE_BATTERIES = Category(
        name = 'Portable-Batteries-Storage-Batteries',
        id = '066'
    )
    BEAUTY_CARE = Category(
        name = 'Beauty-Care',
        id = '067'
    )
    PERSONAL_CARE_GOODS = Category(
        name = 'Personal-Care-Goods',
        id = '068'
    )
    PERSONAL_CARE_APPLIANCES = Category( 
        name = 'Personal-Care-Appliances',
        id = '069'
    )
    VITAMINS_SUPPLEMENTS = Category(
        name = 'Vitamins-Supplements',
        id = '070'
    )
    DIET_NUTRITION = Category( 
        name = 'Diet-Nutrition',
        id = '071'
    )
    HEALTH_CARE = Category( 
        name = 'Health-Care',
        id = '072'
    )
    HYGIENE = Category( 
        name = 'Hygiene',
        id = '073'
    )
    MASSAGE_RELAXATION = Category( 
        name = 'Massage-Relaxation',
        id = '074'
    )
    TOYS_PICTURE_BOOKS = Category( 
        name = 'Toys-Picture-Books',
        id = '075'
    )
    BABY_CARRIERS = Category( 
        name = 'Baby-Carriers',
        id = '076'
    )
    DIAPERS_WIPES = Category( 
        name = 'Diapers-Wipes',
        id = '077'
    )
    FORMULA = Category( 
        name = 'Formula',
        id = '078'
    )
    BED_BATH_PRODUCTS = Category( 
        name = 'Bed-Bath-Products',
        id = '079'
    )
    NURSERY_BABY_FURNITURE = Category( 
        name = 'Nursery-Baby-Furniture',
        id = '080'
    )
    OTHER_BABY_GOODS = Category( 
        name = 'Other-Baby-Goods',
        id = '081'
    )
    KIDS_BABY_APPAREL = Category(
        name = 'Kids-Baby-Apparel',
        id = '082'
    )
    CAR_ACCESSORIES = Category( 
        name = 'Car-Accessories',
        id = '083'
    )
    GARAGE_ACCESSORIES = Category( 
        name = 'Garage-Accessories',
        id = '084'
    )
    WASH_WAX = Category(
        name = 'Wash-Wax',
        id = '085'
    )
    CAR_MAINTENANCE = Category( 
        name = 'Car-Maintenance',
        id = '086'
    )
    PAPER_GOODS = Category(
        name = 'Paper-Goods',
        id = '087'
    )
    CLEANING_LAUNDRY_PRODUCTS = Category(
        name = 'Cleaning-Laundry-Products',
        id = '088'
    )
    PET_SUPPLIES = Category(
        name = 'Pet-Supplies',
        id = '089'
    )
    BATTERIES = Category(
        name = 'Batteries',
        id = '090'
    )
    KITCHEN_SUNDRIES = Category(
        name = 'Kitchen-Sundries',
        id = '091'
    )
    CHOCOLATE = Category(
        name = 'Chocolate',
        id = '092'
    )
    COOKIES_BISCUIT = Category(
        name = 'Cookies-Biscuit',
        id = '093'
    )
    SNACKS = Category( 
        name = 'Snacks',
        id = '094'
    )
    RICE_CONFECTIONERY = Category(
        name = 'Rice-Confectionery',
        id = '095'
    )
    GUM_CANDY = Category( 
        name = 'Gum-Candy',
        id = '096'
    )
    COFFEE_TEA = Category(
        name = 'Coffee-Tea',
        id = '097'
    )
    WATER_BEVERAGES = Category(
        name = 'Water-Beverages',
        id = '098'
    )
    PANTRY_DRY_GOODS = Category(
        name = 'Pantry-Dry-Goods',
        id = '099'
    )
    DROPSHIP_FROZEN_CHILLED_ITEMS = Category(
        name = 'Dropship-Frozen-Chilled-Items',
        id = '100'
    )
    WINE = Category(
        name = 'Wine',
        id = '101'
    )
    SPIRITS = Category(
        name = 'Spirits',
        id = '102'
    )
    BEER = Category(
        name = 'Beer',
        id = '103'
    )
    MENS_CLOTHING = Category(
        name = 'Mens-Clothing',
        id = '104'
    )
    WOMENS_CLOTHING = Category(
        name = 'Womens-Clothing',
        id = '105'
    )
    CHILDRENS_CLOTHING = Category(
        name = 'Childrens-Clothing',
        id = '106'
    )
    BAGS = Category( 
        name = 'Bags',
        id = '107'
    )
    LUGGAGE = Category(
        name = 'Luggage',
        id = '108'
    )
    PURSES_WALLETS_CARD_HOLDERS = Category(
        name = 'Purses-Wallets-Card-Holders',
        id = '109'
    )
    JEWELRY = Category( 
        name = 'Jewelry',
        id = '110'
    )
    WATCHES = Category( 
        name = 'Watches',
        id = '111'
    )
    SUNGLASSES = Category( 
        name = 'Sunglasses',
        id = '112'
    )
    GLASSES = Category( 
        name = 'Glasses',
        id = '113'
    )
    CONTACT_LENSES = Category( 
        name = 'Contact-Lenses',
        id = '114'
    )
    GIFT_CARDS_TICKETS = Category(
        name = 'Gift-Cards-Tickets',
        id = '115'
    )
    JAPANESE_BOOKS = Category( 
        name = 'Japanese-Books',
        id = '116'
    )
    FOREIGN_LANGUAGE_BOOKS = Category(
        name = 'Foreign-Language-Books',
        id = '117'
    )
    FOOD_GIFTS = Category(
        name = 'Food-Gifts',
        id = '118'
    )
    FLOWER_GIFTS = Category(
        name = 'Flower-Gifts',
        id = '119'
    )
    JANITORIAL_BREAKROOM_SUPPLIES = Category( 
        name = 'Janitorial-Breakroom-Supplies',
        id = '120'
    )
    STORAGE_EQUIPMENT = Category( 
        name = 'Storage-Equipment',
        id = '121'
    )
    PAPER = Category(
        name = 'Paper',
        id = '122'
    )
    BASIC_OFFICE_SUPPLIES = Category(
        name = 'Basic-Office-Supplies',
        id = '123'
    )
    OFFICE_ELECTRONICS = Category(
        name = 'Office-Electronics',
        id = '124'
    )
    DIGITAL_STATIONARY = Category(
        name = 'Digital-Stationary',
        id = '125'
    )
    WRITING_SUPPLIES = Category(
        name = 'Writing-Supplies',
        id = '126'
    )
    FILING_STORAGE = Category(
        name = 'Filing-Storage',
        id = '127'
    )
    MAILING_PACKING_SHIPPING = Category(
        name = 'Mailing-Packing-Shipping',
        id = '128'
    )
    OFFICE_FURNITURE = Category(
        name = 'Office-Furniture',
        id = '129'
    )
    SCHOOL_SUPPLIES_HOBBY_CRAFTS = Category(
        name = 'School-Supplies-Hobby-Crafts',
        id = '130'
    )
    BUSINESS_COMMERCIAL_APPLIANCES = Category(
        name = 'Commercial-Appliances',
        id = '131'
    )
    BULK_ORDER_PALLET_DELIVERY = Category( 
        name = 'Bulk-Order-Pallet-Delivery',
        id = '132'
    )