from flask import current_app, flash, redirect, url_for
from flask_login import login_required, current_user

from app.model.base import db
from app.model.gift import Gift
from . import web


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            db.session.add(gift)
            current_user.beans += float(current_app.config['BEANS_UPLOAD_ONE_BOOK'])
    else:
        flash('这本书已添加至赠送清单或已存在心愿清单')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
