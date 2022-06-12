from .settings_common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ロギング設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,  # 既存ロガーを無効化
    # ロガーの設定
    "loggers": {
        # Djangoが利用するロガー
        "django": {"handlers": ["console"], "level": "INFO"},
        # employeesアプリケーションが利用するロガー
        "employees": {"handlers": ["console"], "level": "DEBUG"},
    },
    # ハンドラの設定
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "dev",
        },
    },
    # フォーマッタの設定
    "formatters": {
        "dev": {
            "format": "\t".join(
                [
                    "%(asctime)s",
                    "[%(levelname)s]",
                    "%(pathname)s(Line:%(lineno)d)",
                    "%(message)s",
                ]
            )
        },
    },
}
