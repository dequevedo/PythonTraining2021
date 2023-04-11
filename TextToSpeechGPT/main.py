import tkinter as tk
import pyaudio
import wave
import os

class AudioRecorder:
    def __init__(self, master):
        self.is_recording = False
        self.chunk = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 1
        self.fs = 44100
        self.frames = []

        self.master = master
        self.master.title("Gravador de Áudio")

        self.record_button = tk.Button(self.master, text="Gravar", command=self.toggle_record)
        self.record_button.pack(pady=20)

    def toggle_record(self):
        if not self.is_recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.sample_format,
                                  channels=self.channels,
                                  rate=self.fs,
                                  frames_per_buffer=self.chunk,
                                  input=True)

        self.frames = []
        self.is_recording = True
        self.record_button.config(text="Parar")

        print("Gravando...")

        self.master.after(100, self.record)

    def record(self):
        if self.is_recording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)
            self.master.after(100, self.record)

    def stop_recording(self):
        print("Gravação finalizada.")
        self.is_recording = False
        self.record_button.config(text="Gravar")

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        file_name = "output.wav"
        if os.path.exists(file_name):
            file_number = 1
            while os.path.exists(f"output_{file_number}.wav"):
                file_number += 1
            file_name = f"output_{file_number}.wav"

        wf = wave.open(file_name, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()

        print(f"Áudio salvo como {file_name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioRecorder(master=root)
    root.mainloop()
