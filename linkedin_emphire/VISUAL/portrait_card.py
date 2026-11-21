#!/usr/bin/env python3
"""Portrait card, layout B from the Tolu study (DAILY CONTENT/2026-11-20_tolu-study_posts-and-cards.md).

Off-white ground, thin outline frame, name chip, heavy headline left, cut-out portrait right,
yellow follow box, black name bar. No verified tick: the profile is not verified.

    python3 VISUAL/portrait_card.py ASSETS/brand/portrait_vest_cutout.png "Headline." VERIFIED_POSTS/<slug>/visual/cover.png 90
"""
import sys, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
cut, headline, out = sys.argv[1], sys.argv[2], sys.argv[3]
W,H=1080,1350
F='/usr/share/fonts/opentype/inter/'
bold=lambda s:ImageFont.truetype(F+'InterDisplay-Bold.otf',s)
semi=lambda s:ImageFont.truetype(F+'InterDisplay-SemiBold.otf',s)
med=lambda s:ImageFont.truetype(F+'InterDisplay-Medium.otf',s)
INK=(17,17,17); YEL=(249,216,17); LINE=(70,70,70)
c=Image.new('RGB',(W,H),(243,242,238)); d=ImageDraw.Draw(c)
random.seed(7)
for _ in range(900):  # paper speckle
    x,y=random.randrange(W),random.randrange(H); r=random.choice((1,1,2))
    g=random.randrange(215,232); d.line((x,y,x+random.randrange(-6,7),y+random.randrange(-6,7)),fill=(g,g,g),width=r)
# frame
d.rounded_rectangle((60,112,670,1150),radius=70,outline=LINE,width=3)
d.rounded_rectangle((395,800,670,1150),radius=40,outline=LINE,width=3)
# quote mark
d.text((800,250),'“',font=bold(260),fill=(225,224,220))
# portrait
p=Image.open(cut).convert('RGBA'); bb=p.getbbox(); p=p.crop(bb)
ph=980; pw=int(p.width*ph/p.height); p=p.resize((pw,ph),Image.LANCZOS)
c.paste(p,(450,H-ph),p)
d=ImageDraw.Draw(c)
# chip over the frame's top line
d.rectangle((105,85,560,140),fill=(243,242,238))
src=Image.open(cut).convert('RGBA'); face=src.crop((330,90,690,450)).resize((76,76),Image.LANCZOS)
av=Image.new('RGB',(76,76),(0,32,64)); av.paste(face,(0,0),face)
mask=Image.new('L',(76,76),0); ImageDraw.Draw(mask).ellipse((0,0,75,75),fill=255)
c.paste(av,(118,74),mask); d.ellipse((116,72,195,151),outline=(255,255,255),width=3)
d.text((212,95),'Olusanya Timothy',font=bold(34),fill=INK)
# headline
f=bold(int(sys.argv[4]) if len(sys.argv)>4 else 92); words=headline.split(); lines=[]; cur=''
for w_ in words:
    t=(cur+' '+w_).strip()
    if d.textlength(t,font=f)<=520: cur=t
    else: lines.append(cur); cur=w_
lines.append(cur)
y=215
for ln in lines:
    d.text((118,y),ln,font=f,fill=INK); y+=int(f.size*1.12)
# follow box
bx0,by0,bx1,by1=118,max(y+40,840),600,max(y+40,840)+130
d.rectangle((bx0,by1,bx1,by1+12),fill=(90,90,90))
d.rounded_rectangle((bx0,by0,bx1,by1),radius=46,fill=YEL,corners=(True,False,False,False))
ix,iy=150,by0+38  # person-plus icon
d.ellipse((ix+40,iy-4,ix+72,iy+28),fill=INK); d.rounded_rectangle((ix+28,iy+30,ix+84,iy+62),radius=16,fill=INK)
d.rectangle((ix,iy+24,ix+26,iy+30),fill=INK); d.rectangle((ix+10,iy+14,ix+16,iy+40),fill=INK)
tf=med(27); tx=ix+108
for i,t in enumerate(['Follow Olusanya Timothy','for AI red teaming','and evaluation']):
    d.text((tx,by0+22+i*32),t,font=tf,fill=INK)
# name bar
d.rectangle((55,1222,830,1290),fill=INK)
d.text((85,1239),'OLUSANYA TIMOTHY  ||  AI RED TEAMING & EVALUATION',font=semi(26),fill=(255,255,255))
c.save(out); c.convert('RGB').save(out.rsplit('.',1)[0]+'.jpg',quality=92)
print(len(lines),'lines, box at',by0)
