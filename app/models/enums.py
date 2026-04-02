import enum

class UserRole(str, enum.Enum):
    ADMIN="ADMIN"
    ANALYST="ANALYST"
    VIEWER="VIEWER"

class RecordType(str, enum.Enum):
    INCOME="INCOME"
    EXPENSE="EXPENSE"