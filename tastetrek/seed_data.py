from tastetrek import db
from tastetrek.models import User, Event, Comment, Booking
from werkzeug.security import generate_password_hash
from datetime import date, datetime


def seed_database():
    # Create demo users
    demo_user = User(
        first_name='Alice',
        surname='Wang',
        email='alice@example.com',
        password_hash=generate_password_hash('password123'),
        contact_number='0412 345 678',
        street_address='123 Queen St, Brisbane QLD 4000'
    )
    db.session.add(demo_user)

    demo_user2 = User(
        first_name='Bob',
        surname='Smith',
        email='bob@example.com',
        password_hash=generate_password_hash('password123'),
        contact_number='0423 456 789',
        street_address='456 Edward St, Brisbane QLD 4000'
    )
    db.session.add(demo_user2)

    demo_user3 = User(
        first_name='Carol',
        surname='Chen',
        email='carol@example.com',
        password_hash=generate_password_hash('password123'),
        contact_number='0434 567 890',
        street_address='789 George St, Brisbane QLD 4000'
    )
    db.session.add(demo_user3)
    db.session.flush()

    # Create events
    event1 = Event(
        title='Tokyo Night Market Bites',
        description='Join us for an evening of authentic Asian street food, featuring over 30 vendors. From sizzling yakitori to melt-in-your-mouth takoyaki, our night market brings the best street food right to your city. Live music will run throughout the evening.',
        category='Street Food',
        date=date(2026, 8, 15),
        start_time='18:00',
        end_time='23:00',
        venue='Downtown Square Park, Brisbane',
        capacity=200,
        image_url='https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=600',
        status='Open',
        owner_id=demo_user.id
    )
    db.session.add(event1)

    event2 = Event(
        title='Michelin Star Gala',
        description='A premium 5-course tasting menu prepared by world-renowned chefs. Experience the pinnacle of fine dining with carefully paired wines and exquisite presentations.',
        category='Fine Dining',
        date=date(2026, 9, 10),
        start_time='19:00',
        end_time='22:00',
        venue='The Grand Ballroom, Hilton Brisbane',
        capacity=100,
        image_url='https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=600',
        status='Sold Out',
        owner_id=demo_user.id
    )
    db.session.add(event2)

    event3 = Event(
        title='Sweet Tooth Expo',
        description='The ultimate destination for dessert lovers. Featuring artisanal chocolates, gourmet cakes, handcrafted ice creams, and live pastry demonstrations.',
        category='Desserts & Baking',
        date=date(2026, 5, 10),
        start_time='10:00',
        end_time='18:00',
        venue='Brisbane Convention Centre',
        capacity=300,
        image_url='https://images.unsplash.com/photo-1551024506-0bccd828d307?w=600',
        status='Inactive',
        owner_id=demo_user2.id
    )
    db.session.add(event3)

    event4 = Event(
        title='Korean BBQ Festival',
        description='Grill your way through authentic Korean BBQ with premium cuts and traditional sides. Experience the vibrant culture of Korean street food with music and entertainment.',
        category='Street Food',
        date=date(2026, 10, 5),
        start_time='17:00',
        end_time='22:00',
        venue='South Bank Parklands, Brisbane',
        capacity=250,
        image_url='https://images.unsplash.com/photo-1529193591184-b1d58069ecdd?w=600',
        status='Open',
        owner_id=demo_user2.id
    )
    db.session.add(event4)

    event5 = Event(
        title='Sushi Masterclass',
        description='Learn the art of sushi from master chefs, with fresh ingredients sourced from Japan. This hands-on workshop will teach you everything from rice preparation to perfect rolling techniques.',
        category='Fine Dining',
        date=date(2026, 10, 20),
        start_time='14:00',
        end_time='17:00',
        venue='Culinary Institute, Fortitude Valley',
        capacity=40,
        image_url='https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=600',
        status='Open',
        owner_id=demo_user3.id
    )
    db.session.add(event5)

    event6 = Event(
        title='Tuscany Italian Feast',
        description='A celebration of authentic Italian cuisine featuring pasta, wine, and live music. Enjoy handmade pasta, wood-fired pizzas, and a selection of fine Italian wines.',
        category='Fine Dining',
        date=date(2026, 11, 8),
        start_time='18:30',
        end_time='22:30',
        venue='Riverfront Piazza, New Farm',
        capacity=150,
        image_url='https://images.unsplash.com/photo-1498579150354-977475b7ea0b?w=600',
        status='Cancelled',
        owner_id=demo_user.id
    )
    db.session.add(event6)

    event7 = Event(
        title='Vegan Street Food Carnival',
        description='Discover the best plant-based street food from around the world. From jackfruit tacos to vegan dumplings, this carnival proves that plant-based eating is anything but boring.',
        category='Vegan / Plant-Based',
        date=date(2026, 12, 5),
        start_time='11:00',
        end_time='20:00',
        venue='West End Markets, Brisbane',
        capacity=180,
        image_url='https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600',
        status='Open',
        owner_id=demo_user2.id
    )
    db.session.add(event7)

    event8 = Event(
        title='Breakfast All Day Festival',
        description='Celebrate the most important meal of the day with a festival dedicated entirely to breakfast foods. From fluffy pancakes and crispy bacon to exotic smoothie bowls and gourmet coffee, enjoy breakfast favorites all day long.',
        category='Vegan / Plant-Based',
        date=date(2027, 1, 15),
        start_time='08:00',
        end_time='16:00',
        venue='Riverside Gardens, South Bank',
        capacity=120,
        image_url='https://images.unsplash.com/photo-1504754524776-8f4f37790ca0?w=600',
        status='Open',
        owner_id=demo_user3.id
    )
    db.session.add(event8)

    event9 = Event(
        title='Chocolate Wonderland',
        description='A paradise for chocolate lovers. Explore artisanal chocolate makers from around the world, participate in tasting workshops, and watch live chocolate sculpting demonstrations. Pure indulgence awaits.',
        category='Desserts & Baking',
        date=date(2027, 2, 14),
        start_time='10:00',
        end_time='19:00',
        venue='Brisbane City Hall',
        capacity=250,
        image_url='https://images.unsplash.com/photo-1549007994-cb92caebd54b?w=600',
        status='Open',
        owner_id=demo_user.id
    )
    db.session.add(event9)

    db.session.flush()

    # Add some bookings
    booking1 = Booking(
        user_id=demo_user.id,
        event_id=event2.id,
        quantity=2,
        booking_date=datetime(2026, 6, 15, 10, 30)
    )
    db.session.add(booking1)

    booking2 = Booking(
        user_id=demo_user.id,
        event_id=event3.id,
        quantity=1,
        booking_date=datetime(2026, 4, 20, 14, 15)
    )
    db.session.add(booking2)

    booking3 = Booking(
        user_id=demo_user2.id,
        event_id=event1.id,
        quantity=3,
        booking_date=datetime(2026, 7, 1, 9, 0)
    )
    db.session.add(booking3)

    # Add some comments
    comment1 = Comment(
        user_id=demo_user.id,
        event_id=event1.id,
        content='I attended last year and the takoyaki was amazing. Can\'t wait for this one!',
        created_at=datetime(2026, 7, 2, 15, 30)
    )
    db.session.add(comment1)

    comment2 = Comment(
        user_id=demo_user3.id,
        event_id=event1.id,
        content='Looking forward to trying the new vendors this year!',
        created_at=datetime(2026, 7, 3, 10, 15)
    )
    db.session.add(comment2)

    comment3 = Comment(
        user_id=demo_user2.id,
        event_id=event5.id,
        content='This sounds incredible. I\'ve always wanted to learn proper sushi techniques!',
        created_at=datetime(2026, 7, 1, 12, 0)
    )
    db.session.add(comment3)

    db.session.commit()
