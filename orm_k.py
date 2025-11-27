from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

Base = declarative_base()


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(500))
    created_at = Column(DateTime, default=datetime.now)

    users = relationship("User", back_populates="department")
    tasks = relationship("Task", back_populates="department")

    def __repr__(self):
        return f"<Department(name='{self.name}')>"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(String(20), default='user')
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

    created_at = Column(DateTime, default=datetime.now)

    department = relationship("Department", back_populates="users")

    tasks = relationship("Task", back_populates="assigned_user")

    def __repr__(self):
        return f"<User(login='{self.login}', department='{self.password}'), role='{self.role}' >"


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(String(1000))
    deadline = Column(Date)

    assigned_to_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

    status_id = Column(Integer, ForeignKey('task_statuses.id'), default=1)
    status_ref = relationship("TaskStatus", back_populates="tasks")
    created_at = Column(DateTime, default=datetime.now)

    assigned_user = relationship("User", back_populates="tasks")
    department = relationship("Department", back_populates="tasks")

    def __repr__(self):
        return f"<Task(title='{self.title}', deadline={self.deadline}, department='{self.department.name}')>"


class UserLog(Base):
    __tablename__ = 'user_logs'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    action = Column(String(200), nullable=False)  # 'login', 'create_task', etc.
    created_at = Column(DateTime, default=datetime.now)

    user = relationship("User")


class TaskStatus(Base):
    __tablename__ = 'task_statuses'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    tasks = relationship("Task", back_populates="status_ref")

engine = create_engine('sqlite:///deadline_manager.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
default_statuses = ['active', 'completed', 'cancelled']
for status_name in default_statuses:
    if not session.query(TaskStatus).filter_by(name=status_name).first():
        session.add(TaskStatus(name=status_name))
session.commit()
session.close()


