from app import app
from flask import render_template, url_for, redirect
from app.forms import PostForm, TitleForm
import datetime


@app.route('/')
@app.route('/index')
@app.route('/index/<title>', methods=['GET', 'POST'])
def index(title=''):
    products = {
        0: {
            'title': 'Soap',
            'price': 3.86,
            'desc': 'Very clean soapy soap stuff that soaps soap.',
            'url': 'http://placehold.it/250x250'
        },
        1: {
            'title': 'Grapes',
            'price': 4.56,
            'desc': 'Grapey grapes with a grapey grape taste.',
            'url': 'http://placehold.it/250x250'
        },
        2: {
            'title': 'Desk',
            'price': 245.99,
            'desc': 'Many drawers to hold desk things, and useful for desk stuff.',
            'url': 'http://placehold.it/250x250'
        },
        3: {
            'title': 'Desk',
            'price': 245.99,
            'desc': 'Many drawers to hold desk things, and useful for desk stuff.',
            'url': 'http://placehold.it/250x250'
        },
        4: {
            'title': 'Desk',
            'price': 245.99,
            'desc': 'Many drawers to hold desk things, and useful for desk stuff.',
            'url': 'http://placehold.it/250x250'
        },
        5: {
            'title': 'Desk',
            'price': 245.99,
            'desc': 'Many drawers to hold desk things, and useful for desk stuff.',
            'url': 'http://placehold.it/250x250'
        },
        6: {
            'title': 'Desk',
            'price': 245.99,
            'desc': 'Many drawers to hold desk things, and useful for desk stuff.',
            'url': 'http://placehold.it/250x250'
        },
        7: {
            'title': 'Desk',
            'price': 245.99,
            'desc': 'Many drawers to hold desk things, and useful for desk stuff.',
            'url': 'http://placehold.it/250x250'
        }
    }
    return render_template('index.html', products=products, title=title)

posts_dict = {
    0: {
        'date': 'Sept. 9th, 2018',
        'name': 'Max',
        'tweet': 'Today I had cereal for breakfast.'
    },
    1: {
        'date': 'July 1st, 2018',
        'name': 'Kelly',
        'tweet': 'Went for a run downtown.'
    },
    2: {
        'date': 'June 21st, 2018',
        'name': 'Max',
        'tweet': 'Got a new job!! Working for the man.'
    },
    3: {
        'date': 'March 4th, 2018',
        'name': 'Kelly',
        'tweet': 'Hiking is fun, get outside.'
    },
    4: {
        'date': 'February 8th, 2018',
        'name': 'Kelly',
        'tweet': 'This is a sample text. This is a sample text.'
    },
    5: {
        'date': 'October 10th, 2017',
        'name': 'Max',
        'tweet': 'This is a sample text. This is a sample text.'
    },
    6: {
        'date': 'October 1st, 2017',
        'name': 'Max',
        'tweet': 'This is a sample text. This is a sample text.'
    },
    7: {
        'date': 'Sept. 31st, 2017',
        'name': 'Kelly',
        'tweet': 'This is a sample text. This is a sample text.'
    }
}

@app.route('/posts/<name>', methods=['GET', 'POST'])
def posts(name = 'Max'):
    form = PostForm()

    people = {
        0: {
            'name': 'Max',
            'age': 26,
            'bio': 'Avid swimmer, cat lover, and I ride a bike everywhere.',
            'url': 'http://placehold.it/250x250'
        },
        1: {
            'name': 'Kelly',
            'age': 21,
            'bio': 'My name is Kelly, I work in Boston and love dogs <3.',
            'url': 'http://placehold.it/250x250'
        }
    }

    if form.validate_on_submit():
        tweet = form.post.data
        date = datetime.datetime.now().date()
        length = len(posts_dict)
        posts_dict[length] = {
            'date': date,
            'name': name,
            'tweet': tweet
        }

    return render_template('posts.html', people=people, name=name, posts=posts_dict, page='posts', form=form)


@app.route('/title', methods=['GET', 'POST'])
def title():
    form2 = TitleForm()

    if form2.validate_on_submit():
        title = form2.title.data
        return redirect(url_for('index', title=title))

    return render_template('title.html', form=form2)
