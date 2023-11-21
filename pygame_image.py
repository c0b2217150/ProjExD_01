import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    k_img = pg.image.load("ex01/fig/3.png")
    k_img = pg.transform.flip(k_img, True, False)
    k_imgs =[k_img,pg.transform.rotozoom(k_img, 4, 1.0), pg.transform.rotozoom(k_img, 7, 1.0), pg.transform.rotozoom(k_img, 10, 1.0)]
    bg_imgs = [bg_img, pg.transform.flip(bg_img, True, False)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200
        
        screen.blit(bg_imgs[0], [-x, 0])
        screen.blit(bg_imgs[1], [1600-x, 0])
        screen.blit(bg_imgs[0], [3200-x, 0])
        screen.blit(bg_imgs[1], [4800-x, 0])

        if tmr % 8 == 0 or tmr % 8 == 7 :
            screen.blit(k_imgs[0], [300, 200])
        elif tmr % 8 == 1 or tmr % 8 == 6:
            screen.blit(k_imgs[1], [300, 200])
        elif tmr % 8 == 2 or tmr % 8 == 5:
            screen.blit(k_imgs[2], [300, 200])
        else:
            screen.blit(k_imgs[3], [300, 200])      

        pg.display.update()
        tmr += 1        
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()