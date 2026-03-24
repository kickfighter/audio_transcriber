import whisper
import argparse
import os
from datetime import timedelta

def transcribe_to_srt(input_file):
    # Загружаем модель (автоматически использует GPU если доступен)
    model = whisper.load_model("base")
    
    # Транскрибация с детализацией временных меток
    result = model.transcribe(input_file, word_timestamps=True)
    
    # Генерируем имя выходного файла
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.srt"
    
    # Создаем SRT файл
    with open(output_file, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result["segments"], start=1):
            # Форматируем время для SRT
            start_time = str(timedelta(seconds=segment['start'])).replace('.', ',')
            end_time = str(timedelta(seconds=segment['end'])).replace('.', ',')
            
            # Записываем блок SRT
            f.write(f"{i}\n")
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{segment['text'].strip()}\n\n")
    
    print(f"Транскрипция сохранена в {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Whisper транскрибатор в SRT')
    parser.add_argument('input_file', help='Путь к аудио/видео файлу (mp3, wav, m4a и др.)')
    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"Ошибка: файл {args.input_file} не найден")
    else:
        transcribe_to_srt(args.input_file)
