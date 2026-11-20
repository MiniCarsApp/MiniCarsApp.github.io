#!/usr/bin/env python3
"""Generates the MiniCars website in the app's six languages.

Usage: python3 tools/build.py .   (from the repository root)
"""
import hashlib
import os
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "."

DEVELOPER = "MiniCars"
EMAIL = "minicarsapp@proton.me"
FORM_KEY = "1af8ef65-c6dd-42a8-872e-474a42849f86"
APPLE_PRIVACY = "https://www.apple.com/legal/privacy/"
WEB3FORMS_PRIVACY = "https://web3forms.com/privacy"
PROTON_PRIVACY = "https://proton.me/legal/privacy"
DUTCH_DPA = "https://autoriteitpersoonsgegevens.nl"

# Order of the language menu. Paths are lowercase; the code is the lang attribute.
LANGS = [
    ("en", "/", "English"),
    ("ru", "/ru/", "Русский"),
    ("de", "/de/", "Deutsch"),
    ("es", "/es/", "Español"),
    ("fr", "/fr/", "Français"),
    ("pt-BR", "/pt-br/", "Português (Brasil)"),
]
PATH = {code: path for code, path, _ in LANGS}


def asset(name):
    """Asset URL with a content hash, so browsers fetch the new file after an update
    (GitHub Pages lets browsers cache files for 10 minutes)."""
    with open(os.path.join(OUT, "assets", name), "rb") as fh:
        return f"/assets/{name}?v={hashlib.md5(fh.read()).hexdigest()[:8]}"
SHORT = {"en": "EN", "ru": "RU", "de": "DE", "es": "ES", "fr": "FR", "pt-BR": "PT"}

# ---------------------------------------------------------------------------
# Texts. Feature names match the app's own Localizable.strings.
# ---------------------------------------------------------------------------

T = {}

T["en"] = dict(
    privacy="Privacy Policy", support="Support", language="Language", theme="Switch between light and dark theme",
    footer="MiniCars — a catalog for your diecast model collection.",
    home_lead="Keep your diecast model collection and wishlist on your iPhone and iPad: photos, prices, purchase places, voice notes and statistics.",
    icon_alt="MiniCars app icon",
    tile_privacy="MiniCars collects no data. Everything stays on your device.",
    tile_support="Questions, ideas or a problem? Write to us.",
    effective="Effective November 20, 2026", developer_label="Developer", country="the Netherlands",
    summary="<strong>In short:</strong> the MiniCars app does not collect, store or share your personal data. There is no account, no advertising, no analytics and no tracking. The developer has no servers that receive data from the app — everything you add to it stays on your device.",
    s1="Data you keep in the app",
    s1p1="Models, photos, videos, voice notes and their transcripts, notes, tags, prices, purchase dates and places, and planned purchases are stored only on your device, inside the app's own storage. The developer cannot see or access them.",
    s1p2="If device backups are turned on (iCloud Backup or a computer backup), this data may be included in your backup. Backups are handled by Apple under the <a href=\"{apple}\">Apple Privacy Policy</a> and your device settings.",
    s2="Permissions",
    s2p="The app asks for access only when you use a feature that needs it. You can change any permission at any time in iOS Settings → MiniCars; the rest of the app keeps working.",
    th_perm="Permission", th_use="What it is used for",
    perms=[
        ("Camera", "Taking photos and videos of your models."),
        ("Microphone", "Sound in videos and voice notes."),
        ("Speech recognition", "Turning voice notes into text. Recognition runs on your device only; audio is not sent anywhere."),
        ("Photos", "Adding photos and videos from your library to a model."),
        ("Location (while using the app)", "Marking where you bought a model. To show the address, the coordinates are sent to Apple's map service."),
        ("Contacts", "Choosing a friend to tell about a new model. Contacts are read on your device and are not stored or sent by the app. You send the message yourself through Messages or Mail."),
        ("Calendar", "Adding an event for a planned purchase date through the system calendar screen. On iOS 17 and later no calendar access is requested."),
        ("Face ID, Touch ID or passcode", "Showing hidden prices. The check is done by iOS; the app only receives the result."),
        ("Bluetooth", "“{exchange}” with another collector (see section 3)."),
        ("Notifications", "Reminders on a planned purchase day. Reminders are scheduled on your device."),
    ],
    s3="“{exchange}” over Bluetooth",
    s3p1="“{exchange}” lets two people standing next to each other compare a wishlist with a collection. It works directly between the two devices over Bluetooth, without the internet, and starts only after both people agree.",
    s3p2="Only the following is sent to the other device: the name you choose for the comparison (up to 30 characters), a short code, and for each model in your wishlist or matching model in your collection — vehicle type, make, model, manufacturer, scale, colour, series and catalogue number. Photos, videos, voice notes, notes, tags, prices, dates and places are never sent. The other person's list is used only to show the result and is not saved after you close the screen.",
    s4="Apple services",
    s4p="Maps and address lookup use Apple Maps; messages and e-mails are sent by you through Apple's Messages and Mail. These services are provided by Apple under the <a href=\"{apple}\">Apple Privacy Policy</a>.",
    s5="Export and sharing",
    s5p="Data leaves the app only when you decide so: for example, when you export your collection to a CSV file or share a message about a model through the system share sheet.",
    s6="Deleting your data",
    s6p="You can delete any model with its photos, videos and notes in the app. Deleting the app removes all its data from the device.",
    s7="Contacting support",
    s7p1="When you write to us through the <a href=\"{support}\">support form</a> or by e-mail, we receive your name, e-mail address, the topic and your message. We use them only to answer you and do not share them with anyone for other purposes.",
    s7p2="The form delivers the message through <a href=\"{web3forms}\">Web3Forms</a>, and our mailbox is hosted by <a href=\"{proton}\">Proton Mail</a>. We keep the correspondence as long as needed to help you and then delete it; you can ask us to delete it at any time.",
    s8="Your rights",
    s8p="The developer is based in the Netherlands, and the EU General Data Protection Regulation (GDPR) applies. You have the right to access, correct or delete the personal data we hold about you (in practice, only support correspondence), to restrict or object to its processing and to receive a copy of it. Write to <a href=\"mailto:{email}\">{email}</a>. You can also lodge a complaint with the Dutch Data Protection Authority, <a href=\"{dpa}\">Autoriteit Persoonsgegevens</a>, or the authority in your country.",
    s9="Children",
    s9p="The MiniCars app collects no personal data from anyone, including children.",
    s10="Changes to this policy",
    s10p="If this policy changes, the new version will be published on this page with a new effective date.",
    s11="Contact",
    s11p="{developer}, the Netherlands · <a href=\"mailto:{email}\">{email}</a> · <a href=\"{support}\">support page</a>",
    support_lead="Questions, ideas or a problem with MiniCars? Fill in the form, and we will reply to your e-mail.",
    f_name="Your name", f_email="Your e-mail (for the reply)", f_topic="Topic", f_message="Message", f_send="Send",
    topics=["Question", "Problem or bug", "Idea or suggestion", "Privacy", "Other"],
    f_subject="MiniCars support request",
    f_sending="Sending…", f_ok="Thank you! Your message has been sent. We usually reply within a few days.",
    f_err="The message could not be sent. Please try again later or write to us by e-mail.",
    f_consent="We use your name, e-mail and message only to answer you — see the <a href=\"{privacy}\">Privacy Policy</a>.",
    f_alt="Or write directly to <a href=\"mailto:{email}\">{email}</a>. If something does not work, please mention your device and iOS version.",
    faq="Frequently asked questions",
    faqs=[
        ("Where is my collection stored?", "Only on your device. To keep a copy, turn on iCloud Backup or export the collection in the app: {settings} → {export}."),
        ("A feature asks for access I declined earlier.", "Open Settings → MiniCars on your device and turn the permission on. The app's own {settings} have an “{opensettings}” button."),
        ("How does “{exchange}” work?", "Both people open “{exchange}” in MiniCars with Bluetooth on. After one sends a request and the other accepts, the app shows which models from one wishlist are in the other collection. Only texts are sent — no photos or prices. See the <a href=\"{privacy}\">Privacy Policy</a>."),
        ("How do I delete my data?", "Delete models in the app, or delete the app to remove all its data from the device."),
    ],
    app=dict(exchange="Compare nearby", settings="Settings", export="Export to CSV", opensettings="Open iOS Settings"),
)

