from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


jobstores = {
    'default': SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")
}
scheduler = BackgroundScheduler(jobstores=jobstores)
