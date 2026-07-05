from flask import Blueprint, render_template, request, flash
from tastetrek.models import Event
from datetime import date

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    # Auto-update expired events to Inactive
    Event.update_statuses()

    category = request.args.get('category', '')
    search = request.args.get('search', '')

    query = Event.query

    if category:
        query = query.filter_by(category=category)

    if search:
        query = query.filter(Event.title.ilike(f'%{search}%') |
                             Event.description.ilike(f'%{search}%') |
                             Event.venue.ilike(f'%{search}%'))

    events = query.order_by(Event.date.desc()).all()
    categories = ['Street Food', 'Fine Dining', 'Desserts & Baking', 'Vegan / Plant-Based']

    return render_template('index.html', events=events, categories=categories,
                           selected_category=category, search=search, date=date)


@main_bp.route('/csrf-error')
def csrf_error():
    flash('Session expired or invalid form. Please try again.', 'danger')
    return render_template('index.html', events=[], categories=[],
                           selected_category='', search='', date=date)
