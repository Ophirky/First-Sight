# Imports
import secrets, os
from PIL import Image
from FirstSight import app
from FirstSight.models import Users
from FirstSight import login_manager

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)
    return picture_fn

@login_manager.user_loader
def load_user(user_id: int):
    return Users.query.get(int(user_id))