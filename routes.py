# giveforgood/routes.py

from flask import render_template, redirect, url_for, flash
from giveforgood import app, db
from giveforgood.models import Donation  # <-- MODIFIED: Removed ContactMessage
from giveforgood.forms import DonationForm  # <-- MODIFIED: Removed ContactForm

@app.route('/')
@app.route('/index')
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html', title='About Us')

# --- ADD THIS NEW GALLERY ROUTE ---
@app.route('/gallery')
def gallery():
    """Renders the gallery page."""
    # For now, we'll pass a dummy list of image URLs.
    # Later, you could load these from your database or a folder.
    image_list = [
        "https://media.licdn.com/dms/image/v2/D4E22AQEAfxmst8RLhQ/feedshare-shrink_1280/B4EZgyoU1tGwAw-/0/1753196092206?e=2147483647&v=beta&t=6pZEBJRw9DLOEdidPd_9lDmFX_ACzSb8xqUq2jSIn1k",
        "https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?q=80&w=1740&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1599059813005-11265ba4b4ce?q=80&w=1740&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1518398046578-83b75435e695?q=80&w=1740&auto=format&fit=crop"
    ]
    return render_template('gallery.html', title='Gallery', images=image_list)
# ------------------------------------

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    """Renders the donation page and handles form submission."""
    form = DonationForm()
    if form.validate_on_submit():
        # The form data (including form.message.data) is valid!
        # We will add the logic to save this to the database in Step 4.
        flash(f'Thank you, {form.name.data}, for your generous donation of ${form.amount.data}!', 'success')
        return redirect(url_for('home'))
        
    return render_template('donate.html', title='Donate', form=form)

# --- DELETE THE ENTIRE /contact ROUTE BELOW ---
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     ...
#     ...