T["ru"] = dict(
    privacy="Политика конфиденциальности", support="Поддержка", language="Язык", theme="Переключить светлую и тёмную тему",
    footer="MiniCars — каталог вашей коллекции масштабных моделей.",
    home_lead="Ваша коллекция масштабных моделей и вишлист на iPhone и iPad: фото, цены, места покупки, голосовые заметки и статистика.",
    icon_alt="Иконка приложения MiniCars",
    tile_privacy="MiniCars не собирает данные. Всё остаётся на вашем устройстве.",
    tile_support="Вопрос, идея или проблема? Напишите нам.",
    effective="Действует с 20 ноября 2026 г.", developer_label="Разработчик", country="Нидерланды",
    summary="<strong>Коротко:</strong> приложение MiniCars не собирает, не хранит и не передаёт ваши персональные данные. В нём нет аккаунтов, рекламы, аналитики и отслеживания. У разработчика нет серверов, на которые попадали бы данные из приложения, — всё, что вы в него добавляете, остаётся на вашем устройстве.",
    s1="Данные, которые вы храните в приложении",
    s1p1="Модели, фото, видео, голосовые заметки и их расшифровки, заметки, теги, цены, даты и места покупки, планируемые покупки хранятся только на вашем устройстве, в собственном хранилище приложения. Разработчик их не видит и не имеет к ним доступа.",
    s1p2="Если на устройстве включено резервное копирование (iCloud или компьютер), эти данные могут попасть в резервную копию. Резервными копиями управляет Apple в соответствии с <a href=\"{apple}\">политикой конфиденциальности Apple</a> и вашими настройками.",
    s2="Разрешения",
    s2p="Приложение запрашивает доступ только тогда, когда вы пользуетесь функцией, которой он нужен. Любое разрешение можно изменить в Настройках iOS → MiniCars; остальное приложение продолжит работать.",
    th_perm="Разрешение", th_use="Для чего используется",
    perms=[
        ("Камера", "Фото и видео ваших моделей."),
        ("Микрофон", "Звук в видео и голосовые заметки."),
        ("Распознавание речи", "Расшифровка голосовых заметок в текст. Распознавание идёт только на устройстве, звук никуда не отправляется."),
        ("Фото", "Добавление снимков и видео из вашей медиатеки к модели."),
        ("Геопозиция (при использовании)", "Отметка места покупки модели. Чтобы показать адрес, координаты отправляются в картографический сервис Apple."),
        ("Контакты", "Выбор друга, которому вы хотите рассказать о новой модели. Контакты читаются на устройстве, приложение их не сохраняет и не передаёт. Сообщение отправляете вы сами через «Сообщения» или «Почту»."),
        ("Календарь", "Добавление события на запланированную дату покупки через системный экран календаря. На iOS 17 и новее доступ к календарю не запрашивается."),
        ("Face ID, Touch ID или код-пароль", "Показ скрытых цен. Проверку выполняет iOS, приложение получает только результат."),
        ("Bluetooth", "«{exchange}» с другим коллекционером (см. раздел 3)."),
        ("Уведомления", "Напоминания в день запланированной покупки. Напоминания планируются на устройстве."),
    ],
    s3="«{exchange}» по Bluetooth",
    s3p1="«{exchange}» позволяет двум людям, стоящим рядом, сравнить вишлист одного с коллекцией другого. Обмен идёт напрямую между двумя устройствами по Bluetooth, без интернета, и начинается только после согласия обоих.",
    s3p2="На другое устройство передаётся только: выбранное вами имя для сверки (до 30 символов), короткий код и по каждой модели из вишлиста или совпавшей модели из коллекции — тип техники, марка, модель, производитель, масштаб, цвет, серия и номер по каталогу. Фото, видео, голосовые заметки, заметки, теги, цены, даты и места никогда не передаются. Список собеседника используется только для показа результата и не сохраняется после закрытия экрана.",
    s4="Сервисы Apple",
    s4p="Карты и определение адреса работают через Apple Maps, сообщения и письма вы отправляете сами через «Сообщения» и «Почту» Apple. Эти сервисы предоставляет Apple в соответствии с <a href=\"{apple}\">политикой конфиденциальности Apple</a>.",
    s5="Экспорт и отправка",
    s5p="Данные покидают приложение только по вашему решению: например, когда вы экспортируете коллекцию в файл CSV или отправляете сообщение о модели через системное меню «Поделиться».",
    s6="Удаление данных",
    s6p="Любую модель вместе с фото, видео и заметками можно удалить в приложении. При удалении приложения все его данные удаляются с устройства.",
    s7="Обращения в поддержку",
    s7p1="Когда вы пишете нам через <a href=\"{support}\">форму поддержки</a> или по почте, мы получаем ваше имя, адрес почты, тему и текст сообщения. Мы используем их только для ответа вам и никому не передаём для других целей.",
    s7p2="Форма доставляет сообщение через сервис <a href=\"{web3forms}\">Web3Forms</a>, а наш почтовый ящик размещён в <a href=\"{proton}\">Proton Mail</a>. Переписку мы храним, пока она нужна, чтобы помочь вам, а затем удаляем; вы можете попросить удалить её в любой момент.",
    s8="Ваши права",
    s8p="Разработчик находится в Нидерландах, поэтому действует Общий регламент ЕС по защите данных (GDPR). Вы вправе получить доступ к персональным данным, которые у нас есть (на практике — только к переписке с поддержкой), исправить или удалить их, ограничить их обработку или возразить против неё и получить их копию. Пишите на <a href=\"mailto:{email}\">{email}</a>. Вы также можете подать жалобу в нидерландский орган по защите данных <a href=\"{dpa}\">Autoriteit Persoonsgegevens</a> или в надзорный орган своей страны.",
    s9="Дети",
    s9p="Приложение MiniCars не собирает персональные данные ни у кого, в том числе у детей.",
    s10="Изменения политики",
    s10p="Если политика изменится, новая версия будет опубликована на этой странице с новой датой вступления в силу.",
    s11="Контакты",
    s11p="{developer}, Нидерланды · <a href=\"mailto:{email}\">{email}</a> · <a href=\"{support}\">страница поддержки</a>",
    support_lead="Вопрос, идея или проблема с MiniCars? Заполните форму — мы ответим на вашу почту.",
    f_name="Ваше имя", f_email="Ваша почта (для ответа)", f_topic="Тема", f_message="Сообщение", f_send="Отправить",
    topics=["Вопрос", "Проблема или ошибка", "Идея или предложение", "Конфиденциальность", "Другое"],
    f_subject="Обращение в поддержку MiniCars",
    f_sending="Отправляем…", f_ok="Спасибо! Сообщение отправлено. Обычно мы отвечаем в течение нескольких дней.",
    f_err="Не удалось отправить сообщение. Попробуйте позже или напишите нам на почту.",
    f_consent="Имя, почту и текст сообщения мы используем только для ответа — см. <a href=\"{privacy}\">политику конфиденциальности</a>.",
    f_alt="Или напишите напрямую на <a href=\"mailto:{email}\">{email}</a>. Если что-то не работает, укажите, пожалуйста, устройство и версию iOS.",
    faq="Частые вопросы",
    faqs=[
        ("Где хранится моя коллекция?", "Только на вашем устройстве. Чтобы сохранить копию, включите резервное копирование в iCloud или экспортируйте коллекцию в приложении: {settings} → {export}."),
        ("Функция просит доступ, в котором я раньше отказал.", "Откройте на устройстве Настройки → MiniCars и включите разрешение. В Настройках самого приложения есть кнопка «{opensettings}»."),
        ("Как работает «{exchange}»?", "Оба открывают «{exchange}» в MiniCars с включённым Bluetooth. Когда один отправит запрос, а другой согласится, приложение покажет, какие модели из вишлиста одного есть в коллекции другого. Передаются только тексты — без фото и цен. Подробнее — в <a href=\"{privacy}\">политике конфиденциальности</a>."),
        ("Как удалить мои данные?", "Удалите модели в приложении или удалите само приложение — тогда все его данные будут удалены с устройства."),
    ],
    app=dict(exchange="Сверка рядом", settings="Настройки", export="Экспортировать в CSV", opensettings="Открыть настройки iOS"),
)

