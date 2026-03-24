Here's a README.md file with both Russian and English sections:

```markdown
# Whisper SRT Transcriber

## English

### Description
This script uses OpenAI's Whisper speech recognition model to transcribe audio and video files into SubRip (SRT) subtitle format. It automatically detects and utilizes GPU if available for faster processing.

### Features
- Supports multiple audio/video formats (mp3, wav, m4a, etc.)
- Automatic GPU acceleration when available
- Generates SRT subtitle files with accurate timestamps
- Preserves original filename with .srt extension

### Requirements
- Python 3.7+
- OpenAI Whisper
- FFmpeg (required by Whisper)

### Installation
```bash
pip install openai-whisper
```

FFmpeg installation:
- **Ubuntu/Debian**: `sudo apt install ffmpeg`
- **MacOS**: `brew install ffmpeg`
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

### Usage
```bash
python transcribe.py <audio_or_video_file>
```

Example:
```bash
python transcribe.py interview.mp3
```
This will create `interview.srt` in the same directory.

### Output Format
The script generates standard SRT format:
```
1
00:00:00,000 --> 00:00:05,000
Transcribed text goes here

2
00:00:05,000 --> 00:00:10,000
Next segment of text
```

### Model
Currently uses the "base" Whisper model. You can modify the model size in the code (`tiny`, `base`, `small`, `medium`, `large`) for different speed/accuracy trade-offs.

---

## Русский

### Описание
Этот скрипт использует модель распознавания речи Whisper от OpenAI для транскрибации аудио и видео файлов в формат субтитров SubRip (SRT). Автоматически определяет и использует GPU, если доступен, для ускорения обработки.

### Возможности
- Поддержка различных аудио/видео форматов (mp3, wav, m4a и др.)
- Автоматическое ускорение на GPU при наличии
- Создание SRT субтитров с точными временными метками
- Сохранение исходного имени файла с расширением .srt

### Требования
- Python 3.7+
- OpenAI Whisper
- FFmpeg (требуется для Whisper)

### Установка
```bash
pip install openai-whisper
```

Установка FFmpeg:
- **Ubuntu/Debian**: `sudo apt install ffmpeg`
- **MacOS**: `brew install ffmpeg`
- **Windows**: Скачайте с [ffmpeg.org](https://ffmpeg.org/download.html)

### Использование
```bash
python transcribe.py <аудио_или_видео_файл>
```

Пример:
```bash
python transcribe.py интервью.mp3
```
Это создаст файл `интервью.srt` в той же директории.

### Формат вывода
Скрипт генерирует стандартный формат SRT:
```
1
00:00:00,000 --> 00:00:05,000
Текст транскрипции здесь

2
00:00:05,000 --> 00:00:10,000
Следующий сегмент текста
```

### Модель
В настоящее время используется модель Whisper "base". Вы можете изменить размер модели в коде (`tiny`, `base`, `small`, `medium`, `large`) для выбора между скоростью и точностью.

---

## Notes / Примечания

- The script processes the entire file at once - for large files, consider using smaller model or GPU acceleration
- Скрипт обрабатывает файл целиком - для больших файлов рекомендуется использовать меньшую модель или GPU
- Supported formats depend on FFmpeg installation
- Поддерживаемые форматы зависят от установки FFmpeg
```
