from environs import Env

env = Env()

BOT_TOKEN: str = env.str("BOT_TOKEN", "1724096909:AAGSScHCJ62PD_ZYqAVJhywOZ4iRbixrT2I")
USE_WEBHOOK: bool = env.bool("USE_WEBHOOK", False)
ADMIN_CHAT_ID: str = env.str("ADMIN_CHAT_ID", "@Valdemar41k")