T["de"] = dict(
    privacy="Datenschutzerklärung", support="Support", language="Sprache", theme="Zwischen hellem und dunklem Design wechseln",
    footer="MiniCars – ein Katalog für deine Modellauto-Sammlung.",
    home_lead="Deine Modellauto-Sammlung und Wunschliste auf iPhone und iPad: Fotos, Preise, Kauforte, Sprachnotizen und Statistiken.",
    icon_alt="App-Symbol von MiniCars",
    tile_privacy="MiniCars sammelt keine Daten. Alles bleibt auf deinem Gerät.",
    tile_support="Fragen, Ideen oder ein Problem? Schreib uns.",
    effective="Gültig ab 20. November 2026", developer_label="Entwickler", country="Niederlande",
    summary="<strong>Kurz gesagt:</strong> Die App MiniCars erfasst, speichert und teilt keine personenbezogenen Daten. Es gibt kein Konto, keine Werbung, keine Analyse und kein Tracking. Der Entwickler hat keine Server, die Daten aus der App empfangen – alles, was du hinzufügst, bleibt auf deinem Gerät.",
    s1="Daten, die du in der App speicherst",
    s1p1="Modelle, Fotos, Videos, Sprachnotizen und ihre Abschriften, Notizen, Tags, Preise, Kaufdaten und -orte sowie geplante Käufe werden nur auf deinem Gerät im eigenen Speicher der App abgelegt. Der Entwickler kann sie weder sehen noch darauf zugreifen.",
    s1p2="Wenn Gerätebackups aktiviert sind (iCloud-Backup oder Backup auf einem Computer), können diese Daten im Backup enthalten sein. Backups werden von Apple gemäß der <a href=\"{apple}\">Datenschutzrichtlinie von Apple</a> und deinen Geräteeinstellungen verwaltet.",
    s2="Berechtigungen",
    s2p="Die App fragt nur dann nach Zugriff, wenn du eine Funktion nutzt, die ihn braucht. Jede Berechtigung kannst du jederzeit in den iOS-Einstellungen → MiniCars ändern; der Rest der App funktioniert weiter.",
    th_perm="Berechtigung", th_use="Wofür sie genutzt wird",
    perms=[
        ("Kamera", "Fotos und Videos deiner Modelle aufnehmen."),
        ("Mikrofon", "Ton in Videos und Sprachnotizen."),
        ("Spracherkennung", "Sprachnotizen in Text umwandeln. Die Erkennung läuft nur auf deinem Gerät; der Ton wird nirgendwohin gesendet."),
        ("Fotos", "Fotos und Videos aus deiner Mediathek zu einem Modell hinzufügen."),
        ("Standort (beim Verwenden der App)", "Markieren, wo du ein Modell gekauft hast. Um die Adresse anzuzeigen, werden die Koordinaten an den Kartendienst von Apple gesendet."),
        ("Kontakte", "Einen Freund auswählen, dem du von einem neuen Modell erzählen möchtest. Kontakte werden auf deinem Gerät gelesen und von der App weder gespeichert noch gesendet. Die Nachricht verschickst du selbst über Nachrichten oder Mail."),
        ("Kalender", "Einen Termin für ein geplantes Kaufdatum über die System-Kalenderansicht hinzufügen. Ab iOS 17 wird kein Kalenderzugriff angefragt."),
        ("Face ID, Touch ID oder Code", "Ausgeblendete Preise anzeigen. Die Prüfung übernimmt iOS; die App erhält nur das Ergebnis."),
        ("Bluetooth", "„{exchange}“ mit einem anderen Sammler (siehe Abschnitt 3)."),
        ("Mitteilungen", "Erinnerungen am geplanten Kauftag. Die Erinnerungen werden auf deinem Gerät geplant."),
    ],
    s3="„{exchange}“ über Bluetooth",
    s3p1="Mit „{exchange}“ können zwei Personen, die nebeneinander stehen, eine Wunschliste mit einer Sammlung vergleichen. Das funktioniert direkt zwischen den beiden Geräten über Bluetooth, ohne Internet, und startet erst, wenn beide zustimmen.",
    s3p2="An das andere Gerät wird nur Folgendes gesendet: der Name, den du für den Abgleich wählst (bis zu 30 Zeichen), ein kurzer Code und für jedes Modell deiner Wunschliste bzw. jedes passende Modell deiner Sammlung – Fahrzeugtyp, Marke, Modell, Hersteller, Maßstab, Farbe, Serie und Katalognummer. Fotos, Videos, Sprachnotizen, Notizen, Tags, Preise, Daten und Orte werden nie gesendet. Die Liste der anderen Person dient nur zur Anzeige des Ergebnisses und wird nach dem Schließen des Bildschirms nicht gespeichert.",
    s4="Dienste von Apple",
    s4p="Karten und Adresssuche nutzen Apple Karten; Nachrichten und E-Mails verschickst du selbst über Nachrichten und Mail von Apple. Diese Dienste stellt Apple gemäß der <a href=\"{apple}\">Datenschutzrichtlinie von Apple</a> bereit.",
    s5="Export und Teilen",
    s5p="Daten verlassen die App nur, wenn du es entscheidest: zum Beispiel, wenn du deine Sammlung als CSV-Datei exportierst oder eine Nachricht über ein Modell über das Teilen-Menü des Systems verschickst.",
    s6="Deine Daten löschen",
    s6p="Du kannst jedes Modell mit seinen Fotos, Videos und Notizen in der App löschen. Wenn du die App löschst, werden alle ihre Daten vom Gerät entfernt.",
    s7="Kontakt mit dem Support",
    s7p1="Wenn du uns über das <a href=\"{support}\">Support-Formular</a> oder per E-Mail schreibst, erhalten wir deinen Namen, deine E-Mail-Adresse, das Thema und deine Nachricht. Wir verwenden sie nur, um dir zu antworten, und geben sie nicht für andere Zwecke weiter.",
    s7p2="Das Formular stellt die Nachricht über <a href=\"{web3forms}\">Web3Forms</a> zu, unser Postfach wird bei <a href=\"{proton}\">Proton Mail</a> betrieben. Wir bewahren den Schriftverkehr so lange auf, wie es nötig ist, um dir zu helfen, und löschen ihn dann; du kannst die Löschung jederzeit verlangen.",
    s8="Deine Rechte",
    s8p="Der Entwickler hat seinen Sitz in den Niederlanden, es gilt die EU-Datenschutz-Grundverordnung (DSGVO). Du hast das Recht auf Auskunft, Berichtigung und Löschung der personenbezogenen Daten, die wir über dich haben (in der Praxis nur Support-Schriftverkehr), auf Einschränkung der Verarbeitung, Widerspruch und eine Kopie deiner Daten. Schreib an <a href=\"mailto:{email}\">{email}</a>. Du kannst dich außerdem bei der niederländischen Datenschutzbehörde <a href=\"{dpa}\">Autoriteit Persoonsgegevens</a> oder der Behörde in deinem Land beschweren.",
    s9="Kinder",
    s9p="Die App MiniCars erfasst von niemandem personenbezogene Daten, auch nicht von Kindern.",
    s10="Änderungen dieser Erklärung",
    s10p="Wenn sich diese Erklärung ändert, wird die neue Fassung mit neuem Gültigkeitsdatum auf dieser Seite veröffentlicht.",
    s11="Kontakt",
    s11p="{developer}, Niederlande · <a href=\"mailto:{email}\">{email}</a> · <a href=\"{support}\">Support-Seite</a>",
    support_lead="Fragen, Ideen oder ein Problem mit MiniCars? Fülle das Formular aus, und wir antworten an deine E-Mail-Adresse.",
    f_name="Dein Name", f_email="Deine E-Mail (für die Antwort)", f_topic="Thema", f_message="Nachricht", f_send="Senden",
    topics=["Frage", "Problem oder Fehler", "Idee oder Vorschlag", "Datenschutz", "Sonstiges"],
    f_subject="MiniCars Support-Anfrage",
    f_sending="Wird gesendet …", f_ok="Danke! Deine Nachricht wurde gesendet. Wir antworten in der Regel innerhalb weniger Tage.",
    f_err="Die Nachricht konnte nicht gesendet werden. Bitte versuche es später erneut oder schreib uns per E-Mail.",
    f_consent="Name, E-Mail und Nachricht verwenden wir nur, um dir zu antworten – siehe <a href=\"{privacy}\">Datenschutzerklärung</a>.",
    f_alt="Oder schreib direkt an <a href=\"mailto:{email}\">{email}</a>. Wenn etwas nicht funktioniert, nenne bitte dein Gerät und deine iOS-Version.",
    faq="Häufige Fragen",
    faqs=[
        ("Wo wird meine Sammlung gespeichert?", "Nur auf deinem Gerät. Für eine Kopie aktiviere das iCloud-Backup oder exportiere die Sammlung in der App: {settings} → {export}."),
        ("Eine Funktion fragt nach einem Zugriff, den ich früher abgelehnt habe.", "Öffne auf deinem Gerät Einstellungen → MiniCars und aktiviere die Berechtigung. In den {settings} der App gibt es auch die Taste „{opensettings}“."),
        ("Wie funktioniert „{exchange}“?", "Beide öffnen „{exchange}“ in MiniCars bei eingeschaltetem Bluetooth. Nachdem einer eine Anfrage gesendet und der andere zugestimmt hat, zeigt die App, welche Modelle der einen Wunschliste in der anderen Sammlung sind. Es werden nur Texte gesendet – keine Fotos und keine Preise. Siehe <a href=\"{privacy}\">Datenschutzerklärung</a>."),
        ("Wie lösche ich meine Daten?", "Lösche Modelle in der App oder lösche die App, um alle ihre Daten vom Gerät zu entfernen."),
    ],
    app=dict(exchange="Abgleich in der Nähe", settings="Einstellungen", export="Als CSV exportieren", opensettings="iOS-Einstellungen öffnen"),
)

