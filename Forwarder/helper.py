from Forwarder.vars import db
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def generate_settings():
    from_channel = db.get('FROM')
    to_channel = db.get('TO')
    from_msg = db.get('FROM_MSG')
    to_msg = db.get('TO_MSG')
    all = db.get('ALL')
    photo = db.get('PHOTO')
    video = db.get('VIDEO')
    audio = db.get('AUDIO')
    text = db.get('TEXT')
    document = db.get('DOCUMENT')
    tag = db.get('TAG')

    if from_msg == '0':
        from_msg = 'First'
    if to_msg == '0':
        to_msg = 'Last'
    if tag == 'copy':
        tag = 'Without Quote'
    else:
        tag = 'With Quote'
    if all == 'true':
        temp = \
        "TEXT       -       ✅\n" \
        "PHOTO      -       ✅\n" \
        "VIDEO      -       ✅\n" \
        "AUDIO      -       ✅\n" \
        "DOCUMENTS  -       ✅"
    else:
        temp = ''
        if text == 'true':
            temp += "TEXT       -       ✅"
        else:
            temp += "TEXT       -       ❌"
        if photo == 'true':
            temp += "\nPHOTO      -       ✅"
        else:
            temp += "\nPHOTO      -       ❌"
        if video == 'true':
            temp += "\nVIDEO      -       ✅"
        else:
            temp += "\nVIDEO      -       ❌"
        if audio == 'true':
            temp += "\nAUDIO      -       ✅"
        else:
            temp += "\nAUDIO      -       ❌"
        if document == 'true':
            temp += "\nDOCUMENTS  -       ✅"
        else:
            temp += "\nDOCUMENTS  -       ❌"

    text = f"""<b>Details:</b>
<code>From : {from_channel}</code>
<code>To   : {to_channel}</code>

<b>Settings:</b>
<code>From Msg  :   {from_msg}</code>
<code>To Msg    :   {to_msg}</code>

<code>FORWARD   :   {tag}</code>

<code>{temp}</code>"""
    return text


def generate_settings_btns():
    from_msg = db.get('FROM_MSG')
    to_msg = db.get('TO_MSG')
    tag = db.get('TAG')
    all = db.get('ALL')
    photo = db.get('PHOTO')
    video = db.get('VIDEO')
    audio = db.get('AUDIO')
    text = db.get('TEXT')
    document = db.get('DOCUMENT')
    btn = []

    if from_msg == '0':
        btn.append(
            [InlineKeyboardButton('From Msg : First',callback_data='toogle_settings|First')]
        )
    else:
        btn.append(
            [InlineKeyboardButton(f'From Msg : {from_msg}', callback_data='toogle_settings|First')]
        )
    if to_msg == '0':
        btn[0].append(
            InlineKeyboardButton('To Msg : Last',callback_data='toogle_settings|Last')
        )
    else:
        btn[0].append(
            InlineKeyboardButton(f'To Msg : {to_msg}', callback_data='toogle_settings|Last')
        )
    if tag == 'copy':
        btn.append(
            [InlineKeyboardButton('Forward : Without Quote', callback_data='toogle_settings|Tag')]
        )
    else:
        btn.append(
            [InlineKeyboardButton('Forward : With Quote', callback_data='toogle_settings|Tag')]
        )
    if all == 'true':
        btn.append(
            [
                InlineKeyboardButton('TEXT', callback_data='NoneBtn'),
                InlineKeyboardButton('✅', callback_data='toogle_settings|Text')
            ]
        )
        btn.append(
            [
                InlineKeyboardButton('PHOTO', callback_data='NoneBtn'),
                InlineKeyboardButton('✅', callback_data='toogle_settings|Photo')
            ]
        )
        btn.append(
            [
                InlineKeyboardButton('VIDEO', callback_data='NoneBtn'),
                InlineKeyboardButton('✅', callback_data='toogle_settings|Video')
            ]
        )
        btn.append(
            [
                InlineKeyboardButton('AUDIO', callback_data='NoneBtn'),
                InlineKeyboardButton('✅', callback_data='toogle_settings|Audio')
            ]
        )
        btn.append(
            [
                InlineKeyboardButton('DOCUMENT', callback_data='NoneBtn'),
                InlineKeyboardButton('✅', callback_data='toogle_settings|Docs')
            ]
        )
    else:
        if text == 'true':
            btn.append(
                [
                    InlineKeyboardButton('TEXT', callback_data='NoneBtn'),
                    InlineKeyboardButton('✅', callback_data='toogle_settings|Text')
                ]
            )
        else:
            btn.append(
                [
                    InlineKeyboardButton('TEXT', callback_data='NoneBtn'),
                    InlineKeyboardButton('❌', callback_data='toogle_settings|Text')
                ]
            )
        if photo == 'true':
            btn.append(
                [
                    InlineKeyboardButton('PHOTO', callback_data='NoneBtn'),
                    InlineKeyboardButton('✅', callback_data='toogle_settings|Photo')
                ]
            )
        else:
            btn.append(
                [
                    InlineKeyboardButton('PHOTO', callback_data='NoneBtn'),
                    InlineKeyboardButton('❌', callback_data='toogle_settings|Photo')
                ]
            )
        if video == 'true':
            btn.append(
                [
                    InlineKeyboardButton('VIDEO', callback_data='NoneBtn'),
                    InlineKeyboardButton('✅', callback_data='toogle_settings|Video')
                ]
            )
        else:
            btn.append(
                [
                    InlineKeyboardButton('VIDEO', callback_data='NoneBtn'),
                    InlineKeyboardButton('❌', callback_data='toogle_settings|Video')
                ]
            )
        if audio == 'true':
            btn.append(
                [
                    InlineKeyboardButton('AUDIO', callback_data='NoneBtn'),
                    InlineKeyboardButton('✅', callback_data='toogle_settings|Audio')
                ]
            )
        else:
            btn.append(
                [
                    InlineKeyboardButton('AUDIO', callback_data='NoneBtn'),
                    InlineKeyboardButton('❌', callback_data='toogle_settings|Audio')
                ]
            )
        if document == 'true':
            btn.append(
                [
                    InlineKeyboardButton('DOCUMENT', callback_data='NoneBtn'),
                    InlineKeyboardButton('✅', callback_data='toogle_settings|Docs')
                ]
            )
        else:
            btn.append(
                [
                    InlineKeyboardButton('DOCUMENT', callback_data='NoneBtn'),
                    InlineKeyboardButton('❌', callback_data='toogle_settings|Docs')
                ]
            )
    btn.append(
        [
            InlineKeyboardButton('ALL ✅', callback_data='toogle_settings|All'),
            InlineKeyboardButton('NONE ❌', callback_data='toogle_settings|None')
        ]
    )
    btn.append([InlineKeyboardButton(text='Back', callback_data='save_settings')])
    return InlineKeyboardMarkup(btn)

def all_checker():
    photo = db.get('PHOTO')
    video = db.get('VIDEO')
    audio = db.get('AUDIO')
    text = db.get('TEXT')
    document = db.get('DOCUMENT')

    if photo == video == audio == text == document == 'true':
        db.put('ALL','true')
    else:
        db.put('ALL','false')