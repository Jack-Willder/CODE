from PIL import Image, ImageDraw, ImageFont

text = "How is it Going ?"

# new = Image.new("RGB", (3000, 3000), color=(3, 255, 232))
new = Image.open("C:\CODE\Projects\Attendance Analytics Datasheet\TEST - MODULE - PIL\img.jpg")

d = ImageDraw.Draw(new)

d.text((1500, 1500), text=text, fill=(255, 255, 255))

new.save("hello.png")