T["es"] = dict(
    privacy="Política de privacidad", support="Soporte", language="Idioma", theme="Cambiar entre tema claro y oscuro",
    footer="MiniCars: un catálogo para tu colección de coches a escala.",
    home_lead="Tu colección de coches a escala y tu lista de deseos en el iPhone y el iPad: fotos, precios, lugares de compra, notas de voz y estadísticas.",
    icon_alt="Icono de la app MiniCars",
    tile_privacy="MiniCars no recopila datos. Todo se queda en tu dispositivo.",
    tile_support="¿Preguntas, ideas o algún problema? Escríbenos.",
    effective="Vigente desde el 20 de noviembre de 2026", developer_label="Desarrollador", country="Países Bajos",
    summary="<strong>En resumen:</strong> la app MiniCars no recopila, no almacena ni comparte tus datos personales. No hay cuenta, ni publicidad, ni analítica, ni seguimiento. El desarrollador no tiene servidores que reciban datos de la app: todo lo que añades se queda en tu dispositivo.",
    s1="Datos que guardas en la app",
    s1p1="Los modelos, fotos, vídeos, notas de voz y sus transcripciones, notas, etiquetas, precios, fechas y lugares de compra y las compras previstas se guardan solo en tu dispositivo, dentro del almacenamiento propio de la app. El desarrollador no puede verlos ni acceder a ellos.",
    s1p2="Si tienes activadas las copias de seguridad (copia en iCloud o en un ordenador), estos datos pueden incluirse en ellas. Apple gestiona las copias de seguridad según la <a href=\"{apple}\">Política de privacidad de Apple</a> y los ajustes de tu dispositivo.",
    s2="Permisos",
    s2p="La app solo pide acceso cuando usas una función que lo necesita. Puedes cambiar cualquier permiso en cualquier momento en Ajustes de iOS → MiniCars; el resto de la app sigue funcionando.",
    th_perm="Permiso", th_use="Para qué se usa",
    perms=[
        ("Cámara", "Hacer fotos y vídeos de tus modelos."),
        ("Micrófono", "Sonido en los vídeos y notas de voz."),
        ("Reconocimiento de voz", "Convertir las notas de voz en texto. El reconocimiento se hace solo en tu dispositivo; el audio no se envía a ningún sitio."),
        ("Fotos", "Añadir fotos y vídeos de tu fototeca a un modelo."),
        ("Ubicación (al usar la app)", "Marcar dónde compraste un modelo. Para mostrar la dirección, las coordenadas se envían al servicio de mapas de Apple."),
        ("Contactos", "Elegir a un amigo para contarle sobre un modelo nuevo. Los contactos se leen en tu dispositivo y la app no los guarda ni los envía. El mensaje lo envías tú mismo con Mensajes o Mail."),
        ("Calendario", "Añadir un evento en la fecha de compra prevista con la pantalla del calendario del sistema. En iOS 17 y posteriores no se pide acceso al calendario."),
        ("Face ID, Touch ID o código", "Mostrar los precios ocultos. La comprobación la hace iOS; la app solo recibe el resultado."),
        ("Bluetooth", "«{exchange}» con otro coleccionista (ver sección 3)."),
        ("Notificaciones", "Recordatorios el día de compra previsto. Los recordatorios se programan en tu dispositivo."),
    ],
    s3="«{exchange}» por Bluetooth",
    s3p1="«{exchange}» permite que dos personas que están juntas comparen una lista de deseos con una colección. Funciona directamente entre los dos dispositivos por Bluetooth, sin internet, y empieza solo cuando ambas personas aceptan.",
    s3p2="Al otro dispositivo solo se envía: el nombre que eliges para la comparación (hasta 30 caracteres), un código corto y, de cada modelo de tu lista de deseos o modelo coincidente de tu colección, el tipo de vehículo, la marca, el modelo, el fabricante, la escala, el color, la serie y el número de catálogo. Nunca se envían fotos, vídeos, notas de voz, notas, etiquetas, precios, fechas ni lugares. La lista de la otra persona solo se usa para mostrar el resultado y no se guarda al cerrar la pantalla.",
    s4="Servicios de Apple",
    s4p="Los mapas y la búsqueda de direcciones usan Mapas de Apple; los mensajes y correos los envías tú con Mensajes y Mail de Apple. Apple presta estos servicios según la <a href=\"{apple}\">Política de privacidad de Apple</a>.",
    s5="Exportar y compartir",
    s5p="Los datos solo salen de la app cuando tú lo decides: por ejemplo, al exportar tu colección a un archivo CSV o al compartir un mensaje sobre un modelo con el menú Compartir del sistema.",
    s6="Eliminar tus datos",
    s6p="Puedes eliminar cualquier modelo con sus fotos, vídeos y notas en la app. Al eliminar la app se borran todos sus datos del dispositivo.",
    s7="Contactar con soporte",
    s7p1="Cuando nos escribes con el <a href=\"{support}\">formulario de soporte</a> o por correo, recibimos tu nombre, tu dirección de correo, el tema y tu mensaje. Los usamos solo para responderte y no los compartimos con nadie para otros fines.",
    s7p2="El formulario entrega el mensaje a través de <a href=\"{web3forms}\">Web3Forms</a> y nuestro buzón está alojado en <a href=\"{proton}\">Proton Mail</a>. Conservamos la correspondencia el tiempo necesario para ayudarte y después la eliminamos; puedes pedirnos que la eliminemos en cualquier momento.",
    s8="Tus derechos",
    s8p="El desarrollador está en los Países Bajos y se aplica el Reglamento General de Protección de Datos de la UE (RGPD). Tienes derecho a acceder, rectificar o suprimir los datos personales que tenemos sobre ti (en la práctica, solo la correspondencia con soporte), a limitar su tratamiento u oponerte a él y a recibir una copia. Escribe a <a href=\"mailto:{email}\">{email}</a>. También puedes presentar una reclamación ante la autoridad neerlandesa de protección de datos, <a href=\"{dpa}\">Autoriteit Persoonsgegevens</a>, o ante la autoridad de tu país.",
    s9="Menores",
    s9p="La app MiniCars no recopila datos personales de nadie, tampoco de menores.",
    s10="Cambios en esta política",
    s10p="Si esta política cambia, la nueva versión se publicará en esta página con una nueva fecha de vigencia.",
    s11="Contacto",
    s11p="{developer}, Países Bajos · <a href=\"mailto:{email}\">{email}</a> · <a href=\"{support}\">página de soporte</a>",
    support_lead="¿Preguntas, ideas o algún problema con MiniCars? Rellena el formulario y te responderemos por correo.",
    f_name="Tu nombre", f_email="Tu correo (para la respuesta)", f_topic="Tema", f_message="Mensaje", f_send="Enviar",
    topics=["Pregunta", "Problema o error", "Idea o sugerencia", "Privacidad", "Otro"],
    f_subject="Solicitud de soporte de MiniCars",
    f_sending="Enviando…", f_ok="¡Gracias! Tu mensaje se ha enviado. Normalmente respondemos en unos días.",
    f_err="No se ha podido enviar el mensaje. Inténtalo más tarde o escríbenos por correo.",
    f_consent="Usamos tu nombre, correo y mensaje solo para responderte; consulta la <a href=\"{privacy}\">Política de privacidad</a>.",
    f_alt="O escribe directamente a <a href=\"mailto:{email}\">{email}</a>. Si algo no funciona, indica tu dispositivo y la versión de iOS.",
    faq="Preguntas frecuentes",
    faqs=[
        ("¿Dónde se guarda mi colección?", "Solo en tu dispositivo. Para tener una copia, activa la copia de seguridad en iCloud o exporta la colección en la app: {settings} → {export}."),
        ("Una función pide un acceso que rechacé antes.", "Abre Ajustes → MiniCars en tu dispositivo y activa el permiso. En los {settings} de la app también está el botón «{opensettings}»."),
        ("¿Cómo funciona «{exchange}»?", "Las dos personas abren «{exchange}» en MiniCars con el Bluetooth activado. Cuando una envía una solicitud y la otra acepta, la app muestra qué modelos de una lista de deseos están en la otra colección. Solo se envían textos, sin fotos ni precios. Consulta la <a href=\"{privacy}\">Política de privacidad</a>."),
        ("¿Cómo elimino mis datos?", "Elimina los modelos en la app o elimina la app para borrar todos sus datos del dispositivo."),
    ],
    app=dict(exchange="Comparar cerca", settings="Ajustes", export="Exportar a CSV", opensettings="Abrir Ajustes de iOS"),
)

