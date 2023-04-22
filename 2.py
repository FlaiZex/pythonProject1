class MediaPlayer:
    def open(self, file: str) -> None:
        self.filename = file

    def play(self) -> None:
        print(f"Воспроизведение {self.filename}")

if __name__ == "__main__":
    media1 = MediaPlayer()
    media2 = MediaPlayer()

    media1.open("filemedia1")
    media2.open("filemedia2")

    media1.play()
    media2.play()
