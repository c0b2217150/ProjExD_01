import sys
import pygame as pg
def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")  # 練習１：背景画像Surfaceの生成
    kk_img = pg.image.load("ex01/fig/3.png")  # 練習２：こうかとん画像Surfaceの生成
    kk_img = pg.transform.flip(kk_img, True, False)# 練習２：こうかとんの左右反転
    bg_img = pg.transform.flip(bg_img, True, False)  
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]  # 練習３：こうかとんSurfaceのリスト
    bg_img2 = pg.transform.flip(bg_img,True,False)
    tmr = 0
    a = 0
    while True:
        kok_img=pg.transform.rotate(bg_img2,a)
        kk_img3=[bg_img2, kok_img]
        for event in pg.event.get():
            if event.type == pg.QUIT: return


        x=tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(bg_img2, [4800-x, 0])
        screen.blit(kk_imgs[tmr%2], [300, 200])


        



        pg.display.update()
        tmr += 1   
        clock.tick(5000)


if __name__ == "__main__":

    

    pg.init()
    main()
    pg.quit()
    sys.exit()
