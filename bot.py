import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

MAIN_MENU = [
    [
        InlineKeyboardButton("🚩 중계거래", callback_data="trade"),
        InlineKeyboardButton("💎 제휴문의", callback_data="partner"),
    ],
    [
        InlineKeyboardButton("💎 박제문의", callback_data="report"),
        InlineKeyboardButton("📢 본방입장", url="https://t.me/+xRuYdxF8P7U3ZjVl"),
    ],
    [
        InlineKeyboardButton("📣 제휴채널", url="https://t.me/NOIRETEAM24"),
        InlineKeyboardButton("📞 상담원연결", callback_data="support"),
    ],
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 전업커 고객센터봇에 오신걸 환영합니다.\n\n"
        "원하시는 메뉴를 아래 버튼을 통해 눌러주세요."
    )

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(MAIN_MENU),
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "trade":
        keyboard = [
            [InlineKeyboardButton("🏠 메인으로", callback_data="home")]
        ]

        await query.edit_message_text(
            "🚩 중계거래 신청\n\n거래 상대방 아이디를 입력해주세요.\n예시 : @username",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "partner":
        keyboard = [
            [InlineKeyboardButton("💰 제휴 가격 안내", callback_data="price")],
            [InlineKeyboardButton("🏠 메인으로", callback_data="home")],
        ]

        await query.edit_message_text(
            "💎 제휴문의\n\n업종을 선택하시면 양식을 안내해드립니다.",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "report":
        keyboard = [
            [InlineKeyboardButton("문의하기", url="https://t.me/Blood_8888")],
            [InlineKeyboardButton("🏠 메인으로", callback_data="home")],
        ]

        await query.edit_message_text(
            "💎 박제문의\n\n문의 : @Blood_8888",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "support":
        keyboard = [
            [InlineKeyboardButton("📞 @NOIRE_TEAM", url="https://t.me/NOIRE_TEAM")],
            [InlineKeyboardButton("🏠 메인으로", callback_data="home")],
        ]

        await query.edit_message_text(
            "전업커 상담텔레 아래로 연락 주시면\n보다 자세히 상담 도와드리겠습니다.",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "home":
        await query.edit_message_text(
            "👋 전업커 고객센터봇에 오신걸 환영합니다.\n\n원하시는 메뉴를 아래 버튼을 통해 눌러주세요.",
            reply_markup=InlineKeyboardMarkup(MAIN_MENU),
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()


if __name__ == "__main__":
    main()
