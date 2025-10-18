from spamirai_dataset_common import DataItem, Dataset, dataset_paths
from telegram import Update
from telegram.constants import ReactionEmoji
from telegram.ext import ContextTypes

from ..config import config

dataset = Dataset(dataset_paths.get_dataset_layer_path(config.dataset_layer_name))


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != config.super_admin_id:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="You are not the super admin! 🚷",
        )

        return

    data_item = DataItem(
        update.message.text or update.message.caption,
        config.default_label,
        config.default_source,
    )

    added = dataset.add(data_item)

    await context.bot.set_message_reaction(
        chat_id=update.effective_chat.id,
        message_id=update.message.message_id,
        reaction=[ReactionEmoji.FIRE if added else ReactionEmoji.OK_HAND_SIGN],
    )
