class CategoryMapping:
    def __init__(self):
        self.category_mapping = {
            'Super': 'Health',
            'Ali Butcher': 'Atha',
            'Best Kingsland Butchers': 'Atha',
            'M R D F': 'Atha',
            'Middleton Rawdo Gfoods': 'Atha',
            'Natures Menu': 'Atha',
            'Park Pets': 'Atha',
            'Rover': 'Atha',
            'To Ana Maria Carvajal Londoño': 'Atha',
            'Cash at Autovia Tarragona Reus': 'Cash',
            'Cash at Hfx  Hackney': 'Cash',
            'Cash at Notemachine': 'Cash',
            'Economy Cash': 'Cash',
            'Remitly': 'Credit',
            'To Juan Sebastian Giraldo Mejia': 'Credit',
            'Depositing savings': 'Depositing savings',
            'Payment from Doshi App Limited': 'Doshi',
            '365 T 111': 'Food Out',
            'Apothecary East': 'Food Out',
            'Babsang': 'Food Out',
            'Beigel Shop': 'Food Out',
            'BLACK SHEEP coffee': 'Food Out',
            'Bouillon Pigalle': 'Food Out',
            'Camden Market': 'Food Out',
            'Casetta di Trastevere': 'Food Out',
            'Chai Guys': 'Food Out',
            'Cheema Brother London': 'Food Out',
            'Ciardi Bar Ristorante': 'Food Out',
            'Ckfoodvegan': 'Food Out',
            'Costa Coffee': 'Food Out',
            'Dishoom': 'Food Out',
            'Eatviet': 'Food Out',
            'El Tresor De La Lolita': 'Food Out',
            'Eurest Virgin Media Griff': 'Food Out',
            'Eventist Group': 'Food Out',
            'Five Guys': 'Food Out',
            'Flesh And Buns': 'Food Out',
            'Ftc Chiswick Gb124': 'Food Out',
            'German Doner': 'Food Out',
            'Gordo?s Pizzeria': 'Food Out',
            'Govinda\'s': 'Food Out',
            'Green Leaf Café': 'Food Out',
            'Hai Cafe': 'Food Out',
            'Hai Cafe Hai Cafe': 'Food Out',
            'Harrods': 'Food Out',
            'HAUS San Vicente': 'Food Out',
            'Hibachi Salad': 'Food Out',
            'Homeland Hunan': 'Food Out',
            'Honest Burgers': 'Food Out',
            'honest greens': 'Food Out',
            'House Of Momo': 'Food Out',
            'I Thai': 'Food Out',
            'Ineos Enterprises Gren': 'Food Out',
            'Italiamos': 'Food Out',
            'J B Food Store': 'Food Out',
            'Jamones Martinez': 'Food Out',
            'Kayra Food': 'Food Out',
            'Kebab Zero': 'Food Out',
            'Khanom Krok': 'Food Out',
            'La Parrilla': 'Food Out',
            'L\'Antico Forno di Piazza Trevi': 'Food Out',
            'Liberty Global': 'Food Out',
            'loaf of bread': 'Food Out',
            'My Neighbours the Dumplings - Clapton': 'Food Out',
            'Non Solo Pizza': 'Food Out',
            'PAUL': 'Food Out',
            'Pitta Souvlaki': 'Food Out',
            'Pizza Union': 'Food Out',
            'Pizza Union Dalston': 'Food Out',
            'Porteña': 'Food Out',
            'Pret': 'Food Out',
            'RASA': 'Food Out',
            'Renfe': 'Travel',
            'Rotisserie': 'Food Out',
            'Shake Shack': 'Food Out',
            'Spice Mountain': 'Food Out',
            'Spizza': 'Food Out',
            'Starbucks': 'Food Out',
            'Streat Latin': 'Food Out',
            'The Bagel House': 'Food Out',
            'The Best Turkish Kebab': 'Food Out',
            'The Canons Gait': 'Food Out',
            'The Sweet Collab': 'Food Out',
            'Three Bowls': 'Food Out',
            'To Maria Camila Ballesteros Rodriguez': 'Food Out',
            'Tongue & Brisket': 'Food Out',
            'Tonkotsu': 'Food Out',
            'Tortilla': 'Food Out',
            'Trattoria da Augusto': 'Food Out',
            'UCHI': 'Food Out',
            'unbounce.com': 'Food Out',
            'Urban Falafel': 'Food Out',
            'Wok to Walk': 'Food Out',
            'Yard Sale Pizza': 'Food Out',
            'Zest Kitchen': 'Food Out',
            'ALDI': 'Groceries',
            'Benugo': 'Groceries',
            'Carrefour': 'Groceries',
            'Casey S': 'Groceries',
            'Casey?s': 'Groceries',
            'Coop': 'Groceries',
            'Co-op': 'Groceries',
            'Fair Deal ': 'Groceries',
            'Fair Deal Foodstore London': 'Groceries',
            'Frituur frans Hooiaard': 'Groceries',
            'Grenade': 'Groceries',
            'Hoxton Fruit and Veg': 'Groceries',
            'Londis': 'Groceries',
            'Marks & Spencer': 'Groceries',
            'Nabinagar Alimentare ..': 'Groceries',
            'Palm 2': 'Groceries',
            'Planet Organic': 'Groceries',
            'Sainsbury\'s': 'Groceries',
            'Shops cashback for Grenade': 'Groceries',
            'Tasty S Supermarket': 'Groceries',
            'Tesco': 'Groceries',
            'Boots': 'Health',
            'E Street Barbers': 'Health',
            'E Street Barbers Ldn': 'Health',
            'Farmacia Nuria Taberner': 'Health',
            'Holland & Barrett': 'Health',
            'Legend Hair Studio': 'Health',
            'Superdrug': 'Health',
            'The Legend Barber': 'Health',
            'To investment account': 'Investment',
            'From LAURA VILLARRAGA ALBINO': 'Laura',
            'To LAURA VILLARRAGA ALBINO': 'Laura',
            'To Laura Villarraga Albino': 'Savings',
            'Basepoint': 'Stratesys',
            'Printful': 'Doshi',
            '107': 'Pubs & Drinks',
            'Angel Comedy L': 'Pubs & Drinks',
            'Arepa &': 'Pubs & Drinks',
            'Arepa And Co Oslo Hack': 'Pubs & Drinks',
            'Bar Dona': 'Pubs & Drinks',
            'Bar Frattina': 'Pubs & Drinks',
            'Bath And Nort East Somers': 'Pubs & Drinks',
            'Beer Merchants Tap': 'Pubs & Drinks',
            'Benugo': 'Pubs & Drinks',
            'BFI Southbank': 'Pubs & Drinks',
            'Birdcage': 'Pubs & Drinks',
            'Blondies': 'Pubs & Drinks',
            'Blondies Brewery': 'Pubs & Drinks',
            'Chelsea Football Club': 'Pubs & Drinks',
            'Chelsea Potter': 'Pubs & Drinks',
            'Corrochio\'s Dalston': 'Pubs & Drinks',
            'Crate Brewery': 'Pubs & Drinks',
            'Crooked Billet': 'Pubs & Drinks',
            'Crown And Castle': 'Pubs & Drinks',
            'Dalston Eastern Curve Gar': 'Pubs & Drinks',
            'Duke of Wellington': 'Pubs & Drinks',
            'Dukeofhammersmith': 'Pubs & Drinks',
            'Earth (evolutionary Ar': 'Pubs & Drinks',
            'Efc Stoke Newington': 'Pubs & Drinks',
            'El Puestu': 'Pubs & Drinks',
            'Elephants Head': 'Pubs & Drinks',
            'Food & Wine': 'Pubs & Drinks',
            'Greene King': 'Pubs & Drinks',
            'Greene King Brewing &': 'Pubs & Drinks',
            'Greenwood Food & Wine': 'Pubs & Drinks',
            'Grosvenor Wines': 'Pubs & Drinks',
            'Grow': 'Pubs & Drinks',
            'Grow Cook Eat': 'Pubs & Drinks',
            'Grow Well': 'Pubs & Drinks',
            'Hackney Church Brew C': 'Pubs & Drinks',
            'Hackney Whole Foods': 'Groceries',
            'Hnd House': 'Pubs & Drinks',
            'Hoop & Toy': 'Pubs & Drinks',
            'James Joyce s.c.r.l.': 'Pubs & Drinks',
            'Juju\'s Bar and Stage': 'Pubs & Drinks',
            'Khans Of Kensington': 'Pubs & Drinks',
            'La Pollera Col': 'Pubs & Drinks',
            'La Pollera Colora': 'Pubs & Drinks',
            'La Quincave': 'Pubs & Drinks',
            'Let\'s Do This': 'Pubs & Drinks',
            'London Coctail Club': 'Pubs & Drinks',
            'London Theatre Direct': 'Pubs & Drinks',
            'Ls Conservatory Archi': 'Pubs & Drinks',
            'Mare Street Market': 'Pubs & Drinks',
            'Marlusse et lapin': 'Pubs & Drinks',
            'Mercato Metropolitano': 'Pubs & Drinks',
            'Nags Head': 'Pubs & Drinks',
            'Newington Green Pubs': 'Pubs & Drinks',
            'Number 90': 'Pubs & Drinks',
            'O2 Forum Kentish Town': 'Pubs & Drinks',
            'Oake Entertainmen': 'Pubs & Drinks',
            'Oslo': 'Pubs & Drinks',
            'Phonox': 'Pubs & Drinks',
            'PowerHaus': 'Pubs & Drinks',
            'Princess of Wales': 'Pubs & Drinks',
            'Red Hand': 'Pubs & Drinks',
            'Red Lion': 'Pubs & Drinks',
            'Rio Cinema': 'Pubs & Drinks',
            'Rosa\'s Carnaby': 'Pubs & Drinks',
            'Rose & Crown': 'Pubs & Drinks',
            'Shakespeares Head': 'Pubs & Drinks',
            'Shuk London': 'Pubs & Drinks',
            'Skylight - Rooftop Bar': 'Pubs & Drinks',
            'Sophie\'s': 'Pubs & Drinks',
            'Swan': 'Pubs & Drinks',
            'Sweet Thursday': 'Pubs & Drinks',
            'Taberna del Bierzo': 'Pubs & Drinks',
            'Terraza New Cuco\'s': 'Pubs & Drinks',
            'The Alma': 'Pubs & Drinks',
            'The Alpaca': 'Pubs & Drinks',
            'The Bull': 'Pubs & Drinks',
            'The Clapton Hart': 'Pubs & Drinks',
            'The Colonel Fawcett': 'Pubs & Drinks',
            'The Crooked Billet': 'Pubs & Drinks',
            'The Crown and Shuttle': 'Pubs & Drinks',
            'The Crown Tavern': 'Pubs & Drinks',
            'The George & Dragon': 'Pubs & Drinks',
            'The Hawley Arms': 'Pubs & Drinks',
            'The Jago': 'Pubs & Drinks',
            'The Market Place': 'Pubs & Drinks',
            'The Old Blue Last': 'Pubs & Drinks',
            'The Shacklewell Arms': 'Pubs & Drinks',
            'The Star By Hackney Downs': 'Pubs & Drinks',
            'The Steam Passage': 'Pubs & Drinks',
            'The Stonehenge Inn': 'Pubs & Drinks',
            'The Sun Tavern': 'Pubs & Drinks',
            'The Victoria': 'Pubs & Drinks',
            'The Willow': 'Pubs & Drinks',
            'To Angelica Fajardo Osorio': 'Pubs & Drinks',
            'To FELIPE GUTIERREZ RE': 'Pubs & Drinks',
            'To Julian Rojas Garcia - Reyes': 'Pubs & Drinks',
            'To NICCOLO UMBERTO J DELLALBA': 'Pubs & Drinks',
            'Trullo': 'Pubs & Drinks',
            'Via Emilia Shoreditch': 'Food Out',
            'Victory Mansion': 'Pubs & Drinks',
            'Village Underground': 'Pubs & Drinks',
            'We Are': 'Pubs & Drinks',
            'Youngs': 'Pubs & Drinks',
            'Payment from Lina Orhiunu': 'Rent',
            'To Lina Orhiunu': 'Rent',
            'Amazon Prime': 'Services',
            'British Gas': 'Services',
            'gov.uk': 'Services',
            'Lb Hackney Parking': 'Services',
            'OpenAI': 'Services',
            'Payment from Lina Orhiunu': 'Services',
            'Spotify': 'Services',
            'Thames Water': 'Services',
            'Voxi': 'Services',
            'Amazon': 'Shopping',
            'Argos': 'Shopping',
            'Ash News': 'Shopping',
            'Boots': 'Health',
            'Brussels Gifts': 'Shopping',
            'La Belgique Gourmande': 'Shopping',
            'London3day.com': 'Shopping',
            'Mailboxes': 'Shopping',
            'Millennium Point': 'Shopping',
            'Mm E&c': 'Shopping',
            'Mygraduationclip': 'Shopping',
            'National Hygiène Group': 'Shopping',
            'Pages Of Hackney': 'Shopping',
            'PBS Int': 'Atha',
            'Post Office': 'Shopping',
            'Qmul Co Ma32': 'Shopping',
            'Reef': 'Shopping',
            'Replay Clothing': 'Shopping',
            'Slideshow': 'Shopping',
            'Sportdifferent': 'Shopping',
            'TK Maxx': 'Shopping',
            'To Xavier Montel': 'Shopping',
            'Toolstation': 'Shopping',
            'UNIQLO': 'Shopping',
            'Walther Koening Books': 'Shopping',
            'Waverley Mall': 'Shopping',
            'Westgate Oxford Car Park': 'Shopping',
            'WHSmith': 'Shopping',
            'Wilko': 'Shopping',
            'Payment from Stratesys Technology Solutions Limi': 'Stratesys',
            'Payment from Stratesys Technology Solutions Limited': 'Stratesys',
            'Payment from Third Bridge Group': 'Third Bridge Group',
            'dott': 'Transport',
            'Ferrocarrils de la Generalitat Valenciana': 'Transport',
            'TMB': 'Transport',
            'Transfer to Ana Maria Carvajal Londono refund': 'Transport',
            'Transport for London': 'Transport',
            'Uber': 'Transport',
            'Avianca': 'Travel',
            'Booking': 'Travel',
            'British Airways': 'Travel',
            'Clockwork Pharmacy & Travel Vaccination Clinic': 'Travel',
            'eurostar': 'Travel',
            'Hilton': 'Travel',
            'Hotel Giolitti': 'Travel',
            'jet2.com': 'Travel',
            'kiwi.com': 'Travel',
            'Mobile Locker': 'Travel',
            'Moxy Hotels': 'Travel',
            'Ryanair': 'Travel',
            'Shell': 'Travel',
            'sitbusshuttle.com': 'Travel',
            'Southern Railway Web': 'Travel',
            'Stansted Express': 'Travel',
            'Trainline': 'Travel',
            'Victoria Station': 'Travel',
            'Weezevent': 'Travel',
            'World Duty Free': 'Travel',
            'Withdrawing savings': 'Withdrawing savings'
        }

    def get_category(self, description):
        for key, value in self.category_mapping.items():
            if description == key:
                return value
        return 'Not Defined'