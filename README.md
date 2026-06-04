«Project S.I.N.G.U.L.A.R.I.T.Y.» – Audio Player with Visualizer


 English


 Overview
Project S.I.N.G.U.L.A.R.I.T.Y. is a desktop audio player written in Python, HTML5, CSS3, and JavaScript using the «pywebview» library. It offers a modern light‑theme interface, playlist management, an interactive frequency visualizer, metadata support (including embedded cover art), and playback modes (shuffle, repeat). The player runs in its own native window and can play local audio files and folders.


 Key Features
- «Playlist management» – create, rename, delete playlists; add/remove tracks.
- «Playback» – play, pause, previous, next, seek, volume control.
- «Visualizer» – circular frequency‑based visualizer with smoothly shifting colors.
- «Metadata support» – extracts and displays embedded cover art in the center of the visualizer (via jsmediatags).
- «Playback modes» – shuffle and repeat (mutually exclusive).
- «Folder & file import» – add single/multiple audio files or an entire folder of supported formats.
- «Cross‑playlist continuation» – when the current playlist ends, the player automatically switches to the next playlist.
- «Settings dialog» – project info and a link to the author’s VK page.


 Technology Stack
- «Python 3.11.0» – backend / host process.
- «pywebview» – creates a native window and embeds the web frontend.
- «HTML5 / CSS3 / JavaScript» – user interface, player logic, visualizer.
- «Web Audio API» – real‑time frequency analysis.
- «jsmediatags» – extracts cover art from audio files (loaded via CDN).


 Project Structure
The entire application is contained in a single Python file «SINGULARITY.py».  
The file includes:
- A class «WebViewApp» that creates and runs the window.
- A large multi‑line string «HTML_CONTENT» holding the complete HTML/CSS/JS frontend.

There are no external assets – everything is self‑contained.

The application has been converted into an «.exe» file for user convenience.

 Installation & Running
- Download the EXE file from GitHub and use the application immediately.
- Or download the application from the official website.
- Or run the web version directly on the official website.


User Interface & Controls


 Sidebar (collapsible)
- Hover over the left edge or click the “S” icon to expand.
- «Playlist list» – shows all playlists. Hover over a playlist to see rename/delete buttons. Click a playlist name to switch to it.
- «New playlist» – «+» button at the top of the playlist list.
- «Current playlist tracks» – list of tracks in the selected playlist. Hover over a track to see a delete button. Click a track to start playing it.


 Main area
- «Canvas visualizer» – circular animated bars that react to the sound. The center displays the track’s cover art (if available) or a stylized “S” logo.
- «Bottom control bar»:
  - «+» button – opens a mini menu to add audio files or a folder.
  - Transport buttons: previous, play/pause, next.
  - Mode toggles: shuffle (⇄) and repeat (↻) – mutually exclusive.
  - Seek bar – click or drag to change playback position.
  - Volume slider – icon + slider.
  - Track name display – shows the name of the current track (tooltip on hover).
  - Gear button – opens the settings modal.


 Settings modal
- Displays project name, author, version.
- Contains a link to the author’s VK page.


How to Use


 Adding music
- Click the «+» button in the bottom bar, then choose «Add files» (select one or more audio files) or «Add folder» (select a folder – the player will recursively find all audio files).
- All added tracks will be placed into the «currently active playlist».


 Playlist management
- «Create» – click the «+» button next to “PLAYLISTS” in the sidebar.
- «Rename» – expand the sidebar, hover over a playlist, click the pencil icon.
- «Delete» – hover over a playlist and click the trash icon (the last playlist cannot be deleted).
- «Remove track» – expand the sidebar, hover over a track in the current playlist, click the trash icon.


 Playback
- Double‑click (or single‑click) a track in the playlist to start playback.
- Use the buttons on the bottom control bar.
- When a track ends:
  - If «repeat» is on → the track restarts.
  - Else if «shuffle» is on → a random track from the same playlist is played.
  - Else → the next track in the playlist is played.
  - If the playlist ends, the player automatically switches to the next playlist (in creation order) and starts playing its first track.


 Visualizer
- The circular visualizer reacts to the audio frequency spectrum.
- Colors shift smoothly with time and the music’s “energy”.
- If the current track has embedded cover art, it appears in the center and pulses slightly to the beat.


 Important Notes
- Supported audio formats depend on the browser engine used by «pywebview» (usually Chromium). The most common formats (MP3, WAV, OGG, etc.) work.
- Cover art extraction requires the «jsmediatags» library (loaded via CDN). When offline or if the CDN is unavailable, the visualizer will show the “S” logo instead.
- The player uses the Web Audio API; on some systems a user action may be required to start the audio context. Pressing the “play” button initializes it.
- All playlist data and track references are stored only in RAM – they are lost when the page is refreshed or the window is closed. In the current version, saving playlists to disk is not implemented (this is a temporary solution).


 Author & Version
- «Author»: A.A. Korotchenko
- «Version»: 0.8
- Contacts: via VKontakte (link inside the settings window or on the official website), GitHub (link is on the official website)


Русский


Обзор
Project S.I.N.G.U.L.A.R.I.T.Y. — это десктопный аудиоплеер, написанный на Python, html5, css3 и javascript с использованием библиотеки «pywebview». Он предлагает современный светлый интерфейс, управление плейлистами, интерактивный частотный визуализатор, поддержку метаданных (включая встроенные обложки) и режимы воспроизведения (shuffle, repeat). Плеер работает в собственном нативном окне и может проигрывать локальные аудиофайлы и папки.


