from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from tastetrek import db
from tastetrek.models import Booking, Event
from tastetrek.forms import BookingForm

bookings_bp = Blueprint('bookings', __name__)


@bookings_bp.route('/history')
@login_required
def history():
    bookings = Booking.query.filter_by(user_id=current_user.id)\
        .order_by(Booking.booking_date.desc()).all()
    return render_template('booking_history.html', bookings=bookings)


@bookings_bp.route('/book/<int:event_id>', methods=['POST'])
@login_required
def book(event_id):
    # Validate event exists and is available for booking
    event = Event.query.get_or_404(event_id)

    if event.status != 'Open':
        flash('This event is not available for booking.', 'danger')
        return redirect(url_for('events.detail', event_id=event.id))

    form = BookingForm()
    if form.validate_on_submit():
        qty = form.quantity.data
        remaining = event.tickets_remaining()

        if qty > remaining:
            flash(f'Sorry, only {remaining} ticket(s) remaining.', 'danger')
            return redirect(url_for('events.detail', event_id=event.id))

        booking = Booking(
            user_id=current_user.id,
            event_id=event.id,
            quantity=qty
        )
        db.session.add(booking)
        db.session.commit()

        if event.tickets_remaining() == 0:
            event.status = 'Sold Out'
            db.session.commit()

        flash(f'Booking confirmed! Order #{booking.id} — {qty} ticket(s) booked.', 'success')
        return redirect(url_for('bookings.confirmation', booking_id=booking.id))

    return redirect(url_for('events.detail', event_id=event.id))


@bookings_bp.route('/confirmation/<int:booking_id>')
@login_required
def confirmation(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.user_id != current_user.id:
        flash('You can only view your own bookings.', 'danger')
        return redirect(url_for('bookings.history'))
    return render_template('booking_confirmation.html', booking=booking)