T["fr"] = dict(
    privacy="Politique de confidentialité", support="Assistance", language="Langue", theme="Basculer entre thème clair et sombre",
    footer="MiniCars — un catalogue pour votre collection de miniatures.",
    home_lead="Votre collection de miniatures et votre liste d’envies sur iPhone et iPad : photos, prix, lieux d’achat, notes vocales et statistiques.",
    icon_alt="Icône de l’app MiniCars",
    tile_privacy="MiniCars ne collecte aucune donnée. Tout reste sur votre appareil.",
    tile_support="Une question, une idée ou un problème ? Écrivez-nous.",
    effective="En vigueur depuis le 20 novembre 2026", developer_label="Développeur", country="Pays-Bas",
    summary="<strong>En bref :</strong> l’app MiniCars ne collecte, ne stocke et ne partage pas vos données personnelles. Il n’y a ni compte, ni publicité, ni analyse, ni suivi. Le développeur n’a aucun serveur qui reçoit des données de l’app : tout ce que vous y ajoutez reste sur votre appareil.",
    s1="Les données que vous conservez dans l’app",
    s1p1="Les modèles, photos, vidéos, notes vocales et leurs transcriptions, notes, tags, prix, dates et lieux d’achat et achats prévus sont stockés uniquement sur votre appareil, dans l’espace de stockage propre à l’app. Le développeur ne peut ni les voir ni y accéder.",
    s1p2="Si les sauvegardes de l’appareil sont activées (sauvegarde iCloud ou sur un ordinateur), ces données peuvent y être incluses. Les sauvegardes sont gérées par Apple conformément à la <a href=\"{apple}\">Politique de confidentialité d’Apple</a> et aux réglages de votre appareil.",
    s2="Autorisations",
    s2p="L’app ne demande un accès que lorsque vous utilisez une fonctionnalité qui en a besoin. Vous pouvez modifier chaque autorisation à tout moment dans Réglages iOS → MiniCars ; le reste de l’app continue de fonctionner.",
    th_perm="Autorisation", th_use="À quoi elle sert",
    perms=[
        ("Appareil photo", "Prendre des photos et des vidéos de vos modèles."),
        ("Micro", "Le son des vidéos et les notes vocales."),
        ("Reconnaissance vocale", "Transformer les notes vocales en texte. La reconnaissance se fait uniquement sur votre appareil ; l’audio n’est envoyé nulle part."),
        ("Photos", "Ajouter à un modèle des photos et vidéos de votre photothèque."),
        ("Localisation (lorsque l’app est active)", "Indiquer où vous avez acheté un modèle. Pour afficher l’adresse, les coordonnées sont envoyées au service de cartes d’Apple."),
        ("Contacts", "Choisir un ami à qui parler d’un nouveau modèle. Les contacts sont lus sur votre appareil ; l’app ne les enregistre ni ne les envoie. Vous envoyez vous-même le message avec Messages ou Mail."),
        ("Calendrier", "Ajouter un événement à la date d’achat prévue via l’écran de calendrier du système. Sous iOS 17 et versions ultérieures, aucun accès au calendrier n’est demandé."),
        ("Face ID, Touch ID ou code", "Afficher les prix masqués. La vérification est faite par iOS ; l’app ne reçoit que le résultat."),
        ("Bluetooth", "« {exchange} » avec un autre collectionneur (voir la section 3)."),
        ("Notifications", "Les rappels le jour d’achat prévu. Les rappels sont programmés sur votre appareil."),
    ],
    s3="« {exchange} » par Bluetooth",
    s3p1="« {exchange} » permet à deux personnes côte à côte de comparer une liste d’envies avec une collection. Cela fonctionne directement entre les deux appareils par Bluetooth, sans internet, et ne commence qu’une fois que les deux personnes ont accepté.",
    s3p2="Seuls les éléments suivants sont envoyés à l’autre appareil : le nom que vous choisissez pour la comparaison (30 caractères maximum), un code court et, pour chaque modèle de votre liste d’envies ou modèle correspondant de votre collection, le type de véhicule, la marque, le modèle, le fabricant, l’échelle, la couleur, la série et la référence catalogue. Les photos, vidéos, notes vocales, notes, tags, prix, dates et lieux ne sont jamais envoyés. La liste de l’autre personne sert uniquement à afficher le résultat et n’est pas conservée après la fermeture de l’écran.",
    s4="Services d’Apple",
    s4p="Les cartes et la recherche d’adresse utilisent Plans d’Apple ; vous envoyez vous-même les messages et e-mails avec Messages et Mail d’Apple. Ces services sont fournis par Apple conformément à la <a href=\"{apple}\">Politique de confidentialité d’Apple</a>.",
    s5="Export et partage",
    s5p="Les données ne quittent l’app que lorsque vous le décidez : par exemple, quand vous exportez votre collection dans un fichier CSV ou partagez un message sur un modèle avec le menu de partage du système.",
    s6="Supprimer vos données",
    s6p="Vous pouvez supprimer n’importe quel modèle avec ses photos, vidéos et notes dans l’app. Supprimer l’app efface toutes ses données de l’appareil.",
    s7="Contacter l’assistance",
    s7p1="Lorsque vous nous écrivez via le <a href=\"{support}\">formulaire d’assistance</a> ou par e-mail, nous recevons votre nom, votre adresse e-mail, le sujet et votre message. Nous les utilisons uniquement pour vous répondre et ne les partageons avec personne à d’autres fins.",
    s7p2="Le formulaire transmet le message via <a href=\"{web3forms}\">Web3Forms</a>, et notre boîte mail est hébergée par <a href=\"{proton}\">Proton Mail</a>. Nous conservons la correspondance le temps nécessaire pour vous aider, puis nous la supprimons ; vous pouvez nous demander de la supprimer à tout moment.",
    s8="Vos droits",
    s8p="Le développeur est établi aux Pays-Bas et le Règlement général sur la protection des données de l’UE (RGPD) s’applique. Vous avez le droit d’accéder aux données personnelles que nous détenons à votre sujet (en pratique, uniquement la correspondance avec l’assistance), de les rectifier ou de les effacer, d’en limiter le traitement ou de vous y opposer et d’en recevoir une copie. Écrivez à <a href=\"mailto:{email}\">{email}</a>. Vous pouvez aussi introduire une réclamation auprès de l’autorité néerlandaise de protection des données, <a href=\"{dpa}\">Autoriteit Persoonsgegevens</a>, ou de l’autorité de votre pays.",
    s9="Enfants",
    s9p="L’app MiniCars ne collecte de données personnelles auprès de personne, y compris les enfants.",
    s10="Modifications de cette politique",
    s10p="Si cette politique change, la nouvelle version sera publiée sur cette page avec une nouvelle date d’entrée en vigueur.",
    s11="Contact",
    s11p="{developer}, Pays-Bas · <a href=\"mailto:{email}\">{email}</a> · <a href=\"{support}\">page d’assistance</a>",
    support_lead="Une question, une idée ou un problème avec MiniCars ? Remplissez le formulaire et nous vous répondrons par e-mail.",
    f_name="Votre nom", f_email="Votre e-mail (pour la réponse)", f_topic="Sujet", f_message="Message", f_send="Envoyer",
    topics=["Question", "Problème ou bug", "Idée ou suggestion", "Confidentialité", "Autre"],
    f_subject="Demande d’assistance MiniCars",
    f_sending="Envoi…", f_ok="Merci ! Votre message a été envoyé. Nous répondons généralement sous quelques jours.",
    f_err="Le message n’a pas pu être envoyé. Réessayez plus tard ou écrivez-nous par e-mail.",
    f_consent="Nous utilisons votre nom, votre e-mail et votre message uniquement pour vous répondre — voir la <a href=\"{privacy}\">Politique de confidentialité</a>.",
    f_alt="Ou écrivez directement à <a href=\"mailto:{email}\">{email}</a>. Si quelque chose ne fonctionne pas, indiquez votre appareil et votre version d’iOS.",
    faq="Questions fréquentes",
    faqs=[
        ("Où est stockée ma collection ?", "Uniquement sur votre appareil. Pour en garder une copie, activez la sauvegarde iCloud ou exportez la collection dans l’app : {settings} → {export}."),
        ("Une fonctionnalité demande un accès que j’ai refusé.", "Ouvrez Réglages → MiniCars sur votre appareil et activez l’autorisation. Les {settings} de l’app proposent aussi le bouton « {opensettings} »."),
        ("Comment fonctionne « {exchange} » ?", "Les deux personnes ouvrent « {exchange} » dans MiniCars avec le Bluetooth activé. Quand l’une envoie une demande et que l’autre accepte, l’app indique quels modèles d’une liste d’envies se trouvent dans l’autre collection. Seuls des textes sont envoyés, sans photos ni prix. Voir la <a href=\"{privacy}\">Politique de confidentialité</a>."),
        ("Comment supprimer mes données ?", "Supprimez les modèles dans l’app, ou supprimez l’app pour effacer toutes ses données de l’appareil."),
    ],
    app=dict(exchange="Comparer à proximité", settings="Réglages", export="Exporter en CSV", opensettings="Ouvrir les Réglages iOS"),
)

