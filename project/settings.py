from .settings_common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]

STATIC_ROOT = "/usr/share/nginx/html/static"
MEDIA_ROOT = "/usr/share/nginx/html/media"

# ロギング設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,  # 既存ロガーを無効化
    # ロガーの設定
    "loggers": {
        # Djangoが利用するロガー
        "django": {"handlers": ["file"], "level": "INFO"},
        # employeesアプリケーションが利用するロガー
        "employees": {"handlers": ["file"], "level": "INFO"},
    },
    # ハンドラの設定
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/django.log"),
            "formatter": "prod",
            "when": "D",  # ログローテーション
            "interval": 1,   # ログローテーション間隔(1日)
            "backupCount": 7,  # 保存しておくログファイル数
        },
    },
    # フォーマッタの設定
    "formatters": {
        "prod": {
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
