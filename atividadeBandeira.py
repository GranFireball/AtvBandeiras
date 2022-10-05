from this import d
from PIL import Image, ImageDraw

def bandeiraJapao(output):
    image = Image.new("RGB", (600, 400), "white")
    draw = ImageDraw.Draw(image)
    draw.chord((180, 100, 400, 320), start=0, end=360, width=40, fill="red") 
    image.save(output) 

def bandeiraAntPort(output):
    image = Image.new("RGB", (600, 400), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((250, 0, 330, 400), width=20, fill="blue") 
    draw.rectangle((0, 150, 600, 230), width=20, fill="blue") 
    image.save(output) 

def bandeiraMatoGrosso(output):
    image = Image.new("RGB", (600, 400), "blue")
    draw = ImageDraw.Draw(image)
    draw.polygon(((50, 200), (300, 340),(300, 60)), fill="white")
    draw.polygon(((550, 200), (300, 340),(300, 60)), fill="white")
    draw.chord((200, 100, 400, 300), start=0, end=360, width=40, fill="green")
    draw.polygon(((205, 170), (395,170), (300, 230)), fill="yellow")
    draw.polygon(((300, 100), (240, 280), (310,230)), fill="yellow")
    draw.polygon(((300, 100), (360, 280), (290,230)), fill="yellow")
    image.save(output) 

if __name__ == "__main__":
    bandeiraJapao("Japao.jpg")
    bandeiraAntPort("AntigaPortugal.jpg")
    bandeiraMatoGrosso("MatoGrosso.jpg")