T["pt-BR"] = dict(
    privacy="Política de Privacidade", support="Suporte", language="Idioma", theme="Alternar entre tema claro e escuro",
    footer="MiniCars — um catálogo para a sua coleção de miniaturas.",
    home_lead="Sua coleção de miniaturas e sua lista de desejos no iPhone e no iPad: fotos, preços, locais de compra, notas de voz e estatísticas.",
    icon_alt="Ícone do app MiniCars",
    tile_privacy="O MiniCars não coleta dados. Tudo fica no seu dispositivo.",
    tile_support="Dúvidas, ideias ou algum problema? Escreva para nós.",
    effective="Em vigor desde 20 de novembro de 2026", developer_label="Desenvolvedor", country="Países Baixos",
    summary="<strong>Em resumo:</strong> o app MiniCars não coleta, não armazena e não compartilha seus dados pessoais. Não há conta, publicidade, análise nem rastreamento. O desenvolvedor não tem servidores que recebam dados do app — tudo o que você adiciona fica no seu dispositivo.",
    s1="Dados que você guarda no app",
    s1p1="Modelos, fotos, vídeos, notas de voz e suas transcrições, notas, tags, preços, datas e locais de compra e compras planejadas ficam armazenados apenas no seu dispositivo, no armazenamento próprio do app. O desenvolvedor não pode vê-los nem acessá-los.",
    s1p2="Se os backups do dispositivo estiverem ativados (backup do iCloud ou em um computador), esses dados podem ser incluídos no backup. Os backups são gerenciados pela Apple de acordo com a <a href=\"{apple}\">Política de Privacidade da Apple</a> e os ajustes do seu dispositivo.",
    s2="Permissões",
    s2p="O app pede acesso somente quando você usa um recurso que precisa dele. Você pode alterar qualquer permissão a qualquer momento em Ajustes do iOS → MiniCars; o restante do app continua funcionando.",
    th_perm="Permissão", th_use="Para que é usada",
    perms=[
        ("Câmera", "Tirar fotos e gravar vídeos dos seus modelos."),
        ("Microfone", "Som nos vídeos e notas de voz."),
        ("Reconhecimento de fala", "Transformar notas de voz em texto. O reconhecimento é feito apenas no seu dispositivo; o áudio não é enviado a lugar nenhum."),
        ("Fotos", "Adicionar fotos e vídeos da sua fototeca a um modelo."),
        ("Localização (durante o uso do app)", "Marcar onde você comprou um modelo. Para mostrar o endereço, as coordenadas são enviadas ao serviço de mapas da Apple."),
        ("Contatos", "Escolher um amigo para contar sobre um modelo novo. Os contatos são lidos no seu dispositivo e o app não os armazena nem os envia. Você mesmo envia a mensagem pelo Mensagens ou pelo Mail."),
        ("Calendário", "Adicionar um evento na data de compra planejada pela tela de calendário do sistema. No iOS 17 ou posterior, não é solicitado acesso ao calendário."),
        ("Face ID, Touch ID ou código", "Mostrar os preços ocultos. A verificação é feita pelo iOS; o app recebe apenas o resultado."),
        ("Bluetooth", "“{exchange}” com outro colecionador (veja a seção 3)."),
        ("Notificações", "Lembretes no dia da compra planejada. Os lembretes são agendados no seu dispositivo."),
    ],
    s3="“{exchange}” via Bluetooth",
    s3p1="“{exchange}” permite que duas pessoas lado a lado comparem uma lista de desejos com uma coleção. Funciona diretamente entre os dois dispositivos via Bluetooth, sem internet, e só começa depois que as duas pessoas aceitam.",
    s3p2="Somente o seguinte é enviado ao outro dispositivo: o nome que você escolhe para a comparação (até 30 caracteres), um código curto e, para cada modelo da sua lista de desejos ou modelo correspondente da sua coleção, o tipo de veículo, a marca, o modelo, o fabricante, a escala, a cor, a série e o número de catálogo. Fotos, vídeos, notas de voz, notas, tags, preços, datas e locais nunca são enviados. A lista da outra pessoa é usada apenas para mostrar o resultado e não é salva depois que você fecha a tela.",
    s4="Serviços da Apple",
    s4p="Os mapas e a busca de endereços usam o Mapas da Apple; mensagens e e-mails são enviados por você pelo Mensagens e pelo Mail da Apple. Esses serviços são fornecidos pela Apple de acordo com a <a href=\"{apple}\">Política de Privacidade da Apple</a>.",
    s5="Exportação e compartilhamento",
    s5p="Os dados só saem do app quando você decide: por exemplo, ao exportar sua coleção para um arquivo CSV ou compartilhar uma mensagem sobre um modelo pelo menu Compartilhar do sistema.",
    s6="Excluir seus dados",
    s6p="Você pode excluir qualquer modelo com suas fotos, vídeos e notas no app. Ao excluir o app, todos os dados dele são removidos do dispositivo.",
    s7="Contato com o suporte",
    s7p1="Quando você nos escreve pelo <a href=\"{support}\">formulário de suporte</a> ou por e-mail, recebemos seu nome, seu endereço de e-mail, o assunto e sua mensagem. Usamos esses dados apenas para responder a você e não os compartilhamos com ninguém para outros fins.",
    s7p2="O formulário entrega a mensagem por meio do <a href=\"{web3forms}\">Web3Forms</a>, e nossa caixa de e-mail fica no <a href=\"{proton}\">Proton Mail</a>. Guardamos a correspondência pelo tempo necessário para ajudar você e depois a excluímos; você pode pedir a exclusão a qualquer momento.",
    s8="Seus direitos",
    s8p="O desenvolvedor está nos Países Baixos, e aplica-se o Regulamento Geral sobre a Proteção de Dados da UE (RGPD). Você tem o direito de acessar, corrigir ou excluir os dados pessoais que temos sobre você (na prática, apenas a correspondência com o suporte), de restringir ou se opor ao tratamento e de receber uma cópia. Escreva para <a href=\"mailto:{email}\">{email}</a>. Você também pode apresentar uma reclamação à autoridade de proteção de dados dos Países Baixos, a <a href=\"{dpa}\">Autoriteit Persoonsgegevens</a>, ou à autoridade do seu país (no Brasil, a ANPD).",
    s9="Crianças",
    s9p="O app MiniCars não coleta dados pessoais de ninguém, inclusive de crianças.",
    s10="Alterações nesta política",
    s10p="Se esta política mudar, a nova versão será publicada nesta página com uma nova data de vigência.",
    s11="Contato",
    s11p="{developer}, Países Baixos · <a href=\"mailto:{email}\">{email}</a> · <a href=\"{support}\">página de suporte</a>",
    support_lead="Dúvidas, ideias ou algum problema com o MiniCars? Preencha o formulário e responderemos por e-mail.",
    f_name="Seu nome", f_email="Seu e-mail (para a resposta)", f_topic="Assunto", f_message="Mensagem", f_send="Enviar",
    topics=["Dúvida", "Problema ou erro", "Ideia ou sugestão", "Privacidade", "Outro"],
    f_subject="Pedido de suporte do MiniCars",
    f_sending="Enviando…", f_ok="Obrigado! Sua mensagem foi enviada. Normalmente respondemos em alguns dias.",
    f_err="Não foi possível enviar a mensagem. Tente novamente mais tarde ou escreva para nós por e-mail.",
    f_consent="Usamos seu nome, e-mail e mensagem apenas para responder a você — veja a <a href=\"{privacy}\">Política de Privacidade</a>.",
    f_alt="Ou escreva diretamente para <a href=\"mailto:{email}\">{email}</a>. Se algo não funcionar, informe seu dispositivo e a versão do iOS.",
    faq="Perguntas frequentes",
    faqs=[
        ("Onde minha coleção fica armazenada?", "Apenas no seu dispositivo. Para ter uma cópia, ative o backup do iCloud ou exporte a coleção no app: {settings} → {export}."),
        ("Um recurso pede um acesso que recusei antes.", "Abra Ajustes → MiniCars no seu dispositivo e ative a permissão. Nos {settings} do app também há o botão “{opensettings}”."),
        ("Como funciona “{exchange}”?", "As duas pessoas abrem “{exchange}” no MiniCars com o Bluetooth ativado. Depois que uma envia um pedido e a outra aceita, o app mostra quais modelos de uma lista de desejos estão na outra coleção. Só são enviados textos — sem fotos nem preços. Veja a <a href=\"{privacy}\">Política de Privacidade</a>."),
        ("Como excluo meus dados?", "Exclua os modelos no app ou exclua o app para remover todos os dados dele do dispositivo."),
    ],
    app=dict(exchange="Comparar por perto", settings="Ajustes", export="Exportar para CSV", opensettings="Abrir Ajustes do iOS"),
)

# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------


def url(lang, slug):
    return PATH[lang] + (slug + "/" if slug else "")


def fill(text, lang):
    return text.format(
        apple=APPLE_PRIVACY, web3forms=WEB3FORMS_PRIVACY, proton=PROTON_PRIVACY, dpa=DUTCH_DPA,
        email=EMAIL, developer=DEVELOPER,
        support=url(lang, "support"), privacy=url(lang, "privacy"),
        **T[lang]["app"],
    )


def language_menu(lang, slug):
    target = "" if slug == "404" else slug
    items = []
    for code, _, name in LANGS:
        current = ' aria-current="true"' if code == lang else ""
        items.append(f'          <a href="{url(code, target)}" hreflang="{code}" lang="{code}"{current}>{name}</a>')
    return "\n".join(items)


def page(lang, slug, title, description, body):
    t = T[lang]
    if slug == "404":
        alternates = ""
    else:
        alternates = "\n".join(
            f'<link rel="alternate" hreflang="{code}" href="{url(code, slug)}">' for code, _, _ in LANGS
        )

    def nav(target, label):
        current = ' aria-current="page"' if target == slug else ""
        return f'<a href="{url(lang, target)}"{current}>{label}</a>'

    full_title = f"{title} — MiniCars" if slug else "MiniCars"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
{alternates}
<link rel="icon" type="image/png" href="/assets/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="stylesheet" href="{asset("style.css")}">
<script>try{{var t=localStorage.getItem("theme");if(t==="light"||t==="dark")document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
<script src="{asset("theme.js")}" defer></script>
</head>
<body>
<header class="site">
  <div class="wrap">
    <a class="brand" href="{url(lang, "")}"><img src="/assets/icon.png" alt="" width="32" height="32">MiniCars</a>
    <nav class="links">
      {nav("privacy", t["privacy"])}
      {nav("support", t["support"])}
    </nav>
    <div class="controls">
      <details class="langs">
        <summary aria-label="{t["language"]}">{SHORT[lang]}</summary>
        <div class="menu">
{language_menu(lang, slug)}
        </div>
      </details>
      <button type="button" class="theme-toggle" aria-label="{t["theme"]}" title="{t["theme"]}">
        <svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5a8.5 8.5 0 1 0 11 11Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
        <svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
</header>
<main>
  <div class="wrap">
{body}
  </div>
</main>
<footer class="site">
  <div class="wrap">
    <span>{t["footer"]}</span>
    <span>© 2026 {DEVELOPER} · <a href="mailto:{EMAIL}">{EMAIL}</a></span>
  </div>
</footer>
</body>
</html>
"""


def home(lang):
    t = T[lang]
    return f"""    <section class="hero">
      <img src="/assets/icon.png" alt="{t["icon_alt"]}" width="128" height="128">
      <h1>MiniCars</h1>
      <p class="lead">{t["home_lead"]}</p>
    </section>
    <div class="tiles">
      <a class="card" href="{url(lang, "privacy")}"><strong>{t["privacy"]}</strong><span>{t["tile_privacy"]}</span></a>
      <a class="card" href="{url(lang, "support")}"><strong>{t["support"]}</strong><span>{t["tile_support"]}</span></a>
    </div>"""


def privacy(lang):
    t = T[lang]
    rows = "\n".join(
        f"        <tr><td>{name}</td><td>{fill(use, lang)}</td></tr>" for name, use in t["perms"]
    )

    def section(number, key, *paragraphs):
        body = "\n".join(f"    <p>{fill(t[p], lang)}</p>" for p in paragraphs)
        return f"    <h2>{number}. {fill(t[key], lang)}</h2>\n{body}"

    return f"""    <h1>{t["privacy"]}</h1>
    <p class="meta">{t["effective"]} · {t["developer_label"]}: {DEVELOPER}, {t["country"]}</p>

    <div class="card">
      <p>{t["summary"]}</p>
    </div>

{section(1, "s1", "s1p1", "s1p2")}

    <h2>2. {t["s2"]}</h2>
    <p>{t["s2p"]}</p>
    <div class="card table-wrap">
      <table>
        <tr><th>{t["th_perm"]}</th><th>{t["th_use"]}</th></tr>
{rows}
      </table>
    </div>

{section(3, "s3", "s3p1", "s3p2")}

{section(4, "s4", "s4p")}

{section(5, "s5", "s5p")}

{section(6, "s6", "s6p")}

{section(7, "s7", "s7p1", "s7p2")}

{section(8, "s8", "s8p")}

{section(9, "s9", "s9p")}

{section(10, "s10", "s10p")}

{section(11, "s11", "s11p")}"""


def support(lang):
    t = T[lang]
    options = "\n".join(f"            <option>{topic}</option>" for topic in t["topics"])
    faqs = "\n".join(
        f"    <h3>{fill(question, lang)}</h3>\n    <p>{fill(answer, lang)}</p>" for question, answer in t["faqs"]
    )
    return f"""    <h1>{t["support"]}</h1>
    <p class="lead">{t["support_lead"]}</p>
    <div class="card">
      <form id="contact-form" action="https://api.web3forms.com/submit" method="POST"
            data-sending="{t["f_sending"]}" data-ok="{t["f_ok"]}" data-err="{t["f_err"]}">
        <input type="hidden" name="access_key" value="{FORM_KEY}">
        <input type="hidden" name="subject" value="{t["f_subject"]}">
        <input type="hidden" name="from_name" value="MiniCars website">
        <input type="hidden" name="language" value="{lang}">
        <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="field">
          <label for="name">{t["f_name"]}</label>
          <input id="name" name="name" type="text" autocomplete="name" maxlength="100" required>
        </div>
        <div class="field">
          <label for="email">{t["f_email"]}</label>
          <input id="email" name="email" type="email" autocomplete="email" maxlength="200" required>
        </div>
        <div class="field">
          <label for="topic">{t["f_topic"]}</label>
          <select id="topic" name="topic">
{options}
          </select>
        </div>
        <div class="field">
          <label for="message">{t["f_message"]}</label>
          <textarea id="message" name="message" maxlength="5000" required></textarea>
        </div>
        <p class="hint">{fill(t["f_consent"], lang)}</p>
        <button type="submit">{t["f_send"]}</button>
        <p id="form-status" class="status" role="status" aria-live="polite"></p>
      </form>
      <p class="hint">{fill(t["f_alt"], lang)}</p>
    </div>

    <h2>{t["faq"]}</h2>
{faqs}
    <script src="{asset("form.js")}" defer></script>"""


def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full) or ".", exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(html)


for code, path, _ in LANGS:
    base = path.lstrip("/")
    t = T[code]
    write(base + "index.html", page(code, "", "MiniCars", t["home_lead"], home(code)))
    write(base + "privacy/index.html", page(code, "privacy", t["privacy"], f"MiniCars — {t['privacy']}", privacy(code)))
    write(base + "support/index.html", page(code, "support", t["support"], f"MiniCars — {t['support']}", support(code)))

links = " · ".join(f'<a href="{path}" lang="{code}">{name}</a>' for code, path, name in LANGS)
write("404.html", page("en", "404", "Page not found", "Page not found",
                       f"    <h1>Page not found</h1>\n    <p>{links}</p>"))
print("ok:", ", ".join(code for code, _, _ in LANGS))
