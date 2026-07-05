from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from tastetrek import db
from tastetrek.models import Event, Comment
from tastetrek.forms import EventForm, CommentForm, BookingForm
from datetime import date

events_bp = Blueprint('events', __name__)


@events_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            title=form.title.data.strip(),
            description=form.description.data.strip(),
            category=form.category.data,
            date=form.date.data,
            start_time=form.start_time.data.strip(),
            end_time=form.end_time.data.strip(),
            venue=form.venue.data.strip(),
            capacity=form.capacity.data,
            image_url=form.image_url.data.strip() if form.image_url.data else '',
            status='Open',
            owner_id=current_user.id
        )
        db.session.add(event)
        db.session.commit()
        flash('Event created successfully!', 'success')
        return redirect(url_for('events.detail', event_id=event.id))

    return render_template('create_event.html', form=form, date=date)


@events_bp.route('/my-events')
@login_required
def my_events():
    events = Event.query.filter_by(owner_id=current_user.id)\
        .order_by(Event.date.desc()).all()
    return render_template('my_events.html', events=events, date=date)


@events_bp.route('/<int:event_id>')
def detail(event_id):
    # Auto-update expired events to Inactive
    Event.update_statuses()

    event = Event.query.get_or_404(event_id)
    comment_form = CommentForm()
    booking_form = BookingForm()
    return render_template('event_details.html', event=event, comment_form=comment_form,
                           booking_form=booking_form, date=date)


@events_bp.route('/<int:event_id>/comment', methods=['POST'])
@login_required
def add_comment(event_id):
    event = Event.query.get_or_404(event_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            user_id=current_user.id,
            event_id=event.id,
            content=form.content.data.strip()
        )
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been posted!', 'success')
    else:
        flash('Comment cannot be empty.', 'danger')
    return redirect(url_for('events.detail', event_id=event.id))


@events_bp.route('/<int:event_id>/update', methods=['GET', 'POST'])
@login_required
def update(event_id):
    event = Event.query.get_or_404(event_id)
    if event.owner_id != current_user.id:
        abort(403)

    form = EventForm(obj=event)
    if form.validate_on_submit():
        event.title = form.title.data.strip()
        event.description = form.description.data.strip()
        event.category = form.category.data
        event.date = form.date.data
        event.start_time = form.start_time.data.strip()
        event.end_time = form.end_time.data.strip()
        event.venue = form.venue.data.strip()
        event.capacity = form.capacity.data
        event.image_url = form.image_url.data.strip() if form.image_url.data else ''
        db.session.commit()
        flash('Event updated successfully!', 'success')
        return redirect(url_for('events.detail', event_id=event.id))

    return render_template('update_event.html', form=form, event=event, date=date)


@events_bp.route('/<int:event_id>/cancel', methods=['POST'])
@login_required
def cancel(event_id):
    event = Event.query.get_or_404(event_id)
    if event.owner_id != current_user.id:
        abort(403)
    event.status = 'Cancelled'
    db.session.commit()
    flash('Event has been cancelled.', 'info')
    return redirect(url_for('events.detail', event_id=event.id))
