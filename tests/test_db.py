from sqlalchemy import select

from fast_api_zero.models import User


def test_create_user(session):
    user = User(
            username='ganjalf',
            email='edson@gmail.com',
            password='135723'
    )

    session.add(user)
    session.commit()

    result = session.scalar(
            select(User).where(User.email == 'edson@gmail.com')
    )

    assert result.username == 'ganjalf'
