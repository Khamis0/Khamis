


__help__ = """- /tr (language code) as reply to a long message.
"""
__mod_name__ = "Google Translate"

dispatcher.add_handler(DisableAbleCommandHandler("tr", do_translate, pass_args=True))