Ключевые возможности
- «Управление плейлистами» – создание, переименование, удаление плейлистов; добавление/удаление треков.
- «Воспроизведение» – play, pause, предыдущий, следующий, перемотка, регулировка громкости.
- «Визуализатор» – круговой визуализатор на основе анализа частот, с плавно меняющимися цветами.
- «Поддержка метаданных» – извлечение и отображение встроенной обложки в центре визуализатора (через jsmediatags).
- «Режимы воспроизведения» – shuffle и repeat (взаимоисключающие).
- «Импорт папок и файлов» – добавление одного/нескольких файлов или целой папки с поддерживаемыми форматами.
- «Автоматический переход между плейлистами» – когда текущий плейлист заканчивается, плеер переключается на следующий.
- «Диалог настроек» – информация о проекте и ссылка на страницу автора ВК.


Технологический стек
- «Python 3.11.0» – серверная часть (хост-процесс).
- «pywebview» – создание нативного окна и встраивание веб‑фронтенда.
- «HTML5 / CSS3 / JavaScript» – пользовательский интерфейс, логика плеера, визуализатор.
- «Web Audio API» – анализ частот в реальном времени.
- «jsmediatags» – извлечение обложек из аудиофайлов (загружается по CDN).


Структура проекта
Все приложение содержится в одном Python-файле «SINGULARITY.py».  
В файле:
- Класс «WebViewApp», который создаёт и запускает окно.
- Большая многострочная строка «HTML_CONTENT», содержащая полный HTML/CSS/JS фронтенд.


Внешних файлов нет – всё самодостаточно.


Приложение было переведено в exe-файл для удобства пользователей


Установка и запуск
- скачать exe-файл с GitHub и сразу пользоваться приложением
- зайти и скачать приложения с официального сайта
- Запустить веб-версию на официальном сайте


Интерфейс и элементы управления


Боковая панель (сворачивается)
- нажмите курсор на левый край или на значок «S», чтобы развернуть.
- «Список плейлистов» – показывает все плейлисты. При наведении на плейлист появляются кнопки переименования и удаления. Нажмите на имя плейлиста, чтобы переключиться на него.
- «Новый плейлист» – кнопка «+» в верхней части списка плейлистов.
- «Треки текущего плейлиста» – список треков выбранного плейлиста. При наведении на трек появляется кнопка удаления. Нажмите на трек, чтобы начать его проигрывание.


Основная область
- «Визуализатор на canvas» – круговые анимированные полосы, реагирующие на звук. В центре отображается обложка трека (если доступна) или стилизованная буква «S».
- «Нижняя панель управления»:
  - Кнопка «+» – открывает мини-меню для добавления аудиофайлов или папки.
  - Транспортные кнопки: предыдущий, play/pause, следующий.
  - Переключатели режимов: shuffle (⇄) и repeat (↻) – взаимоисключающие.
  - Полоса перемотки – клик или перетаскивание для изменения позиции воспроизведения.
  - Ползунок громкости – значок + движок.
  - Отображение имени трека – показывает название текущего трека (подсказка при наведении).
  - Кнопка шестерёнки – открывает окно настроек.


Окно настроек
- Отображает название проекта, автора, версию.
- Содержит ссылку на страницу автора ВКонтакте.


Как пользоваться


Добавление музыки
- Нажмите кнопку «+» в нижней панели, затем выберите «Add files» (выберите один или несколько файлов) или «Add folder» (выберите папку – плеер рекурсивно найдёт все аудиофайлы).
- Все добавленные треки попадут в «текущий активный плейлист».


Управление плейлистами
- «Создать» – нажмите кнопку «+» рядом с надписью «PLAYLISTS» на боковой панели.
- «Переименовать» – разверните боковую панель, наведите курсор на плейлист, нажмите значок карандаша.
- «Удалить» – наведите на плейлист и нажмите значок корзины (последний плейлист удалить нельзя).
- «Удалить трек» – разверните боковую панель, наведите курсор на трек в текущем плейлисте, нажмите корзину.


Воспроизведение
- Двойным (или одинарным) щелчком по треку в плейлисте начните воспроизведение.
- Используйте кнопки нижней панели для управления.
- Когда трек заканчивается:
  - Если включён «repeat» → трек начинается заново.
  - Иначе если включён «shuffle» → случайный трек из того же плейлиста.
  - Иначе → следующий трек в плейлисте.
  - Если плейлист закончился, плеер автоматически переключается на следующий плейлист (в порядке создания) и начинает проигрывать его первый трек.


Визуализатор
- Круговой визуализатор реагирует на частотный спектр аудио.
- Цвета плавно меняются в зависимости от времени и «энергии» музыки.
- Если у текущего трека есть встроенная обложка, она появится в центре и будет слегка пульсировать в такт.


Важные замечания
- Поддерживаемые аудиоформаты зависят от браузерного движка, который использует «pywebview» (обычно Chromium). Наиболее распространённые форматы (MP3, WAV, OGG и др.) работают.
- Извлечение обложек требует библиотеки «jsmediatags» (загружается с CDN). При отсутствии интернета или недоступности CDN визуализатор покажет логотип «S».
- Плеер использует Web Audio API; на некоторых системах для запуска аудио контекста может потребоваться явное действие пользователя. Нажатие кнопки «play» инициализирует его.
- Все данные плейлистов и ссылки на треки хранятся только в оперативной памяти – при перезагрузке страницы или закрытии окна данные теряются. В текущей версии сохранение плейлистов на диск не предусмотрено (это временное решение).


Автор и версия
- Автор: А.А. Коротченко
- Версия: 0.8
- Контакты: через ВКонтакте (ссылка внутри окна настроек или на страницы официального сайта), GitHub (ссылка есть на официальном сайте)
