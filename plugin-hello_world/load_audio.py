from waggle.data.audio import AudioFolder

dataset = AudioFolder("audio_data")

for sample in dataset:
    process_data(sample.data)