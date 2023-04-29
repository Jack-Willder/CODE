from PIL import Image, ImageDraw, ImageFont

text = "How is it Going ?"

# new = Image.new("RGB", (3000, 3000), color=(3, 255, 232))
new = Image.open("C:\CODE\Projects\Attendance Analytics Datasheet\TEST - MODULE - PIL\img.jpg")

d = ImageDraw.Draw(new)

font = ImageFont.truetype(font="arial", size=100)

d.text((100, 100), text=text, fill=(255, 255, 255), font=font, spacing=10)

new.save("hello.png")
