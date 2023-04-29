from PIL import Image, ImageDraw, ImageFont

text = f"""21SCS37    MOHAMED SAMSUL ALAM K             20.5      0     53.41         
21SCS40    MUTHURAJ C                        20        0     54.55         
21SCS22    MOHAMED HAJA SHERIF A             20        0     54.55         
21SCS47    SURIYA M                          19        0     56.82         
21SCS07    ABDUL SALAM I                     19        2     56.82         
21SCS19    MOHAMED AKRAM I                   18.5      0     57.95         
21SCS30    MUSHARAF T                        18        0     59.09         
21SCS10    AL HAJI A                         15.5      0     64.77         
21SCS39    MUGUNTHAN M                       13.5      0     69.32         
21SCS36    DINESH KANNA R                    13.5      0     69.32         
21SCS08    ABUBAKKAR SIDDIK A                13.5      0     69.32         
21SCS33    WAHITH KANI M                     13        0     70.45         
21SCS29    MOHAMMED AFZAR SAMSUDEEN M        13        0     70.45         
21SCS18    MOHAMED ABUBAKKAR SIDDIQ S M S    13        0     70.45         
21SCS09    AHAMED WAJUDEEN S                 12.5      0     71.59         
21SCS44    SELVAN A                          12        0     72.73         
21SCS48    VIGNESH A                         11        0     75            
21SCS35    DEVAK H                           11        0     75            
21SCS42    SABAREESH SOUNDHAR G              10.5      1     76.14         
21SCS32    SYED SIRASUDEEN M                 10.5      0     76.14         
21SCS14    KOTHER THOWFEEK J                 10.5      0     76.14         
21SCS12    JAFFAR SHAFAN N                   10.5      0     76.14         
21SCS23    MOHAMED IQBAL S                   10        0     77.27         
21SCS11    IRFAN K                           10        0     77.27         
21SCS43    SANKARA RAMESWARAN R              9.5       0     78.41         
21SCS26    MOHAMED RISWAN S S                9         0     79.55         
21SCS17    MOHAMED ABDUL RASEETH A K         9         0     79.55         
21SCS06    ABDUL HAMEED S M                  9         0     79.55         
21SCS34    ARUMUGAPERUMAL N                  8.5       0     80.68         
21SCS21    MOHAMED ASRAFF S                  8.5       0     80.68         
21SCS01    GOWSICA K                         8.5       3     80.68         
21SCS31    SYED MOHAMMED ZAHIR HUSSAIN I     8         0     81.82         
21SCS13    JAMAL J M                         8         1     81.82         
21SCS46    VELMURUGAN U                      7.5       0     82.95         
21SCS38    MOHAMED SULAIMAN U                7.5       0     82.95         
21SCS15    MOHAMAD ALHARIS U                 7.5       3     82.95         
21SCS05    SUMAIYA PARVIN N                  7.5       3     82.95         
21SCS04    SANJANA DEVI M                    7.5       3     82.95         
21SCS27    MOHAMED SUHAIL M S                7         0     84.09         
21SCS24    MOHAMED ISMAIL I                  7         0     84.09         
21SCS20    MOHAMED ALI JINNAH S A            7         0     84.09         
21SCS16    MOHAMED AATHIL N K                7         0     84.09         
21SCS28    MOHAMED YUNUS S                   6.5       0     85.23         
21SCS02    JANAKI CAUVERY S                  3.5       3     92.05         
21SCS03    JESINTHA JEYA MOORTHY C           2.5       3     94.32         
21SCS41    RAMALINGAMSABARISH M              2         0     95.45         
"""

# new = Image.new("RGB", (3000, 3000), color=(0, 0, 0))
new = Image.open("C:\CODE\Projects\Attendance Analytics Datasheet\TEST - MODULE - PIL\BG.png")

d = ImageDraw.Draw(new)

font = ImageFont.truetype(font="arial", size=32)

d.text((170, 382.2), text=text, fill=(255, 255, 255), font=font, spacing=15)

new.save("hello-2.png")

# new = Image.open("C:\CODE\Projects\Attendance Analytics Datasheet\TEST - MODULE - PIL\img.jpg")
#
# d = ImageDraw.Draw(new)
#
# font = ImageFont.truetype(font="arial", size=20)
#
# d.text((1500, 100), text=text, fill=(0, 0, 0), font=font, spacing=10)
#
# new.save("hello.png")
