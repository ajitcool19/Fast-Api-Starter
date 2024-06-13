import sentry_sdk
from common.config.config import current_config

def init_sentry():
    sentry_sdk.init(
        dsn= current_config.SENTRY_DSN,
        traces_sample_rate=current_config.TRACES_SAMPLE_RATE,
        profiles_sample_rate=current_config.PROFILES_SAMPLE_RATE,
    )