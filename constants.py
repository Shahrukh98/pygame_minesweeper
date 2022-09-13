from pygame import display,init

init()
info = display.Info()

WINDOW_WIDTH,WINDOW_HEIGHT=info.current_w,info.current_h
BUTTON_LEFT_OFFSET= 0.1 * WINDOW_WIDTH
TOP_OFFSET = 0.1*WINDOW_HEIGHT