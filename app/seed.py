from app.core.database import SessionLocal
from app.models.user import User
from app.models.enums import UserRole
from app.core.security import hash_password


def seed_users():
    db = SessionLocal()

    existing_admin = db.query(User).filter(User.email == "admin@example.com").first()
    if existing_admin:
        print("Admin user already exists.")
        db.close()
        return

    users = [
        User(
            name="Admin User",
            email="admin@example.com",
            password_hash=hash_password("Admin123"),
            role=UserRole.ADMIN,
            is_active=True
        ),
        User(
            name="Analyst User",
            email="analyst@example.com",
            password_hash=hash_password("Analyst123"),
            role=UserRole.ANALYST,
            is_active=True
        ),
        User(
            name="Viewer User",
            email="viewer@example.com",
            password_hash=hash_password("Viewer123"),
            role=UserRole.VIEWER,
            is_active=True
        )
    ]

    db.add_all(users)
    db.commit()
    db.close()

    print("Seed users created successfully.")


if __name__ == "__main__":
    seed_users()